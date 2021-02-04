title: CSC411 Lab #2

## Lab Objectives

* Design and implement addressing scheme (subnets/CIDR)
* How routing tables effect traffic

## Description

You're a network administrator for *Earl's Electronics*, which saw a huge growth in customers over 
the previous year. The owner has decided that one store is no longer enough and wants to expand
with two new stores. The current network design doesn't support the addition of new stores and will
have to be discarded. 

You're tasked with creating a new addressing scheme for the network. When planning the new network 
addressing scheme you'll also need to plan for growth. The list below will provide more information
for each store. Each store should be on it's own subnet. 

* **Original Store**
  * Currently has 20 IPs split among the business offices and cash registers.
  * The store is being remodelled to handle 10 more administrative office 

Recreate the network shown in the diagram below. There will be three networks, each with at least two hosts, a Layer-2 switch, and an edge router. All edge routers should be connected to each other.

Three class-full IP blocks have been provided. Figure out the 
network, broadcast, and host addresses for each network. 
*Use the first available IP address on the interface connecting the router to the switch.*

The fourth class A network is used for addressing the connected routers. The IP addresses to be used for the interfaces connecting the routers has been provided. 

A routing table will be provided upon figuring out the IP addresses for the three networks.

* Network A:
    - **193.45.50.0 Class C Network**
    - 3 Hosts (A, B, C)
* Network B:
    - **173.40.0.0 Class B Network**
    - 3 Hosts (D, E, F)
* Network C: 
    - **78.0.0.0 Class A Network**
    - 3 Hosts (G, H, I)
* Network D (Router Connections)
    - **10.0.0.0 Class A Network**
    - Use IP addresses provided on the router interfaces

![](./csc411-lab2-diagram.png)

## Deliverables

* Individual exports of the finished labs from PT & GNS3.
* Collaborative Solution Manual for completing the lab 

