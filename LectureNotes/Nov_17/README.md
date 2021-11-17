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

  1. Encoding, Compression, and Encryption
     - slides: https://docs.google.com/presentation/d/1_ROtLBf3DaWY9QPbqN0AiVLb7fyD5ft7e058brWJZtU/edit#slide=id.gd376dfe63e_1_13
  
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
        SSLVerifyClient none
        SSLCACertificateFile "conf/ssl.crt/ca.crt"

        <Location "/secure/area">
          SSLVerifyClient require
          SSLVerifyDepth 1
        </Location>
        ```
   1. OpenSSL Certificate Generation
      - Create CSR: 
        * openssl req -new -newkey rsa:2048 -nodes -keyout key_file
      - Store key_file and CSR file
      - Submit CSR to a CA
      - Receive CERT
      - Install CERT
      
