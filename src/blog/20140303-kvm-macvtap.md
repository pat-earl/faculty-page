title: KVM Macvtap vs bridging
tags: linux
summary: Switching my KVM networking from a bridged setup [bridged setup](https://wiki.debian.org/QEMU#Host_and_guests_on_same_network) to `macvtap` got me a **huge performance improvement**. Here are instructions on how to set it up.

I've been using KVM based virtual machine as a web server for a while.
The VM needs a public IP of course, so I used a [bridged setup](https://wiki.debian.org/QEMU#Host_and_guests_on_same_network).
Recently (2014-03-03), however, one of the other machines on my subnet generated some 3Mbps of traffic (to an external server).
This caused my host machine CPU usage to rise to 40%!

I'm guessing this is because the bridged setup put `eth0` in promiscuous mode, and the host kernel has to inspect each packet and decide whether to pass it to the VM guest or not.
I switched my networking setup to `macvtap`, and got a **huge performance improvement**.
The 3Mbps of traffic barely puts a dent on my CPU usage.

## macvtap Setup

Open `virt-manager` and set the following:

    Add Hardware --> Network
    Host device ethXX : macvtap
    Device Model: virtio
    Source Mode: VEPA

Here `ethXX` is your host machines outgoing interface.

## Communication with the host machine.

The only caveat with `VEPA` is that your host machine **CAN NOT** communicate to the guest machine over this interface (unless you have some special *hair pin* switch.)
I worked around this by creating a second `NAT` interface for the guest, and assigning static IP's as follows:

1. Use `virt-manager` to create a second (NAT) interface for the guest.
   Call it `default`. Get the interface up and running in the guest.

2. Run `virsh net-autostart default` to make sure the interface comes up automatically after reboots.

3. Run `virsh net-edit default`.
   It will pop up an XML file with basic network configuration.
   Find the `<dhcp>` section, and below the `<range start... />` line add the line

	    <host mac='guestmac' name='guestname' ip='192.168.122.2' />

4. Edit `/etc/hosts` on the host, and add the line

	    192.168.122.2   guest.host.name

5. Edit `/etc/hosts` on the guest, and add the line

	    192.168.122.1   host.host.name

Now you should have transparent host/guest access on all machines.
(Accessing the guest via an IP address still won't work though; you'll have to use host-names.)
