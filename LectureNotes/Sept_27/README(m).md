# Lecture Notes for September 27, 2021


## Agenda 27th
  1. Quick questions
     - as-is-as assignment ?  How it fits?
     - how a bash script executes under the cgi protocol
     - X- header fields, and how do we know what the value should be for them

  1. Interview Question:
     * Explain what happens when a user types following into their browser:
       - https://www.domain.com/path/to/document?var=value;var=value#section
     * Possible answers:
       1. First
          - DNS is used to determine IP of www.domain.com
          - connects to IP address, check protocol
            - three-way handshake 
          - sends /path/...  to the webserver
          - Not sure about the ";"
          - Fragement (#section) is not sent to the server, but handled by the client
       1. Addition
          - The /path/.. that is sent  within a HTTP Request Message
          - the response (?) is sent within a HTTP Response Message
       1. Addition
          - the query string within the URL starts with the ? mark
          - the query string is something that can be sent to the dynamic document.
       1. Addition
          - the HTTP Request is composed of a request line:  verb uri HTTP/1.1
          - the HTTP Response is compose of a line:  protocol status status_description
          - ? more info is needed on the struct of the HTTP box

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
       * protocol: https
       * userinfo: anonymous (implicit)
       * server_name: www.domain.com
       * TCP port: 443 (implicit: defined by the protocol)
       * path: /path/to/document
       * query_string: var=value;var=value  
         - the & or ; is used to separate components of the query string
         - there is no defined standard to parse the query string
       * fragment: section
         - this is not sent to the server

     - Build the Request Payload
       - SOF (start of file)   -------------------------------------
       - Request line:         GET path?query_string HTTP/1.1
       - Header Info:          host: server_name
       - More header info\*:   X-anything:  value
                               Content-Type: text/html    (Mime Type)
                               Content-Length: 453        (size of Body in bytes is 453)
       - Blank Line:
       - Body (optional)       //html code that is a total of 453 bytes
       - EOF (end of file)     -------------------------------------

     - Establish a Socket 
       - is a layer 4 network connection..
       - a simple tool to this is "socket"
       - DNS lookup on www.domain.com: 127.0.0.1
       - TCP connection:
         - allocate space for the socket(127.0.0.1, 443, 130.166.38.161, 53626)
         -                              (dest-ip, dest-port, source-ip, source-port)
     - Establish a TLS (transport layer security aka SSL) connection
         - exchange certificates, keys, ciphers, etc.
         - Now the channel is encrypted
     - Send Request
       - send(msg)  where msg = "GET path? ....................."

     - Receive Payload
       - SOF (start of file)   -------------------------------------
       - Response line:        HTTP/1.1 200 Okay
       - Header Info:          Date:
       - More header info\*:   Content-length:
                               Content-type: text/html
                               X-favorite-class: ART 304
       - Blank Line:
       - Body (optional)       the contents of the html file.
       - EOF (end of file)     -------------------------------------


  1. Server-side (http server):
     - Establish a socket
        1. socket(127.0.0.1, 443, 0, 0)();  # Buying the phone
        1. listen(5);  # Phone is read to hear upto 5 someones to call
        1. LOOP
           1. accept();
           1. fork();
     - Read (partially) the HTTP Request
     - Execute input filters
     - Determine the filename of the document
     - Execute the appropiate handler

       - More content Generators
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


