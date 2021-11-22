# Lecture Notes for November 22, 2021

## Agenda
  1. Review of SSL material from November 17
  1. Introduction of the New Lab
     - https://github.com/CIT384/apache_ssl_configs
     - https://classroom.github.com/a/PKleOEuG
     - Due Date:  Monday 29th
  1. Tasks
     * Certificates
       - create a CSR for your website using openSSL
       - sign the CSR to create a self-signed certificate
     * Install the necessary Certificate information into your github repo
       - ponder the security implications of such an approach
     * Create a new index.html (or repurpose one)
     * Create a dockerfile to
       - build an apache2 system with all the necessary packages/modules
       - enable the appropriate modules
       - include a vhost definition 
         * for both http and https on the established well-known ports
         * ensure all http traffic is redirected to https
    * Install the Certificate information to the appropriate location

  1. Enhancements
    - Examine the various Ciphers and strength you security Stance
    - Trigger which index.html page gets render based upon the SSLProtocol
    - Use a .htaccess file to force the HTTPS requirement (in addition to)
    - Build a process by which you can after-the-fact install the SSL certs.
      * docker compose, installs the webserver from point A, and then instalss the certs from point B
      * run a probram within the web server to pull the cert from somewhere
      * run a program against the web server to push the cert into the server
    - Codify the above to run each and every year
      * an automatic CSR generation...



# Next On the Agenda  (the three A's of security)
  1. Authentication
  1. Authorization
  1. The third -- Access, Auditing, Accounting, and A..


# Review Information (I.e., notes from the last lecture)
  1. Server Certificate 
     - purpose
     - examine from a browser
     - examine via CLI: openssl s_client -connect 130.166.238.195:443

  1. Apache mod_ssl: https://httpd.apache.org/docs/2.4/mod/mod_ssl.html
     - Server | VHOST Directives
       * SSLEngine on | off
       * SetEnv HTTPS on | off
       * SSLProtocol [+|-] protocol ...  # SSLProtocol TLSv1.2 -TLSv1.1 
       * SSLCACertificateFile \<path>
       * SSLCertificateFile \<path>
       * SSLCertificateKeyFile \<path>
       * SSLProxyEngine on | off
       * SSLCompression  on | off    
         - CRIME Attack: (Compression Ratio Info-leak Made Easy)
         - Upgrade server or turn off compression 

     - Other Directives (including the .htaccess context)
       * SSLRequireSSL
       * SSLVerifyClient none | optional | require | optional_no_ca
       * SSLVerifyDepth \<num>
       * SSLCipherSuite
       * SSLUserName \<env>  # example env: SSL_Client_S_DN_CN

     - Example SSLUserName
       - ``http://steve:83645kzsyd@www.csun.edu:443/~steve/index.html``
          - username?:  steve
       - ``https://www.csun.edu:443/~steve/index.html``
          - SSLVerifyClient require
          - server_cert subject_name: /C=US/postalCode=91330/ST=California/L=Northridge/street=18111 Nordhoff Street/O=California State University, Northridge/ OU=Information Technology/CN=csun.edu
          - client_cert subject_name: /C=US/O=CSUN/ou=COMP_SCI/CN=steve
          - SSLUserName SSL_Client_S_DN_CN


  1. Encoding, Compression, and Encryption
     - slides: https://docs.google.com/presentation/d/1_ROtLBf3DaWY9QPbqN0AiVLb7fyD5ft7e058brWJZtU/edit#slide=id.gd376dfe63e_1_13

     - Server Authentication 
       - Server listens on port X
         * client establish a socket connect to X
         * client starts TLS negation
         * client requests Server's certificate
       - Server sends it certificate
         * client validated the CA (I trust the Certificate)
         * client extracted the public_key
         * client creates a challenge request
           - encrypt a message using the server's public_key
           - sends to the server
       - Server receive the challenge
          - decrypted the message using the server's private_key
          - determines the response
             - encrypts the response using the server's private_key
             - sends that to the client
          * client decrypts the response using the server's public_key 
      - IF ALL IS GOOD, then the server has been authenticated
     - if SSLVerifyClient == require then .... Client Authentication
       - server requests the client's certificate
         * client sends certificate
       - server validates the certificate (do I trust the CA)  # Note "optional_no_ca"
       - server extracts the clients public_key
       - server posses question that is encrypt with the client's public_key
         * client decrypts the question with its private key
         * client sends back the answer
       - server validates the answer
       - IF ALL is GOOD, then the client has been authenticated
       - server sets Username to be whatever the SSLUserName is set to..
    - a Session key is establish and used by both the client and the server
    - Now I can encrypt information using the set of cipher

  1. Apache: Network-level encryption
     - Server-Side Certificates
       ```
       LoadModule ssl_module modules/mod_ssl.so

       Listen 443
       <VirtualHost *:443>
         ServerName www.sandbox.csun.edu
         SSLEngine on
         SSLCertificateFile "/path/to/www.example.com.cert"
         SSLCertificateKeyFile "/path/to/www.example.com.key"
         SSLProxyEngine off
       </VirtualHost>

       <VirtualHost ssh.sandbox.csun.edu:8443>
         ServerName ssh.sandbox.csun.edu
         SetEnv HTTPS on 
       </VirtualHost>
       ```

      - Client-Side Certificates
        ```
        SSLProtocol all
        SSLVerifyClient none
        SSLCACertificateFile "conf/ssl.crt/ca.crt"

        <Location "/marketing/secure">
          SSLProcotol TLS1.3
          SSLVerifyClient require
          SSLVerifyDepth 1
        </Location>
        ```

   1. Files Overview
      - CA Certificate (Certificate Authority)
      - Certificate
      - Key
      - CSR (Certificate Request)

   1. OpenSSL Certificate Generation
      - https://certbot.eff.org ?
      - Create CSR: 
        * openssl req -new -newkey rsa:2048 -nodes -keyout key_file
      - Store key_file and CSR file
      - Submit CSR to a CA, e.g., Internet2
      - Receive CSR
      - perform some type of validation
      - sign the CSR --> CERT
      - send the CERT back to me
      - Install CERT

