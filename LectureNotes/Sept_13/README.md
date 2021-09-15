# Lecture Notes for September 13 & 15, 2021

## Agenda 13th
  1. HTTP Comm Flow:
     - Setting Stage
     - Apache http://http.apache.org
     - Open source:  
       - Software in which you can review, maybe contribute to
       - A large set of possible licenses apply that gover the use/reuse of the software
  1. Review of Process
     - Daemon:  a background process
     - Components of a Process
       - Standard Files: stdin (0), stdout (1), stderr (2), 
         - remapped:  1: access.log, 2: error.log
       - Environment: Variables and Values stored within a memory structure
       - File Types:
         - regular (-)
         - symbolic links (aka shortcuts) (l)
         - directories (d)
         - pipe (p)
         - socket (s)
         - block (b)
         - char (c)

  1. HTTP Communication  (Slides form CIT160)
       - Socket:   (regular, directories, )
  1. CGI: Common Gateway Interface


## Agenda 15th
  1. Review current status of the project
     - bash automation script to test
  1. Pickup where we left off on Monday
     - Morning: Finished the slides of the CIT160 review, CGI
     - Afternoon:
  1. Client-side Activities:
     - browser, curl, socket
  1. CGI: Common Gateway Interface
     - protocol for interprocess communication
     * Parent process 
        - forks a child
        - wire input and output to/from the parent
        - create an environment for the child with a set of "predefined" value
        - writes the body to the child's input
        - read from the child output
        - add header information
        - send back to client
     * Child child
        - examines its environment
        - read from stdin
        - executes it code
        - send output to stdout
           - header info
           - blank line
           - body (options)
        - exit




## Lab Section:
  1. Recall this lab is due: Sep ~14~ 17, 2021, 14:00 PDT
  1. Review outstanding questions
  1. Ensure everyone has a group
  1. Work on the lab


## Foreshadow for Wednesday
  1. Highlevel Anatomy of a Webserver
  1. Backend Modules 
