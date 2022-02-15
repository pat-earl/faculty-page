---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
---

# **Application Programming Interfaces**

CSC273 - Computing Systems Integration

Prof. Patrick Earl

Spring 2022

---

# **Overview**

1. HyperText Transfer Protocol (HTTP)
2. Web-Based APIs
3. Using APIs

---

# **HyperText Transfer Protocol (HTTP)**

- Most widely used protocol on the internet. 
- Application Layer Protocol
- Client/Server Model 
- Request/Reply Messages

---

# HTTP Requests

- Different Methods (Actions):
  - `GET`
  - `PUT`
  - `HEAD`
- Message Format
  - Start Line 
  - Headers
  - Blank Line
  - Body
  
---

# HTTP Replies

- Status Codes
- Message Format:
  - Start Line
  - Headers
  - Empty Line
  - Body

---

# **RESTFUL API**

- **REST**
  - `REpresentational State Transfer`
- A set of guiding principles to implement a REST service

---

# Six Guiding Principles

1. Uniform Interface
2. Client-Server
3. Stateless
4. Cacheable
5. Layered System
6. Code on demand (Optional)

---

# Uniform Interface

- Allow for simplifying an overall system
- Four Constrains:
  - Identification of Resources
  - Manipulation of Resources through Representations
  - Self-Descriptive Messages
  - [Hypermedia as the Engine of Application State](https://restfulapi.net/hateoas/)

---

# Client-Server

- Enforce **Separation of Concerns**
  - Client and Server Components can change independently
- Portability

---

# Stateless

- Each response from the server contains all the information a client needs to understand and complete the request.
- Clients are responsible for keeping session state
- Servers cannot take advantage of any previous session context

---

# Cacheable

- A response should implicitly or explicitly label itself as cacheable or non-cacheable. 
- If so, the client can reuse the response data later for similar requests and over a specified period. 

---

# Layered System

- Allows for an architecture composed of hierarchical layers, where each component has constrains.
- Each component cannot see beyond the immediate layer they are interacting with

---

# Code on Demand

- Client functionality can be extended by downloading and executing code in the form of applets or scripts. 
- Can simply a client by reducing the number of features that are pre-implemented. 
  - Servers can provide part of the features to the client in code, leaving the client to execute it.

---

# Resources

- [What is REST?](https://restfulapi.net/)