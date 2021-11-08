# Lecture Notes: November 27, 2021


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
     - https://www.csun.edu/application

   ```
   Options +FollowSymLinks -MultiViews -indexes
   RewriteEngine On
   RewriteBase /
   RewriteCond %{REQUEST_FILENAME}.php -f
   RewriteCond %{REQUEST_URI} !/$
   RewriteRule (.*) $1.php [L]
   ```

### More on URLs
   1. The most confusing thing... "/"
   1. RESTful URLS: Representational State Transfer
   1. Clean URLs

   * Example:  The laraval .htaccess file
   ```
   <IfModule mod_rewrite.c>
     RewriteEngine On
 
     # Handle Authorization Header
     RewriteCond %{HTTP:Authorization} .
     RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
 
     # Redirect Trailing Slashes If Not A Folder...
     RewriteCond %{REQUEST_FILENAME} !-d
     RewriteCond %{REQUEST_URI} (.+)/$
     RewriteRule ^ %1 [L,R=301]
 
     # Handle Front Controller...
     RewriteCond %{REQUEST_FILENAME} !-d
     RewriteCond %{REQUEST_FILENAME} !-f
     RewriteRule ^ index.php [L]
   </IfModule>
   ```



### TestString

#### Back References
   1. $n : used by RewriteRule Substitution to reference #n grouping
   1. %n : used by RewriteCond TestString to reference 
      - a grouping in last Rewrite Test String

#### Environment and Server Variables
   1. $var : an environment variable just like in CIT160
   1. %var : an Apache Server variable, akin to environment variables
      - Such variables are NOT necessarily passed to a CGI program
      - Server Internals & Date and Time 
      - Connection & Request information
      - HTTP Header information
      - Special Variables 

### CondPattern:
   1. !: negate the results of the CondPattern
   1. lexigraphical tests:  <,>, <=, >= 
      ``RewriteCond %{HTTP_USER_AGENT} "=This Robot/1.0"``
   1. integer comparisons: -eq, -ge, -gt, etc. 
      ``RewriteCond %{SERVER_PORT} "-eq 8080"``
   1. file attribute tests: -d, -f, etc.
      ```
      RewriteCond /var/www/%{REQUEST_URI} !-f
      RewriteRule ^(.+) /other/archive/$1 [R]
      ```

### Flags:
   - [R=301]  == redirect with 301
   - [R]  == redirect
   - [P]  == proxy 
   - [NC] == no case

   - [L]  == last rule to apply
   - [N]  == rerun all the rules starting at the top 
   - [S=n] == skip the next n rules.
   - [C]   == chained rule

