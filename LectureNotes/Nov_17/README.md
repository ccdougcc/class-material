
# Lecture Notes for November 17, 2021

## Agenda
  1. Server Certificate 
     - purpose
     - examine from a browser
     - examine via CLI: openssl s_client -connect 130.166.238.195:443

  1. Apache mod_ssl: https://httpd.apache.org/docs/2.4/mod/mod_ssl.html
     - Server | VHOST Directives
       * SSLEngine on | off
       * SetEnvOn HTTPS on | off
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
          - server_cert subject_name: /C=US/postalCode=91330/ST=California/L=Northridge/ street=18111 Nordhoff Street/O=California State University, Northridge/ OU=Information Technology/CN=csun.edu
          - client_cert subject_name: /C=US/O=CSUN/ou=COMP_SCI/CN=steve
          - SSLUserName SSL_Client_S_DN_CN


  1. Encoding, Compression, and Encryption
     - slides: https://docs.google.com/presentation/d/1_ROtLBf3DaWY9QPbqN0AiVLb7fyD5ft7e058brWJZtU/edit#slide=id.gd376dfe63e_1_13

     - SSL Connnection: Server Authentication
       - client makes a socket connnection to the Server
       - client says send me your certificate
         * server sendes certificate
       - client validates certificate (do I trust the CA?)
       - client extracts the server's public key
       - client poses question that is encrypted with the public key
         * server decryptes the question with it's private key
         * server sends back the answer
       - client validates the answer
       - IF ALL IS GOOD, then the server has been authenticated
     - if SSLVerifyClient == require then .... Client Authentication
       - server requests the client's certificate
         * client sends certificate
       - server validates the certicate (do I trust the CA)  # Note "optional_no_ca"
       - server extracts the clients public_key
       - server posses question that is encrypt with the public_key
         * client decrypts the question with its private key
         * client sends back the answer
       - server validartes the answer
       - server sets Username to be whatever the SSLUserName is set to..


  
  1. Apache: Network-level encryption
     - Server-Side Certificates
       ```
       LoadModule ssl_module modules/mod_ssl.so

       Listen 443
       <VirtualHost *:443>
         ServerName www.example.com
         SSLEngine on
         SSLCertificateFile "/path/to/www.example.com.cert"
         SSLCertificateKeyFile "/path/to/www.example.com.key"
       </VirtualHost>
       ```

      - Client-Side Certificates
        ```
        SSLProtocol all
        SSLVerifyClient none
        SSLCACertificateFile "conf/ssl.crt/ca.crt"

        <Location "/marketing/secure">
          SSLProcotol TSL1.3
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
      - Create CSR: 
        * openssl req -new -newkey rsa:2048 -nodes -keyout key_file
      - Store key_file and CSR file
      - Submit CSR to a CA, e.g., Internet2
      - Receive CSR
      - perform soome type of valadation
      - sign the CSR --> CERT
      - send the CERT back to me
      - Install CERT

