title: Using Box.com cloud storage on Linux

Recently [CMU] announced all users will have 1TB of space of cloud storage at
[Box.com]. This motivated me to set it up on my Linux box. I have not tired to
get syncing working, since I'm perfectly happy with my [unison] set up. But I
can now mount it as a local folder and copy files back and forth.

## Using davfs2 to mount your Box.com storage.

1. Install [davfs2] (on Ubuntu/Debian type `aptitude install davfs2` as root).

2. **Allow `mount.davfs2` to be installed with SUID bit set**. The installation
   prompts for it on Debian. If you made the wrong choice use `dpkg-reconfigure
   davfs2` (as root).

3. Edit `/etc/fstab` and add the line

        # BOX WebDAV
        https://dav.box.com/dav /home/gautam/net/box davfs user,rw,noauto 0 0

    Replace `gautam` with your username and `net/box` with the path in your
   home folder.

4. Add yourself to the `davfs2` group (type `gpasswd -a gautam davfs2` as root,
   log out and log back in.)

5. If you use a single sign on to access your share, then you need to create an
   external password. Login to [Box.com], go to `Account settings / Account`
   and create an external password.

6. Edit `~/.davfs2/secrets` and add the line

        /home/gautam/net/box <email> <password>

    [CMU] users, use your `xxx@andrew.cmu.edu` email and your **external**
   password from above. Regular [Box.com] users, use the email address you use
   to sign on to your account. You can also omit the password and the client
   will prompt you every time you want to mount it.

7. `mount ~/net/box` (as a normal user), and you should have your [Box.com]
   files in this folder.

8. When you're done (esp. before you go offline) be sure to `umount ~/net/box`,
   since your changes might only be cached on your local machine and not synced
   to the server.

### Limitations

1. As of 2015-08-07 `davfs2` doesn't support symbolic links.

2. Uploading some 2GB of data (many small files) took a really long time on a
   very fast connection.

3. Can't seem to update sharing and permissions from the file-system, and have
   to use the website.

## Syncing to [Box.com]

There is an experimental open-source (third party) sync client
[here](https://github.com/noiselabs/box-linux-sync).
There is also a [Python API](http://opensource.box.com/box-python-sdk/)
provided. But I haven't tried either.


## Using [Box.com] on Mobile devices.

They seem to have apps for most platforms [here](https://www.box.com/personal/mobile-access/).

[CMU]: http://www.cmu.edu

[Box.com]: http://www.box.com

[unison]: http://www.cis.upenn.edu/~bcpierce/unison/

[davfs2]: http://savannah.nongnu.org/projects/davfs2
