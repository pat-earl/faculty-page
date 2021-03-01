title: CSC411 SNMP Lab

## Lab Objectives

* Learn how SNMP operators and use SNMP to view router/switch information

## Description

This is going to require some research on your part. Packet Tracer provides a MIB Browser built-in to the PCs, but GNS3 might be a little bit more difficult.
[Here is a blog post about SNMP in PT](https://receponer.wordpress.com/2016/11/24/configure-snmp-protocol-on-cisco-packet-tracer/).

[A post for GNS3 that requires adding a "cloud" to GNS3](https://www.gullynetworkers.com/2019/04/snmp-lab-on-gns3.html). Be careful with this one, see if there is a better solution out there for this.

Use the previous lab (CSC411 Lab #2). Using the devices in Network A, do the following:

1. Assign the following MIB variables to a switch 
   1. sysContact
   2. sysLocation
   3. sysName
2. Do an "SNMP Walk" of the mgmt.system subtree
3. Do an "SNMP Get" of the sysName and sysLocation variables

## Turn In
* Screenshots of the commands and their output from above
* Solution Manual

Place Teams folder called "CSC411 SNMP Lab"
