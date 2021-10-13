# Lecture Notes for September 27, 2021

## Interview Question:
  * Explain what happens when a user types following into their browser:
    - https://www.domain.com/path/to/document?var=value;var=value#section


## Agenda 29th
  1. Quick from the class
     - (M) Content-generator for .x-html, more clarification
       - do we need to modify the headers --- yes, potentially
       - do we need to modify the body -- yes, potentially.
     - (A) How does send-as-is and plain-html fit into the overall architecture?



  1. Last time:
     - A re-re-re-review of the entire process -- going deeper each time.
     - A focus on different types of Content Generators
     - Walked through the code for send-as-is and plain-html
     - Discussed the creation of (or wrote code in class of) a new Content Generator
     - The specification of the new Content Generator:
       - File extention: .x-html
       - MIME type: application/x-html
       - The HTTP response body:
         - has been compressed
         - has been base64 encoded

  1. Today:
     - Based upon questions form the class, generate a lecture on the fly
     - Note that this new Content Generator is more applicable as a Output Filter
     - Discuss:
       1. Client side processing
       1. Browser Plugins
       1. cit384-url

  1. Lab Assignment to be assigned today:
     - Create the .x-html Content Generator
     - Create the cit384-url client side CLI tool
       - the following steps are performed in the tool
         * parse the URL provided on the command line -- leave this for later
           - Usage: cit384-url  hostname port URI
         * make a call to DNS to get the IP address 
         * use the socket command to make a connection to the server
         * send a HTTP request
         * read the HTTP response
         * If it detects Content-type: applicaton/x-html
             - decode the body
             - uncompress the un-decoded body

  1. Testing Harness.
     - build simple server side tool that generate an x-html file 
     - socket -s ${PORT} -f -q -l -p 'cat my.x-html'
       -   -s: a server-side socket is created on ${PORT}
       -   -f: fork a child process for each connection
       -   -q: quit: The connection is closed when an end-of-file condition occurs on stdin
       -   -l: loop to receive the next network connection
       -   -p: execute the supporting program: 'cat my.x-html'


  1. The structure of you cit384-url program
     - Parser the URL: https://www.domain.com/path/to/document?var=value;var=value#section
       * protocol: https
       * userinfo: anonymous (implicit)
       * server_name: www.domain.com
       * TCP port: 443 (implicit: defined by the protocol)
       * path: /path/to/document
       * query_string: var=value;var=value  
       * fragment: section
       * But let's simplify this part to work on the other stuff (see above)

     - Build the Request Payload
       - SOF (start of file)   -------------------------------------
       - Request line:         GET path?query_string HTTP/1.1
       - Header Info:          host: server_name
       - More header info\*:   X-anything:  value
                               
       - Blank Line:
       - Body (optional)       //html code that is a total of 453 bytes
       - EOF (end of file)     -------------------------------------

     - Establish a Socket 
       - DNS lookup on www.domain.com: 127.0.0.1
       - socket 127.0.0.1 443

     - Send Request
       - send(msg)  where msg = "GET path? ....................."

     - Receive Payload
       - SOF (start of file)   -------------------------------------
       - Response line:        HTTP/1.1 200 Okay
       - Header Info:          Date:
       - More header info\*:   Content-length:
                               Content-type: application/x-html
       - Blank Line:
       - Body (optional)       H52QQ964oVNm4BwQdNCEoQNCoZ0yIMSUKQhizJs2cOSUmTOnDBkQYdx8FBOmow0aIApaJONRAQ==
       - EOF (end of file)     -------------------------------------

     
      - Based upon Content-type: do something: in this case
        - $ echo -n "H52QQ964oVNm4BwQdNCEoQNCoZ0yIMSUKQhizJs2cOSUmTOnDBkQYdx8FBOmow0aIApaJONRAQ==" | \
          base64 -d  | uncompress -


