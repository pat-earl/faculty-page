title: Accessing Journals via an SSH proxy
tags: linux
summary: Most universities have IP based authentication for access to Journals and index sites ([MathSciNet](http://www.ams.org/mathscinet/search.html), [Web of Knowledge](http://www.webofknowledge.com), etc.) If you're off campus, they usually provide some VPN client (e.g. Cisco) which is quite painful to work with (at least on Linux). However, if you have [ssh](http://www.openssh.com/) access to a machine on campus, you can access set up a proxy and access journals very easily.

Most universities have IP based authentication for access to Journals and index sites ([MathSciNet](http://www.ams.org/mathscinet/search.html), [Web of Knowledge](http://www.webofknowledge.com), etc.)
If you're off campus, they usually provide some VPN client (e.g. Cisco) which is quite painful to work with.
However, if you have [ssh](http://www.openssh.com/) access to a machine on campus, you can access journals very easily.

This method can also be used to access Gmail from China, or any site that is firewalled from the region you are currently in, **provided** you have `ssh` access to a host from which the site is not firewalled.
This should also work on Macs.

1. Open a terminal and type:

        ssh -D9050 you@campus.machine.edu

2. Leave the terminal open.

3. Open a browser and set it to use `localhost:9050` as a SOCKS proxy.
   In FireFox go to *Preferences / Advanced / Network / Settings* (as of 2014-03-03) and

    1. Check *Manual proxy configuration*

    2. Type `127.0.0.1` into the SOCKS host field, and `9050` into the port field.

    3. Use `SOCKSv5`

    4. Check `Remote DNS`

That's it.
Now accessing any site from your browser will make the request appear to come from your campus computer.
Once you're done with your access to the restricted resources, exit the `ssh` connection, and reset your browsers proxy settings to NONE.

## Tunneling SSH over an SSH proxy

Recently (2014-12-22) I found [github] firewalled from my current location (India).
While the above easily allowed me to access the website from my browser, I couldn't directly access any [github] hosted repositories.
Turns out that you can tell `ssh` to use a proxy to use a site quite easily:

1. Install a version of `netcat` that support proxies (on Debian systems, install the `netcat-openbsd` package; the `netcat-traditional` package **does not** have proxy support, and won't work in this situation).

2. Edit `~/.ssh/config` and add the following:

        Host github.com
            ProxyCommand nc -x localhost:9050 %h %p

3. As before `ssh -D 9050 ...` and leave the terminal open.

Now `ssh` connections to this host will use the proxy and circumvent the firewall.
This means you can `git pull` happily from your [github] repositories.
When you're done, close the terminal window with the ssh connection.

[github]: https://github.com
