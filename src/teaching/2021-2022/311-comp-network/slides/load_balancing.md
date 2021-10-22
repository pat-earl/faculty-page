---
title: "Load Balancing"
subtitle: "CSC311"
author: Patrick Earl
date: 10/2021
slideNumber: true
revealjstheme: robot-lung
width: 1600
height: 1000
transition: slide
---

## Load Balancing

* A single machine can only handle a finite amount of requests before becoming "overloaded."
  * Storage, Processing, Memory Limitations etc.
* Load Balancing allows for spreading requests across different "machines" running the same application.
* Your client sends requests to a single "public" facing machine.
  * The request is handle by a server in the "background" of that public facing IP. 
  * Various technologies and algorithms exist to implement this.

---

## Load Balancing Algorithms
* Dynamic
  * Least Connection
  * Weighted Least Connection
  * Weighted Response Time
  * Resource-based
* Static
  * Round Robin
  * Weighted Round Robin
  * IP Hash

---

## DNS Load Balancing
* Using DNS responses to direct responses to different machines
  * i.e. Have 5 IP addresses.
  * Using a Round Robin approach, respond with the first IP address every 5th time.
* Drawbacks?

---

## Proxying
* Have a machine act on a client's behalf. 
  * Forward Proxy
  * Reverse Proxy

---

## References
* [Types of Load Balancing](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)