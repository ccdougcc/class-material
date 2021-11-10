# Lecture Notes: November 3, 2021

## Plan...
  1. Read the Lab specification
  1. Consider what questions you may have
  1. Have a mini-lecture at ~10:00am and ~4:00pm to
     - review the lab specification
     - answer some possible questions
  1. Go work on the lab


## Reading material:
   1. Lab Assignment: https://classroom.github.com/a/Q9SXEtx0
      - https://github.com/CIT384/additional_apache_configs
   1. vhost (``<VirtualHost>``): https://httpd.apache.org/docs/2.4/vhosts/examples.html
   1. htaccess: https://httpd.apache.org/docs/2.4/howto/htaccess.html
      - $ htpasswd
      - .htaccess
         - require valid-user
         - 
   1. Material removed from the lab:
      - https://httpd.apache.org/docs/2.4/howto/reverse_proxy.html

   1. man curl
      - curl -H "Host: site1" http://localhost:8080/
      - vi /etc/hosts
        - 127.0.0.1 site1
        - 127.0.0.1 site2
        - 127.0.0.1 site3
        - then you can do
           - $ curl http://site1:8080/blah