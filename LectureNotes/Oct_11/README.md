# Lecture Notes: for October 6, 2021 


## Comments on Docker-Composer Lab
   1. We were given a new environment for labs, days after the start of the semester
   1. Some testing was performed during the summer, docker-compose was not
   1. There appears to be some nuances in the use of docker-compose within this environment
      - This is typical!
      - IT professionals need to be prepared to triage, to understand, and to fix and to engineer around such things

### Issues encountered and steps to rectify the issue
    1. .env variables were not instantiated via docker-compose
       - database error:  error: access denied and it showed a sql statement
       - logged into sql server, as root
       - did not root access... 
       - internet searches on how to reset the root password
       - logged in.
       - internet searches on how to display the set database: ``show databases``
       - ``show databases``
          - mysql
          - informational ...
          - \<something else\>
          - ${PROJECT_DB_NAME}
       - went into dockerfile, manually updated the Project_DB_NAME  (and the others)
       - removed everything
       - rebuilt everything
       - tested
       - asked a colleague to do the same, and partially waited for their result
       - posted to slack and asked for more forward
         - The feedback I got was: It didn't work for me!
     ---


## Moving Forward

## Apache Architecture
   1. Internal Architecture of Apache 
      - CLI management tools
        - Server: apache2ctl
        - Site: a2ensite a2dissite
        - Configuration: a2enconf a2disconf
        - Module:  a2enmod a2dismod 
        - Inquiry: a2query (?)
      - Server: File System Layout: /etc/apache2
        - http2.conf        ports.conf 
        - envvars           magic
        - mods-available/   mods-enabled/
        - conf-available/   conf-enabled/
        - sites-available/  sites-enabled/ 
      - Modules 
      - Configurations
      - Sites
   1. Modules
      - core module with a growing set of features
      - Types of additional modules
        - Configuration Management
        - File Management
        - Logging Management
        - Module Management
        - Network Management
        - Server Management
      - you too can create a new module and add it to the system

   1. Configurations
      - common packages that can be incorporated into a site.

   1. Sites (vhosts)
      - named based:     \<VirturalHost cit384-steve:80\>   ..stuff..  \</VirtualHost\>
      - ip based:        \<VirturalHost 130.166.2.32:443\>
      - wildcard based:  \<VirturalHost \*:443\>  \<VirturalHost \*:\*\> 
      * SSL Issues

         ```
         GET /uri/path/to/the/index.html HTTP/1.1
         host: cit384-steve

         ```
         1. make socket connection between the client and the server
         2. establish TLS/SSL (if appropriate): when the scheme is https
         3. send/received the request
         4. check the IP address, the IP port, and the host attribute
         5. select the correct vhost

## URL --> FileSystem Mapping
   * scheme: // authority:password@ hostname /path/to/file/to/execute.php/extra/path/stuff  ?args&args  #fragment
   * location: /path/to/file/to/execute.php

   1. DocumentRoot
   1. Alias
   1. Proxy (for Reverse Proxy-ing)
   1. Redirect
   1. Rewrite
   1. ScriptAlias
   1. UserDir public_html:   ~steve/public_html
   1. DirectoryIndex
   ---
   1. ErrorDocument


## Sections (context):
   1. Server
   1. VirtualHost: (host:port)
   1. Directory:
      - Proxy: URL
      - Location: URI
      - Directory: PATH/
      - File: PATH
   1. .htaccess

## Lab for today
   1. Reexamine your containerized-website lab
   1. Modify your configuration to include the UserDir and DirectoryIndex
   1. Modify your resume-site container (via the dockerfile) to
      1. Add yourself as a user -- driven via the $USER environment value
      1. Copy your resume site to the correct location in the container


### Resources of note:
    1. Modules:     https://httpd.apache.org/docs/current/mod/
    1. URL Mapping: https://httpd.apache.org/docs/2.4/urlmapping.html
    1. Sections:    https://httpd.apache.org/docs/2.4/sections.html

