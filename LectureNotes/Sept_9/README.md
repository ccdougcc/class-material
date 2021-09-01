# Lecture Notes for September 1, 2021

## Agenda
  1. Announcements
     - VMs
       * before, e.g, steve.csun.edu | now, e.g., cit384-steve.csun.edu
       * ssh tunnel to k200.ecs.csun.edu is now working

     - Power Outage
       * no UPS
       * no generator
       * no gracefull shutdown of services
       * Disks that were damaged
          - LDAP directory & VMs for CIT384 had disk damage
          - waiting on Purchasing to cut a PO
       * no backups
       * no automation....

     - Code snippets
     - Safari

  1. git practicum
     - Four areas of concern: Working Directory, Staging Area, Local Rep, Remote Repo
     - clone, push, pull, add, rm, checkout, fetch, status

  1. ssh login review
     - HTML code staging
     - XML stanza
     - mime: multipurpose internet mail extenstion 
    
  1. git process for CV lab
     - branches, etc.
     - review process

  1. HTML review
     - HTML (HyperText Markup Language : structure, hierarchical in nature
     - HTML TAGS or ELEMENTS
        - html: head, body
        - ol & ul  (ordered and unorder lists)
          - li: list items
        - table:  tr, th, td
        - footnote
        - p
        - h1, h2, h3, h5, ...
        
     - CSS (Cascading Style Sheets): all about style
     - Javascript: all about actions



### Notes
  1. K200 misconfig
  ```
  $ hostname ; curl --head https://www.ecs.csun.edu/~steve/
k200.ecs.csun.edu
  $ git clone https://github.com/CIT384/CV-webpage.git
-ksh: git: not found [No such file or directory]
  ```
