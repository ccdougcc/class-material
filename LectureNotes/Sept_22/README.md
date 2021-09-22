# Lecture Notes for September 22, 2021

 

## Agenda 22th
  1. Pickup from last time, i.e., questions, etc.
  1. Quick review
  1. More content Generators
     - asis handler
     - cgi handler
     - html handler

  1. HTTP/s Server Overview
     1. Accept Request:
        1. socket();  # Buying the phone
        1. listen();  # Phone is read to hear someone call
        1. LOOP
           1. accept();
           1. fork();

  1. Read HTTP Request (partially)
     1. Read Request Line: e.g., 
        - GET /\~steve/ HTTP/1.1   : HTTP_METHOD, URI, PROTOCOL
     1. Read the header values (store them some place)
     1. Read the blank line
     1. Defer reading body

  1. Call in turn the input filters

  1. Rewrite the URI into the filename
     - /\~steve/cgi-bin/emit-cgi-env.cgi  
     - /home/users0/ccs/steve/public_html/cgi-bin/emit-cgi-env.cgi 
     - Apache Directives
       1. DocumentRoot /var/html/
       1. UserDir public_html
           - lookup the home directory of \~steve
           - append ${UserDir}
           - append the rest of the URI

  1. Invoke the Contenter Generator (Handler)
      1. AddHandler cgi-script .cgi
      1. AddHandler send-as-is  asis
      1. ~Addhandler plain-html .html~


## Content-Generator: .html
     1. Write media type in the head:   content-type: plain/html
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







## Lab Assignment:
  1. To be provided at the start of the lab
  1. To be completed by the end of the assignment
  
