# Lecture Notes: November 8, 2021


## Questions:
   - (M)
   - (A)

## Today: More on .htaccess and Rewrite Rules
  1. .htaccess is provided to allow users to have greater control over their web applications
  1. Rewrite Rules are provided to allow users to modify the external URL presentation from the file system constraints.
  1. Rewrite Rules are provided to ...
   - you name it, you can pretty much to do it.


### Directives Under Discussion
   * https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html
   1. RewriteRule Pattern Substitution [flags]
   1. RewriteCond TestString CondPattern [flags]
   1. RewriteEngine on|off
   1. RewriteBase URL-path

### Examples: Simple Rewrite Rules within .htaccess
   1. I don't like to expose the name of the .php file
     - https://www.csun.edu/application.php
       - I don't like it, so change it to:
     - https://www.csun.edu/application

       ```
       Options +FollowSymLinks -MultiViews -indexes
       RewriteEngine On
       RewriteBase /
    
       RewriteCond %{REQUEST_FILENAME}.php -f
       RewriteCond %{REQUEST_URI} !/$
       RewriteRule (.*) $1.php  [L]

       ```
     - %{REQUEST_URI}  == /application
     - %{REQUEST_FILENAME} == /var/www/application
     - Desired %{REQUEST_FILENAME} == /var/www/application.php


    - https://www.csun.edu/
      REQUEST_URI= "/"
      ```
      RewriteEngine On
      RewriteRule (.*) $1.php  [L]
      ```
      - then $1 is defined to be  "www.csun.edu", ""
      - then the %{REQUEST_FILENAME} == /.php


### More on URLs
   1. The most confusing thing... "/"
   1. Clean URLs
      - Not Clean: https://www.youtube.com/index.phpv=5AOTcTgOz89
   1. RESTful URLS: Representational State Transfer
     * represent the URL only as slugs
     * have pairs of names / values (collections/instance)
     - https://www.csun.edu/~steve/application.php?classes=cit384,sessions=930
     - https://www.csun.edu/~steve/application.php/classes=cit384/sessions=930  (no query string)
     - https://www.csun.edu/~steve/application.php/classes/cit384/sessions/930  (pairs of values, not equiv)

     * Extending the process
       - https://www.csun.edu/~steve/application/classes/cit384/sessions/930/students/45/assignements/lab1






   * Example:  The laraval .htaccess file
   ```
   <IfModule mod_rewrite.c>
     RewriteEngine On
 
     # Handle Authorization Header
     RewriteCond %{HTTP:Authorization} .
     RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
 
     # Redirect Trailing Slashes If Not A Folder...
     RewriteCond %{REQUEST_FILENAME} !-d
     RewriteCond %{REQUEST_URI} (.*)/$
     RewriteRule ^ %1 [L,R=301]
 
     # Handle Front Controller...
     RewriteCond %{REQUEST_FILENAME} !-d
     RewriteCond %{REQUEST_FILENAME} !-f
     RewriteRule ^ index.php [L]
   </IfModule>
   ```
    - https://www.csun.edu/~steve/application/classes/cit384/sessions/930/students/45/assignements/lab1
      - REQUEST_FILENAME: /home/user/steve/public_html/application /classes/cit384/sessions/930/students/45/assignements/lab1
      - Application is located @: /home/user/steve/public_html/application/index.php

    - Example with roster:
      -  https://www.csun.edu/~steve/roster/css/
         - REQUEST_FILE == /home/users/steve/public_html/roster/css/
           1. check if there is a /home/users/steve/public_html/roster/css/.htaccess, NO!
           1. check if there is a /home/users/steve/public_html/roster/.htaccess,  YES!
           - The Final REQUEST_FILE is: /home/users/steve/public_html/roster/css/

      -  https://www.csun.edu/~steve/roster/stuff/that/does/not/exist
         - REQUEST_FILE == /home/users/steve/roster/stuff/that/does/not/exist
           1. check if there is a /home/users/steve/public_html/roster/stuff/that/does/not/exist/.htaccess, NO!
           1. check if there is a /home/users/steve/public_html/roster/stuff/that/does/not/.htaccess, NO!
           1. ...
           1. check if there is a /home/users/steve/public_html/roster/.htaccess, YES!
           ? What is the current URI: ``/~steve/roster`` 
           1. Apply
           ```
             RewriteRule ^ index.php [L]
           ```
           ```
             RewriteRule %{REQUEST_URI}/ %{REQUEST_URI}/index.php [L]
           ```          


### Syntax
   1. RewriteRule Pattern Substitution [flags]
   1. RewriteCond TestString CondPattern [flags]
   1. RewriteEngine on|off
   1. RewriteBase URL-path

#### TestString

##### Back References
   1. $n : used by RewriteRule Substitution to reference #n grouping
   1. %n : used by RewriteCond TestString to reference 
      - a grouping in last Rewrite Test String

##### Environment and Server Variables
   1. $var : an environment variable just like in CIT160
   1. %var : an Apache Server variable, akin to environment variables
      - Such variables are NOT necessarily passed to a CGI program
      - Server Internals & Date and Time 
      - Connection & Request information
      - HTTP Header information
      - Special Variables 

##### CondPattern:
   1. !: negate the results of the CondPattern
   1. lexigraphical tests:  <,>, <=, >= 
      ``RewriteCond %{HTTP_USER_AGENT} "=Mozilla/5.0"``
   1. integer comparisons: -eq, -ge, -gt, etc. 
      ``RewriteCond %{SERVER_PORT} "-eq 80"``
   1. file attribute tests: -d, -f, etc.
      ```
      RewriteCond /var/www/%{REQUEST_URI} !-f
      RewriteRule ^(.+) /other/archive/$1 [R]
      ```

##### Flags:
   - [R=301]  == redirect with 301
   - [R]  == redirect
   - [P]  == proxy 
   - [NC] == no case

   - [L]  == last rule to apply
   - [N]  == rerun all the rules starting at the top 
   - [S=n] == skip the next n rules.
   - [C]   == chained rule


# Problem to think about...
  - write a set of rewrite rules that provides one of two web pages:  "A"llOthers, and "B"ronze
    1. To get the "B" page, you must
       - be coming from an IP address of 130.166/16
       - be using the new browser "Bronze"...
    1. Otherwise you get the "A" page


