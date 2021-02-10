title: CSC411 Lab #2

## Lab Objectives

* Design and implement addressing scheme (subnets/CIDR)
* How routing tables effect traffic

## Description

You're a network administrator for a business that is opening up two new
offices. You'll need to create an addressing scheme for the current
office building as well the new ones. The current number of hosts are as followed:
1) 50 hosts, 2) 300 hosts, 3) 75 hosts. 
You'll also need to consider the potential growth that the networks will
need to handle and provide your justification on your projection. 

Decide what IP address block you'll be using for the three networks. You also 
need to provide addresses for the routers connecting the network together. Create
the addressing scheme with either subnetting or CIDR. You need to provide
the subnet mask, network address, broadcast address, and host IP range for
each office network and the routers. 

You'll be implementing this addressing scheme with network simulation software.
Your simulation needs to include the following for each network:

* Edge Router
* Switch
* At least two hosts

Once you have created your addressing scheme, you'll need a routing table
to allow for communication between your networks. Provide your addressing
scheme to the instructor, who will provide you with a routing table.

The first host IP should be used for the router interface connected
to the switch.

The diagram below gives a general idea of what your simulation should look like.

![](./csc411-lab2-diagram.png)

## Deliverables

* Individual exports of the finished labs from PT & GNS3.
* Collaborative Solution Manual for completing the lab 

