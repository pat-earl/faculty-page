username: https://me.yahoo.com/a/JqpsIBMjv9jsUXpBXR5z9EeP.g--#ccb4b
name: Stefan
avatar: http://cdn.libravatar.org/avatar/c49731b61c656f5e79ac795c3739f889f212a1d96f001526715fdb73907ec41c
subject: lost at the beginning
date: 2015-07-05 20:35:50
 
I'd like to work through this manual, but at the very beinning I already get lost.
Perhaps it is due to the translation of virt-manager's interface (v1.0.1 running on Netrunner v16 distro) :

I can not find the place / menu to 

Add Hardware --> Network

In the following I had to translate back - so please excuse the different terms:

1. So if i right - klick on localhost (QEMU) ... I can go on with New VM - wrong place
2. Menu File - Add connection - wrong place
3. Menu File - New virtual machine - see 1.  - wrong place
4. Edit Connection details seems promising due to this contains the tabs:
 "overview / Virtual Netzworks / Memory(or storage)/ LAN-Adapters (containing lo)
4a) when I add a LAN connection the only choices are:
  Bridge / Bond / Ethernet / VLAN
Here I added eth0 and neither can make it a macvtap nor can I delete / remove this choice. Even not by calling sudo virt-manager

So where might I add the eth0 macvtap?
