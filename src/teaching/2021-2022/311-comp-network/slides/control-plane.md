---
title: "Chapter 5: Control Plane Overview"
subtitle: "CSC311"
author: Patrick Earl
date: 11/3/2021
slideNumber: true
revealjstheme: robot-lung
width: 1920
height: 1080
transition: fade
---

## Control Plane Overview
* These slides are adopted from the Chapter 5 slide deck.
* We're going to skip over most of the concepts in the control plane and focus on these:
    * ICMP
    * BGP
    * Some guiding principles

---

## The Network-Layer Functions
* Forwarding: Move packets from router's input link to appropriate output link (Data)
* Routing: Determine route taken by packets from source to destination (Control)
* The two approaches:
    * Per-Router
    * Logically Centralized Control (SDN)
    * *More on this in a bit*

---

## Error Reporting: ICMP
* **ICMP:** Internet Control Message Protocol
* Used by hosts and routers to communicate network-level information. 
    * Error Reporting: Unreachable host, network, port, protocol, etc.
    * Echo reply/request (**Ping**)
* ICMP packets are encapsulated inside IPv4 packets
    * The format of the header depends on the type, the first 8 bytes are fixed. 
    * *Type*, *Code*, *Checksum*, *Rest of Header*

---

## ICMP - Ping & Traceroute
* Stuff

---

## Per-Router
![](./images/traditional-routing.png)

---

## Software Defined Networking
![](./images/sdn-routing.png)

---

## Routing: Overview
* **Goal:** Determine "good" paths from sending hosts to receiving host, through a network of routers.
    * *Path:* The sequence of routers that a packet transverse. 
    * *Good?*

---

## Routing Among ISPs: BGP
* TODO