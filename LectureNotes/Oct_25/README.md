# Lecture October 25, 2021

## Notes:
   - (A) Cleanup on Limit and Auth for .htaccess
   - (M) Cleanup on Conditional Includes

## Questions:
   - (A) General progress on the lab?

## Last time:
   - Regular Expressions
     - globbing 
     - basic reg-expr (obsolete)
     - extended reg-expr
     - perl 
   - Greedy / Nongreedy
      - If greedy, and if you want to be polite, then ask
        - that is append the notation with a "?"
      - If polite, and if you want to be greed, then grab _more_
        - that is append the notation with a "+"
   - Syntax Sugar 
     - choice:  ( a | b | c ) -> [abc]
     - repetition: aa* == a+ ->  (reg_expr){lower_limit, upper_limit}
       - a* == a{0,}

   - Directives
     - ``<FilesMatch perl-regex>``
     - ``<AliasMatch perl-regex>``
     - ``<Directory globbing>``

## New Material: htaccess file

### Example: Request processed by the Sever
   - curl https://www.csun.edu/~steve/file/name.html
     - create a socket connection
     - TLS handshake
     - use the wire protocol
       ```
       GET /~steve/file/name.html
       host: www.csun.edu
       Accept: plain/xhtml 
       
       ```

### Server Configuration      
   - .htaccess:  User Level Configuration 
     - more on this later...

   - Server configuration via a set of files
     - ``Include /usr/local/apache2/conf/ssl.conf``
     - ``Include /usr/local/apache2/conf/vhosts/*.conf``

     - Conditional Include (upon system restart)
        ```
        <If "command"> <Else> <Elseif> </If>  : tests on any condition
        <IfDefine> : test on an Environment Variable ($) or Apache Variable (%)
        <IfDirective> : test base upon an Apache directive
        <IfFile> : upon startup, does this file (!) exist
        <IfModule>:
        <IfSection>: 
           <IfSection VirtualHost>
           </IfSection>       
        ```
  
   - Configuration Context: Server, VHost, Location, Directory, .htaccess
     - server level:
       - Listen 8080
     - Virtual Host
       - named and ip-based virtual host
       - examples
       ```
       UserDir public_html 
       <virtualhost *:80>
         DocumentRoot /dev/null
         Redirect permanent https://www.csun.edu/
       </virtualhost>
       <virtualhost *:443>
         DocumentRoot /www/ssh
         UserDir private_html 
       </virtualhost>
       <virtualhost  *:*>
          ServerName  www.csun.edu 
          ServerAlias www
          ServerAdmin root@csun.edu 
       </virtualhost>
       ```
     - Location
       ```<Location "/promotions" >
            Alias /promotions /usr/home/anthony/public_html
            directive2
          </Location>
      ```
     - Directory, and
       ```
          <Directory "/user/home/steve/public_html/cit384.2/" >
             DirectoryIndex cit384.1.html
             directive2
             <Files "*.txt" >
               SetHandler  blah
             </Files>
         </Directory>
      ```

### .htaccess
   * https://httpd.apache.org/docs/2.4/howto/htaccess.html
   - directory location:  /home/users/steve/public_html/file/path/to/my/program/and/options
   - looks for a file called .htaccess where
     - /home/users/steve/public_html/file/path/to/my/program/and/options  << file exists
     - /home/users/steve/public_html/file/path/to/my/program/and
     - /home/users/steve/public_html/file/path/to/my/program << file exists
     - /home/users/steve/public_html/file/path/to/my/
     - and so on.... 
   - server Directives
     - AccessFileName .htaccess
     - AllowOverride: All, None, Directive_list 
       - All-- except "MultiViews"
       - AuthConfig (user/group)
       - Limit (ip/domain)
       - FileInfo  (Handlers & Filter Directives )
       - Indexes  (DirectoryIndex, plus others)
       - Options

   - Options:
      - MultiViews: negotations
      - All (but not MultiViews)
      - ExecCGI 
      - Includes (.shtml)
      - IncludesNOEXEC
      - FollowSymLink
      - FollowSymLinkIfOwnerMatch
      - Indexes


  - .htaccess contents
      - 
        ```
        <Limit>
          Require valid-user
        </Limit>
        ```
        - IP address and/or domain
        - user
        - require group "groupname"
        - Order Allow, Deny
        - Order Deny, Allow

   1. Auth  (Authn, Authz)
      - AuthType Basic
      - AuthName "Enter your csun.edu credentials "
      - AuthUserFile /home/users0/ccs/steve/private_html/roster/.htpasswd
      - Require valid-user
      - ``htpasswd -c Filename username``

