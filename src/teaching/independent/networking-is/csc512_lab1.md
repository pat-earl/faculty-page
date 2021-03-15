title: CSC512 Routing Protocols Lab

## Lab Objectives

* Pick a routing algorithm to route traffic between three separate networks.  
* Explore how the protocol updates the routing table based on network changes.
* Use NAT addressing on one of the networks

## Description

Using the CSC411 Lab 2 network, change the routers to use a routing protocol 
instead of static routes. Implement one protocol that is vendor-specific and 
one with cross-vendor support. 

*PROTOCOL NOTES:*
: Do one protocol in PT and one in GNS3. Don't try to implement two protocols in the same simulator (?)
: Pick the same two and implement them in opposite programs. Meaning if you decide to use *RIP* as one, one person implements it in PT and the other in GNS3. 

Implement NAT addressing on *one* of the routers. You can implement any of
the three types. The local network will need to use a private IP address
scheme on the LAN. Explain your NAT type choice and your new address scheme for that network.

After successfully integrating a routing protocol and NAT do the following:

1. Take a screenshot of the routing tables in *each* router
2. Run a traceroute from a host on your NAT'd network to any other network and include a screenshot. 
3. Run a traceroute between any of the hosts on separate networks and take a screenshot.
    1. *Break* the router link used by the packet. 
    2. Run another traceroute between the same two hosts and take another screenshot. Document and explain the changes (if any) you see between the screenshots.
    3. Take a screenshot of the routing tables.

## Submission

* Individually: An export of the labs from each simulator. 
* Collab: A solution manual outlining how to complete the labs. Make sure to include the screenshots as outlined above. 
    