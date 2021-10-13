# Lecture Notes for October 13, 2021


## Interview Question:
   * Have you every deployed a webserver that supports a set of users?
   * Explain how you did it and what are the important considerations?

## Agenda 13th

### Work on a new lab:
  1. New Lab: https://classroom.github.com/a/CVBl2oB0
  1. Due Date: Saturday night, 11:59 PM

  1. Create a dockerfile from scratch
  1. deploy an apache webserver
  1. configure it to server up users
     - add the UserDir module
     - configure the apache server with the appropriate directives
  1. create a user
  1. deploy the users public_html and it's contents
     - which is there resume

  ---
  1. Built via a github context
  1. Automated started via docker build, docker run on 
     - your laptop for testing and development
     - cit384- VM for production

### Comments on the cit384-
  1. Any issues with your VM, contact Yolanda directly
  1. If you don't get sufficient satisfaction
     - feel free to escalate the issue up the administrative chain
