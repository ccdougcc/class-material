# Lecture Notes for September 8, 2021


## Agenda
 1. Announcements
    - Personal VMs
      * they have been provisioned but not fully tested
      * login to your VM
      * report any problems to "Barrett, Yolanda" <yolanda.barrett@csun.edu>
    - SSH Tunnelling on K200
      * This has been fixed
      * Suggestion: add the following to your .ssh/config file
      ```
      Host k200
         User <userid>
         Hostname k200.ecs.csun.edu
         ProxyJump <userid>@ssh.csun.edu

      Hostname cit384
         User <userid>
         Hostname cit384-<userid>.csun.edu
         ProxyJump <userid>@ssh.csun.edu
      
      ```
    - K200 self-communication has been resolved
    - K200 git software has been installed
    ```
    curl --head https://www.ecs.csun.edu/~steve/  > /dev/null
    git clone https://github.com/CIT384/CV-webpage.git
    
    ```

  1. Basic HTML
    - CIT160 review
      * HTTP Protocol:  
        - Verbs:
        - Request Box, and Response Box
        - Header and Body
      * HTTP payload (aka the Body)
        - It can be anything you want it to be
        - Header specified: mimetype  (Content-type:)
        - Payload specified: comment in payload  (\<!DOCTYPE html\>, #!)
      * XML: Extensible Markup Language is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.
      * HTML: just a instance of XML
    - HTML Document  (HTML Tutorial: https://www.w3schools.com/html/default.asp)
      * HTML provides structure
      * CSS provides style
      * Javascript provides interactivity
    - HTML Document Structure
      * Comments: <!--  comment string -->
      * Node, Tag, Element
        - Empty (\<br\>) and (\<img/\> Void elements
      * Attributes: alt, id, class, href

      * Examples of Structure:
        - Document: head, body, footer
        - List:
        - Table: 
            * elements
            * rows and columns
            * name of the table
            * name of the row
            * name of the column
    - HTML Formating
      * Box Model
      * Formating Elements
        - (old - new) formating elements: avoid the old formating elements
        - E.g., ( \<bold\> - \<strong\>), (\<i\> - \<em\>)

      * Attributes
        - e.g., "style" is an attribute
        - a CSS style had a property and a value: "background-color:powderblue;"
      *

