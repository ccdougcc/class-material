# Lecture Notes: Oct 18, 2021

## Discussion on the role of IT individuals
  - Jack of all trades
  - Expected to figure it out!

## Consider the following problems:
  1. You were hired by a startup company -- We need a web presence now!
  1. What's a tilde..  I want a professional name!
  1. We just hired a marking team!  They want control of the web server!
  1. The company was bought out. New owners want to rebrand the website now!




## The problem:
  1. Remapping the Web URL to a physical file location
     - DocumentRoot 
     - UserDir disable root
     - UserDir /www/users/*      <- http://www.acme.org/~steve/foobar
                                    ``acme.org:/www/users/~steve/foobar``
     - UserDir public_html      <- http://www.acme.org/~steve/foobar
                                    ``acme.org:/www/users/~steve/public_html/foobar``


## Trees, Trees, Trees, and more Trees

# Rewriting the URLs provided by the user

## The simple
  1. DocumentRoot
  1. UserDir
  1. Alias
  1. Redirect


# Alias
  1. Alias URI file-path
     - ``Alias /student/helpdesk  ~student-helpdesk``
     - ``Alias /courses/cit384    /var/www/classes/fall-2022/WebHosting``
  1. ScriptAlias URI full-path
     - ``ScriptAlias /cgi-bin/    /users/web/cgi-programs/``
  1. Redirect [code] URI URL
     - ``Redirect /~lsmith/cit384 https://www.csun.edu/~steve/cit384``
     - ``Redirect 301 /~lsmith/cit384 https://www.csun.edu/~steve/cit384``
     - ``Redirect 302 /~lsmith/cit384 https://www.csun.edu/~steve/cit384``
     - ``Redirect 303 /~lsmith/cit384 https://www.csun.edu/~steve/cit384``

  1. ``RedirectPermanent /~lsmith/cit384 https://www.csun.edu/~steve/cit384``
  1. ``RedirectTemporary /~lsmith/cit384 https://www.csun.edu/~steve/cit384``



## More Complex: Intro into Regular Expressions
  1. AliasMatch  URI-RegExpr substitution
  1. ScriptMatch URI-RegExpr substitution
  1. RedirectMatch URI-ReExpr URL
  1. Rewrite URI-RegExpr substitution flags




## Simple Regular Expression 
  1. Metacharacters
     - $ : end of the line
     - ^ : beginning of the line, not these characters
     - * : zero or more
     - + : one or more
     - | : either this or that
     - () : group things
     - .  : any character what so ever, except \n
     - [] : character classes
     - [ - ] : range operation
     - [^ ] : not operater
     - {n,m} : repetition: at least "n" but nomore the "m"
  1. Types of RegExpression: Different forms of syntax
     - shell: (baby RE)  ``ls a*b``
     - theoretical regular expressions
     - posix regular expression  <---
     - perl regular expression

# Regular Expression Example
  - Social Security number:   ...-..-.... ; [0-9]{2}-[0-9]{2}-[0-9]{4}
  - Credit Card:    .... .... .... .... 
  - number: [-^0-9]

# AliasMatch
  - AliasMatch "/image/" "/ftp/pub/image/"
    - input URI:  ``/~steve/image/picture.gif ``
    - output ?:  /~steve/ftp/pub/image/picture.gif
  - AliasMatch "^/image/" "/ftp/pub/image/"
    - input URI:  ``/~steve/image/picture.gif ``
    - output ?:  No match 
  - AliasMatch "^/image/" "/ftp/pub/image/"
    - input URI:  ``/image/promo/picture.gif ``
    - output ?:  /ftp/pub/image/promo/picture.gif

# AliasMatch with variable substitition
  - ``AliasMatch "^/image/(.*)$" "/ftp/pub/image/$1"``
    - example 1:
      - input:  /image/(this/is/the/directory/for/the/image)
      - output: /ftp/pub/images/this/is/the/directory/for/the/image
# AliasMatch with two variable subsitition
  - ``AliasMatch "^/image/(.*)\.(jpg|gif)$" "/files/$2.images/$1.jpg"``
     - input:   /image/(filename).(jpg)
     - output:  /files/jpg.images/filename.jpg


# AliasMatch  "^/forms/hr/absence-report.pdf$""  /sites/default/files/Absence%20Report%20PA-635F.pdf
# AliasMatch  "^forms/PA-634F/" /sites/default/files/Absence%20Report%20PA-634F.pdf



# The Rewrite Engine (foreshadow)
  1. RewriteEngine On
  1. RewriteCond 
  1. Rewrite pattern substitution flag
     - flag
      - [R=301]  == redirect with 301
      - [R]  == redirect
      - [L]  == last rule to apply
      - [NC] == no case
      - [P] == proxy 


## Consider the following Lab Assignment
  1. Build a splash page for your company
     - Come up with a company name and a simple product
     - Build a simple web page for this company
     - Install this web page at the DocumentRoot location of your web server
  1. Build a simple company directory
     - Come up with 5 fictious sales individuals for your company
     - Create 5 user accounts associated with each contact
       - each sales person wants to manage their own account
     - Create a simple splash page for each contact
       - but they are to busy right now selling product 
       - VP of Sales delegates the intial creation of these pages to you
     - Create Alias directives for each of these contacts
  1. Delegate a portion of the WebSpace to the Marketing team
     - Marketing takes control of "/" and "/promotions"  
     - Sales/Marketing wants all the marketing material to be standardized
     - Marketing wants to the IT time to manage the said collaterial
       - Create an Alias to reposition the DocumentRoot, 
       - Create an infinite set of Alias for all the collaterial
  1. Well go do it, you should now what to do!
     - update the company web page with the new company name
     - force a redirect to the new company name 



# Blackboard
## Trees, Trees, Trees

# Rewriting the URLs provided by the user

## The simple
  1. UserDir
  1. Alias
  1. ScriptAlias
  1. Redirect
  1. RedirectPermanent
  1. RedirectTemp

## More Complex: Intro into Regular Expressions
    1. AliasMatch
  1. ScriptMatch
  1. RedirectMatch
  1. Rewrite






