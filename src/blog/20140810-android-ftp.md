title: Transfering files to Android Devices in Linux
tags: linux, android
summary: Transfering files to/from a android device to a Linux box via `mtp-tools`, FTP over USB, or ssh.

The usual way to transfer files directly over USB is to use [mtp-tools].
Unfortunately this doesn't work for all devices (e.g. my HTC Evo), and even if it does work you have to use a primitive interface.

Here are a couple of methods I use to transfer files:

1. **ftp:** This is fast, but insecure.
   **ONLY USE THIS OVER USB.**
   As an added bonus: If you set this up, then you can use your phone's mobile network on your computer (provided you have your USB cable with you).

2. **ssh/sftp:** This is slow (~200kbps), but secure and convenient.
   I use this over mobile networks, wifi, etc.

## FTP over USB, and sharing your phones network over USB.

### Setting up the USB network adapter.

1. Find your *USB network settings* on your Android device, and set it to *USB tethering*. (This requires that your Android device is connected to the internet.)

2. Now plug it in to your PC and do the following (as root):

        root> ifconfig -a | grep usb
        usb0      Link encap:Ethernet  HWaddr 8a:b7:da:a4:78:ff

    If you see output (as above), you're in good shape.
   Open `/etc/network/interfaces` in your favourite editor (as root) and add the following stanza:

        allow-hotplug usb0
        iface usb0 inet dhcp

    Now run (as root) `if up usb0`, and you should see the network come up.
   (It should also come up automatically when you plug in your Android device again.)
   As a bonus, if your PC is not connected to the internet (and your Android device is), then you can now access the internet on your computer through your Android device! (Beware data charges...)

To transfer files, you need to set up *either* your Android device or your Desktop as an FTP server.
You can transfer files in both directions either way, and there is no real advantage of one over the other.
It's just which interface you prefer using. 

### Connecting to your Android device from your PC.

This is a little simpler than the other way around.

1. Install an FTP server on your Android device.
   There are many free ones available.

2. If your FTP server app allows you to choose the network interface, set it to the USB network adapter.

3. **Change the default port, username, password, and DISABLE anonymous logins.**

4. Start the server.
   It should show you an IP address, port, username and password on the screen.
   Connect to this from your PC:

        ftp -P <port> <user>@<IP.address>

5. **Important:** You might see multiple IP addresses for the server.
   Be sure to connect to the one corresponding to the USB network.
   You can figure this out by finding out the IP address of `usb0` on your PC.
   FTP is completely insecure.
   If you FTP to your phone over the wireless (or mobile network) someone can sniff your password.
   But if you only connect over USB, then you're safe.

6. Transfer whatever you want using `mget` / `mput` whatever you want.
   Your photos should be in the `DCIM` folder. With my computer / phone I get speeds of about 2MB/s.

### Connecting to your PC from your phone.

If you prefer not to have an FTP server on your phone, then you can set one up on your computer.
It is a little more complicated to set up securely though.
I set it up so that:

1. FTP is only accessible through the USB network interface.

2. You have access to all your local files through ftp.

3. You to log in with a password that is different from your login password, so your precious desktop password isn't cached on an insecure phone (or accidentally sent in clear text over the internet).

If you're not as paranoid, the setup is a little easier.
Here are instructions for the paranoid that will work on Debian (and should also work on Ubuntu/others).

1. Run the following as root:

        aptitude install vsftpd libpam-pwdfile

2. Make `/etc/pam.d/vsftpd` look like the following:

        :::shell
        # Standard behaviour for ftpd(8).
        auth	required	pam_listfile.so item=user sense=deny file=/etc/ftpusers onerr=succeed

        # Note: vsftpd handles anonymous logins on its own. Do not enable pam_ftp.so.

        # Customized login using htpasswd file
        auth    required pam_pwdfile.so pwdfile /etc/vsftpd.passwd flock
        @include common-account
        @include common-session

3. You need to put a username and password-hash in `/etc/vsftpd.passwd`.
   To find the password hash, run:

        :::shell
        root> perl -e '$salt=q($1$).int(rand(1e8)); print "password: ";
            chomp($passwd=<STDIN>); print crypt($passwd,$salt),"\n"'
        password: helloworld
        $1$88946554$UjFicyn04d43zuF2ojx0L0

    (When prompted for a password, type something better than *helloworld*).
   Copy the output (the `$1...` string). This is your password hash.

    Now edit `/etc/vsftpd.passwd` and put the following in it:

        :::yaml
        username:$1$88946554$UjFicyn04d43zuF2ojx0L0

    where *username* is the name of the **local user on your machine**.
   Replace `$1$88...` with your password hash of course.

4. Edit `/etc/vsftpd.conf` and set the following:

        :::cfg
        anonymous_enable=NO
        write_enable=YES
        local_umask=022
        local_enable=YES
        virtual_use_local_privs=YES

5. Block FTP connections from everything other than `usb` networks: If you're using [ufw] (which I strongly recommend) edit `/etc/ufw/before.rules`.
   Find a line that looks like:

        ufw-before-input -p udp -d 239.255.255.250 --dport 1900 -j ACCEPT

    After that (and certainly before the `COMMIT` line) add the lines:

        :::shell
        # Accept ftp only over usb
        -A ufw-before-input -p tcp --dport 21 ! -i usb+ -j REJECT

    Restart your firewall. (If you don't know how to flush rules properly, reboot. Don't simply `service ufw restart`, as that never works well for me.)

6. Test it out:

        :::shell
        root> service vsftpd restart
        user> ftp user@localhost

    You should be able to log in with the password you typed above (instead of *helloworld*) and **not** your regular password.

7. If everything worked fine so far, then you can try connecting from your Android device.
   Install an FTP client on your Android device and add a new FTP connection.
   Use the IP address of your desktop's USB interface, your local username, and the password you just created.
   After this you should be able to drag and drop files from your PC as needed.

## SSH/SFTP.

Using SSH is slow on my devices, because the Android devices CPU doesn't seem to be powerful enough to encrypt more than data at rates more than 200kbps.
But it is secure enough to be used over WiFi and mobile networks, so it is quite useful to set up.
There are two ways to do this: From your device, or from your computer.

### SSH from your Android device to your Desktop

I strongly recommend setting this up. It's easy, and super useful.

1. Set up an [SSH server](https://wiki.debian.org/SSH) on your Desktop. (You probably have this done already.)

2. Install an SFTP client on your Android device.
   Create a new connection and enter your login information.

4. For better security, generate an ssh key on your desktop, copy it over to your phone and use it.
   This way your precious UNIX password is not stored in clear text on the android device.
   (Expiring a compromised SSH key is a lot easier than changing your password on all your machines.)

### SSH from your Desktop to your Android

This is not as useful, but does have a certain "geek appeal". It's also very
easy to do: Just go to the Google play store and install any one of many *SSH
Servers*. Start it and follow the instructions.

[mtp-tools]: http://libmtp.sourceforge.net/

[ufw]: https://wiki.ubuntu.com/UncomplicatedFirewall
