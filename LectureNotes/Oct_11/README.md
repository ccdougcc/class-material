# Lecture Notes: for October 6, 2021 


## Comments on Docker-Composer Lab
   1. We were given a new environment for labs, days after the start of the semester
   1. Some testing was performed during the summer, docker-compose was not
   1. There appears to be some nuances in the use of docker-compose within this environment
      - This is typical!
      - IT professionals need to be prepared to triage, to understand, and to fix and to engineer around such things

### Issues encountered and steps to rectify the issue
    1. 


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
      - named based:     \<VituralHost cit384-steve:80\>
      - ip based:        \<VituralHost 130.166.2.32:443\>
      - wildcard based:  \<VituralHost 130.166.2.32:443\>

## URL --> FileSystem Mapping
   1. DocumentRoot
   1. DirectoryIndex
   1. Alias
   1. Proxy (for Reverse Proxy-ing)
   1. Redirect
   1. Rewrite
   1. ScriptAlias
   1. UserDir
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
   1. Reexamine your last lab
   1. Modify your configuration to include the UserDir and DirectoryIndex
   1. Modify your resume-site container (via the dockerfile) to
      1. Add yourself as a user -- driven via the $USER environment value
      1. Copy your resume site to the correct location in the container


### Resources of note:
    1. Modules:     https://httpd.apache.org/docs/current/mod/
    1. URL Mapping: https://httpd.apache.org/docs/2.4/urlmapping.html
    1. Sections:    https://httpd.apache.org/docs/2.4/sections.html

