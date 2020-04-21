title: Remotely waking computers behind newer TP Link routers
summary: I just bought a TP-Link AX 3000 to replace my old router. My previous router had OpenWrt on it -- so to wake up any of my home computers remotely, I could just ssh to my router and run `wol`. OpenWRT is't yet supported on this router, however it's possible to enable with the stock firmware. Here's how:

{{summary}}

1. Open the Router web configuration interface, and switch to the "Advanced" tab.

2. Go to Network » DHCP server » Address reservation, assign a static IP to machine you want.

3. Go to Security » IP &amp; Mac Binding. Find your machine in the "ARP list", and click the link icon on the far right.  It should then show up in the "Binding list" below, and be listed as "Bound" in the ARP list.

4. Go to NAT Forwarding » Virtual Servers and create a new service called WakeOnLan: 
    - Set external port to anything (say 9999)
    - Set internal port to 9
    - Set internal IP to the static address of your machine.

5. Create a service for SSH, whatever other services you need.
   (Changing the external SSH port to something other than 22 reduces the number of brute force attacks on your router by a lot.)

6. Go to Network » Dynamic DNS and enable one of the many services.

7. Now you can wake your computer remotely by:

        wakeonlan -p 9999 -i router.tplinkdns.com <Mac Address>

    and then connect to it by

        ssh -p XXXX router.tplinkdns.com

    For multiple computers, just assign different external ports for each computer.

