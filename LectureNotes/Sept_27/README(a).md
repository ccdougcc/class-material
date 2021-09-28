# Lecture Notes for September 27, 2021


## Agenda 27th
  1. Quick questions
     - Understanding the syntax of bash programming
     - Clarifying things as I ran into the problems -- Devils in the detail
     - Details of how to program and the structure of the program
     - How to deal with GET versus POST on the programming side.
       - Analysis Paralaysis: Remember, start simple and add.
     - How to define the structure of something I don't fully understand.
     - Questions about the HTTP Request/Response Format?
     - ~Professor is asking for to much~
     - ~Professor describes the material in a very poor way~
     - There is a lot and is dense, and we go to fast -- but we have seen it before
     - Individuals need to practice on there own.  (Baby spoonfuls)

 
  1. Interview Question:
     * Explain what happens when a user types following into their browser:
       - https://www.domain.com/path/to/document?var=value;var=value#section
     * Possible answers:
       1. Simpliest 
          - takes me to a web page
          - sends a message to a web server, and the web sends a response
          - we check a datase to determine the IP address of the server, and send a message there
       1. Detailed Oriented
          1. a request is sent to the webserver
          2. the webserver runs through a series of steps
          3. One step is the content-generator to produce the answer, which is either:
             - a static file like foo.html
             - a dynamic file like index.php
          4. I know of three types of content-generators
             - plain-html
             - cgi
             - as-is
          5. A Handler is called for each specific file type
          6. I create new handlers and add to the system
             - AddHandle  large-html  .x-html
          7. after the content-generator executes some additional work is performed to create the HTTP response
          8. the theHTTP response is sent back to the client

  1. AddHandler:  A Content-generator
     - Bland .html -- just cat the file
     - Review asis
       - special first line:   status: 200 description
       - replace the first with HTTP response line
       - add two fields
       - add the rest of the file
       * usage: send-as-is filename
    - Reviewed the premortal-http server
    - Reviewed the send-as-is script and file type
    - Reviewed the plain-html script

  1. Built Handler for .x-html files
     1. Create a new content generator for Large files
        - if file is greater the X
          - set application/x-html
          - run compress on the file
          - run base64 encode
        - else use the .html content handler

  1. Discussed a new cit384-curl that understands the "application/x-html" type
     - Runs the curl with -i options, places the result into a temp file
     - Examines the value of content-type
     - cat "HTTP Response header"
     - cat ""   # the HTTP Respons blank line
     - if content-type == application/x-html then
            cat "HTTP Response body" | base64 -d | uncompress -
         else 
            cat "HTTP Response body ""


# (well not yet) Lab Assignment: .x-html
  1. To be provided after the lecture
  1. To be completed by the start of next lecture
  1. Create a new content generator for Large files
     - if file is greater the X
       - set application/x-html
       - run compress on the file
       - run base64 encode
     - else use the .html content handler





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

# (well not yet) Lab Assignment: .x-html
  1. To be provided after the lecture
  1. To be completed by the start of next lecture
  1. Create a new content generator for Large files
     - if file is greater the X
       - set application/x-html
       - run compress on the file
       - run base64 encode
     - else use the .html content handler


#
