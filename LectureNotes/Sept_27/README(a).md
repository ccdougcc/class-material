# Lecture Notes for September 27, 2021


## Agenda 27th
  1. Quick questions
 

  1. Interview Question:
     * Explain what happens when a user types following into their browser:
       - https://www.domain.com/path/to/document?var=value;var=value#section
     * Possible answers:
 

  1. End-to-end Review

  1. Client URL -- Server Filename
     - https://www.sandbox.csun.edu/calstatepays -> 
       (https://www.sandbox.csun.edu/calstatepays/#/data/majors)
       - web-prod-0.sandbox.csun.edu:/var/www/calstatepays/index.php
     - https://www.sandbox.csun.edu/~steve/cgi-bin/emit-cgi-env.cgi
       - ssh.sandbox.csun.edu:\~steve/public_html/emit-cgi-env.cgi
     - https://www.csun.edu/~steve/cgi-bin/emit-cgi-env.cgi
       - ssh.csun.edu:/home/users0/ccs/steve/webdrive/public_html/cgi-bin/emit-cgi-env.cgi

     - Apache Directives
       1. DocumentRoot /var/html/
       1. UserDir public_html
          - lookup the home directory of \~steve
          - append ${UserDir}
          - append the rest of the URI

  1. Client-side (browser):
     - Server must already be listening for requests!
     - Parser the URL: https://www.domain.com/path/to/document?var=value;var=value#section
     - Build the Request Payload
     - Establish a Socket 
     - Send Request
     - Receive Payload

  1. Server-side (http server):
     - Establish a socket
     - Read (partially) the HTTP Request
     - Execute input filters
     - Determine the filename of the document
     - Execute the appropiate handler
       - asis handler
       - cgi handler
       - html handler

     - Execute output filters  
     - Write the HTTP Response (to the client)
     - Close the connection 


## Content-Generator: .html
   1. Write media type in the head:
      - content-type: text/html
      - content-length: $(stat -f "%z" ${filename})
   1. write blank line
   1. cat the filename.html

## Content-Generator: asis
   1. Read the first line: status: 200 Cool
   1. Transform that line to:  HTTP/1.1 200 
   1. Add two fields:
      - Date:
      - Server:
   1. cat the rest of the file

## Content-Generator: .cgi



## (well not yet) Lab Assignment: .x-html
  1. To be provided after the lecture
  1. To be completed by the start of next lecture
  1. Create a new content generator for Large files
     - if file is greater the X
       - set application/x-html
       - run compress on the file
       - run base64 encode
     - else use the .html content handler


