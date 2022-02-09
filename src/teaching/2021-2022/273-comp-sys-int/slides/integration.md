---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
---

## **Application Integration**

CSC273 - Computing Systems Integration

Prof. Patrick Earl

Spring 2022

---

## **Overview**

- Purpose
- Patterns
- Architectures
- Technologies

---

## What is application integration?

IBM Definition: 

> Application integration is the process of enabling individual applications—each designed for its own specific purpose—to work with one another. By merging and optimizing data and workflows between multiple software applications, organizations can achieve integrations that modernize their infrastructures and support agile business operations.

---

## What is application integration (cont.)?

- Typically the following is required:
  - **Data Integrity** - Keeping shared data consistent 
  - **Workflow** - Orchestrating the integrated flow of multiple activities performed by disparate applications 
  - **User Experience** - Providing access to data and functionality from independently designed applications through what appears to be a single user interface or application service

---

## Purpose

Most applications are developed to one specific thing. They can also be developed at different times, by different developers, vendors, etc. Inherently this means that as designed they are not able to communicate with one another. Leading to "islands" of software.

--

## Purpose

Benefits?

- Modern integration allows for consistent data in a format that is supported across your IT landscape.
- Standard protocols ensure consistent connections. 
- Automation of shared data between applications.
- Complexity is handled by vendors and developers, not the end user.

---

## Purpose

Challenges?

- Complexity of integrating
- Data Integrity 
- Workflow changes
  - Learning curve
  - Presenting of meaningful information

---

## Patterns

- Direct Application to Application Integration
- Use of a 3rd Party Tool 
- APIs - Application Programming Interface
- ERP Systems - *Later*

---

## Patterns

- **Direct Application to Application Integration**
- End user has capability to directly integrate two applications together.
- [Gitlab Integrations](https://docs.gitlab.com/ee/integration/)

---

## Patterns
- *3rd Party Applications**
- [Apache Camel](https://camel.apache.org/)
- Provides frameworks to mirror [Enterprise Integration Patterns](https://camel.apache.org/components/3.15.x/eips/enterprise-integration-patterns.html)

---

## Patterns

- **APIs - Application Programming Interfaces**
- [Wikipedia](https://en.wikipedia.org/wiki/API)
  - > An interface or communication protocol between different parts of a computer program intended to simplify the implementation and maintenance of software.      
- Can be a web-based system, operating system, database, etc.
- Each layer provides a standard form of communicating and data. 
- Most software provides a [developer site](https://docs.gitlab.com/ee/api/) to document how a developer can use their API.

---

## **Sources**

- <https://www.ibm.com/cloud/learn/application-integration>
- <https://martinfowler.com/architecture/>
- Prof. Donna Demarco's Slides on Application Integration