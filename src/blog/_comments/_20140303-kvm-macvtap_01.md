name: GI
email: gi1242@gmail.com
avatar: http://cdn.libravatar.org/avatar/1d9eff8253e59f5c7c243a8c558e4f98c0b2d3df3533dc05a5da7adffc798be2
subject: Network unreachable after upgrade to qemu-1.1.2+dfsg-6a+deb7u2
date: 2014-05-03 15:49:47

After upgrading on 2014-05-02 and rebooting my system my precious `macvtap` was unreachable.
On my host I could see the interface, but was unable to send or receive anything on it.
I realized that after an upgrade of QEmu (not libvirt!) on the host, my host interface `eth1` wasn't being put in promiscuous mode.
A temporary fix is to run

    ifconfig eth1 promisc

after which everything should work.

For a permanent solution, put the following in `/etc/network/interfaces`:

```shell
iface eth1 inet dhcp
    up ifconfig $IFACE promisc
    # Your custom network commands
    # ...
    down ifconfig $IFACE -promisc
```

Hopefully this bug should go away soon.
