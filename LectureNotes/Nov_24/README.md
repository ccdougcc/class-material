# Lecture Notes for November 24, 2021

## Topic for the day: Authentication, Authorization 
## Agenda
  1. Review of
     1. /etc/passwd and /etc/group
     1. unix file permissions
        - chmod ugo+rwx file-name
        - chown steve file-name
        - chgrp fac file-name
     1. Review of URL with username-password
        - ``http://steve:83645kzsyd@www.csun.edu:443/~john/index.html``
        - UserName := steve
     1. Certificate-Based Client Authentication
        - SSLVerifyClient require
        - SSLUserName SSL_CLIENT_S_DN_CN
          - DN: /C=US/O=CSUN/OU=Comp Sci/CN=steve
          - DN: cn=steve, ou=comp sci, o=csun, c=us
          - SSL_CLIENT_S_DN_CN == "steve" -->  UserName := steve

  1. Elementary Authentication (authn) and Authorization (authz) in Apache
     1. Require Directive (core)
        - Require ip | host
        - Require user userid [userid ...]
        - Require valid-user
        - Require group groupid [groupid ...]

     1. AuthType Directive

     1. Programs to create authentication files
        - htpasswd -c .htpasswd steve
        - htdigest -c .htdigest "Enter Password" steve
        - htdbm -T DB -c .htdbm steve   # (SDBM|GDBM|DB|default).





  
  1. Apache Modules (auth_core, and usually at least one from each group) 
     1. Authentication Type  (AuthType)
        - Basic: auth_basic
        - Digest: auth_digest
        - Form: auth_core
     1. Authentication Provider (AuthBasicProvider, AuthDigestProvider)
        - file: (authn_file)
        - dbd: (authn_dbd) # DataBase Driver, aka SQL
        - dbm: (authn_dbm) # Berkeley DB
        - anon: (authn_anon)
        - ldap: (authnz_ldap)
     1. Authorization (Require)
        - host:  (authz_host)
        - user:  (authz_user)
        - groupfile: (authz_groupfile)
        ---
        - owner: (authz_owner)
          * Require file-owner
          * Require file-group
        - dbm:   (authz_dbm)  
          * Require dbd_group groupid
        - dbd:   (authz_dbd)
          * Require dbd-group groupid
          * AuthzDBDQuery "SELECT group FROM authz WHERE user = %s"
        - ldap:  (authnz_ldap)

   1. URL Examples:
      1. HTTP-Request Payload (from ssh.sandbox.csun.edu: socket -s -l 3434)
         1. ``curl http://steve:hello@localhost:3434/``
         1. ``curl --basic --user steve:hello http://localhost:3434/``
         1. ``curl --digest --user steve:hello http://localhost:3434/``
      1. curl requests (from ssh.sandbox.csun.edu:)
         1. ``curl --head http://localhost:8443/~steve/auth-basic/``
         1. ``curl -I http://steve:hello@localhost:8443/~steve/auth-basic/``
         1. ``curl -I http://steve:hello@localhost:8443/~steve/auth-digest/``
         1. ``curl -I --basic --user steve:hello \
                 http://localhost:8443/~steve/auth-basic/``
         1. ``curl -I --digest --user steve:hello \
                 http://localhost:8443/~steve/auth-digest``
      1. ldap-request
         1. ``curl -I http://steve:hello@localhost:8443/~steve/auth-ldap``

   1. .htaccess files
      1. ``ssh.sandbox.csun.edu:~steve/public_html/auth-basic/.htaccess``
      1. ``ssh.sandbox.csun.edu:~steve/public_html/auth-digest/.htaccess``
      1. ``ssh.sandbox.csun.edu:~steve/public_html/auth-ldap/.htaccess``

 



