---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
title: Introduction to Microservices
---

## **Microservices Introduction**

CSC273 - Computing Systems Integration

Prof. Patrick Earl

Spring 2022

---

## **Monolithic Architecture**

- Software applications which are built as a single unit. CSC242 - Web Projects
    - Database
    - Client-Side View (HTML, CSS, and JS)
    - Server-Side Application (PHP)
- To make changes to the system, updates must be pushed to the service-side application.
- Deployment of the system is dependent on system administrators. 

---

## **Microservice Architecture**

- A recent software development approach that splits software into smaller services that complete single business functions. 
- Making software easier to develop, debug, deploy, and maintain. 
- Updates to one the services no longer requires changes to the entire system, just to the service in question. 
- Microservices can interact with a database or each other using different protocols.
    - Such as HTTP/REST.

--- 

## Advantages

- Different programming languages can be used for each service.
- Code base of a single service can be smaller. 
- Individual DevOps process to build and deploy the activities.
- Different services can be scaled independently.
- No Single Point of Failure.
- Isolation can lead to better security.
- Outsourcing of individual services. 
- Reusable

---

## Disadvantages

- Splitting into too many microservices can overload the development process. 
- Design of interaction protocols. 
- Expensive for small development teams. 

Systems designed using the microservice architecture basically become distributed computing systems
which can cause unforeseen bugs. 

---

## **Microservice Deployment**

- Typically small, but complete web services. Containers are usually the preferred method of deployment. 
- Changes the typical SysAdmin role into a DevOps role. 
    - DevOps is a culture within software engineering. 
    - Software Engineers become System Administrators and vice versa. 

---

## **DevOps**
- DevOps (**Dev**eloper **Op**erations) focuses on automating the packaging and deployment of a software system to the end user or market. 
- Typical Stages in delivery of an application (automating as much as possible):
    - Building
    - Testing
    - Packaging
    - Releasing/Deployment
    - Monitoring
- DevOp ideas can be brought into monolithic servers, but is hard to do due to their inflexible nature. 

---

## What are containers?

- Programs are ran in an isolated environment on one operating system. 
    - Comparing to Virtual Machines which require the use of a "guest" operating system. 
- Docker is the most popular technology in use today for containerization. 

---

## Continuous Integration

- **Continuous Integration** (CI) is the process of keeping a primary copy of software and using tests/merging process to expand the features for a given application. 
    - CI is integrated with a **Source Code Management** tool such as *Git*. 
- When the source code gets updated, CI can automatically check the code and test it.
- Assuming the tests pass, the application can be packaged into a container. 
    - The resulting container can be used to updated the deployed version.
    - This process can also be automated. 

---

## Reasons to avoid monoliths

**1 - Impossible to scale vertically**

- Application Scaling:
    - **Horizontal**: New instances of an application are started to handle the amount of requests. 
    - **Vertically**: Improvement of an independent bottleneck application layer.

---

## Reasons to avoid monoliths

**2 - Impossible to update and deploy only one feature**

- Feature changes, additions, or removal require stopping, updating, and starting of a monolithic server. 
    - a.k.a. System Downtime. 
- Microservices can avoid downtime if a bug is affecting a single service. 

---

## Reasons to avoid monoliths

**3 - The failure of one server affects all features**

- Crashing of the server, crashes all the features of an application. 
    - Even if a given feature isn't required for the system to work. 

---

## Breaking an example Monolithic Service into pieces

- Example e-commerce monolith service with the following features:
    - User Registration
    - Product Catalog
    - Shopping Cart
    - Payment Integration
    - E-Mail Notifications
    - Statistics Collection

---

## Sources

- [Microservices vs Monolith: Which architecture is the best choice for your business?](https://www.n-ix.com/microservices-vs-monolith-which-architecture-best-choice-your-business/)
- [Hands-On Microservices with Rust](https://www.packtpub.com/product/hands-on-microservices-with-rust/9781789342758) by Denis Kolodin