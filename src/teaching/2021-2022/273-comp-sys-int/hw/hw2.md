title: Homework #2
breadcrumb: ../index.md

**Due:**
: Friday, March 4th

**Purpose:**
: Demonstrate an understanding of using a REST API.
: Reinforce understanding of HTTP request METHODs.

## Description

Part of your company's onboarding process for developers is to set up the new employee's 
GitLab account. So far this has been a manual process where you receive an email
from HR with the person's info, company e-mail, etc and enter it using Gitlab's web interface.
You recently found out that HR's software provides
a REST API you can use to pull the information. Since you've wanted to automate this task,
you decide to use GitLab's API to take the information returned from the HR software and create
this new account.

The endpoint for the HR software is here: <https://randomuser.me/api/> (This probably isn't a real-
world example of how'd this work, but is an example data format you'd work with).

To figure out your design, you'll need to comb through the [REST API](https://docs.gitlab.com/ee/api/api_resources.html)
documentation for GitLab to see what endpoints you'll need. 

You are going to write a high-level design on how you would perform this process. **You do not need to write any code for this assignment.**

For each endpoint you decide to use, explain the HTTP method you need to use, what parameters are need,
and an example of what the endpoint would look like in an actual request. Also explain what access
level you need and how Gitlab's API allows for you to authenticate.

At a minimum, you should have the following three steps:

1. A request to get the information from the HR software would look like
2. A request to create a new GitLab user would like.
3. A request you could make to confirm that the new user was created. 

You may add in more details if you'd like.

To submit your assignment, upload it to the D2L `Homework #2` assignment dropbox. Make sure your
document is in Word or PDF format. 