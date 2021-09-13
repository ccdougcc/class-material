# Lecture Notes for September 13, 2021

## Agenda
  1. HTTP Comm Flow:
     - Setting Stage
     - Apache
     - Open source
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
  1. Highlevel Anatomy of a Webserver
  1. Backend Modules 
