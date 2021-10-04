# Lab Specification


# Containerized WebSite

## Motivation

In this laboratory assignment, you are to create a web site on your cit384-${USER} VM.  But this web-site will be delivered via a containerized web server.


## Precursory Steps
Complete the following steps to validate that both your local computer and your VM is working correctly. These steps will also help you to re-familize yourself with the common docker commands.

   
   1. Run the docker hello-world example
      ```
      docker run --name inclass hello-world
      ```
   
   1. Copy the CIT160 dockerfile from the sandbox server
      ```
      scp ssh.sandbox.csun.edu:~steve/cit160/dockerfile .
      ```
   
   1. Modify the CIT160 docker file to include the line
      ```
      COPY dockerfile /tmp
      ```
   
   1. Run (Build, Create, Start, and Exec) the command to display the contents of the /tmp/dockerfile 
      ```
      docker build -t bash - < dockerfile
      docker create --name bash --interactive --tty
      docker start bash
      docker exec -it bash cat /tmp/dockerfile
      ```


## Assignment Steps:
   1. Copy your resume and other artifacts into your new repository
   2. Create a dockerfile to be used to create you new website within a container.  This container needs to include:
      - the Apache httpd server
      - your index.html file and other artificates associated with your resume
   3. Add, Commit, and Push your updates to the server

   4. Change your working directory

   5. Run the appropriate docker commands on your desktop to validate everything is working correctly
      ``docker build -t my_resume git@github.com:smf-steve/<blah>.git``
      ``docker run -dit --name resume.site -p 8080:80 my_resume``

   6. Use the curl command to test your website:
      * curl http://localhost:8080/

   7. Using your browser, enter the following URL:
      * http://localhost:8080/

   8. Log into your cit384-${USER}, VM and redo Steps #5 & #6

   9. Ponder how you can use your local browser to access your website on your VM.
      - For inquiring minds, checkout the process to create a tunnel using SSH.
      






## Starter Dockerfile
```
FROM httpd                                      # Obtain a starting image for the Apache Web Server
WORKDIR /usr/local/apache2/htdocs               # Set the working directory to match DocumentRoot
COPY index.html .                               # Copy your index.html file to DocumentRoot directory

# Add in other directives as needed
# LABEL maintainer:"Steven.Fitzgerald@csun.edu"
# RUN
# EXEC
```

## Docker Commands
1. ``docker build -t my_resume git@github.com:smf-steve/<blah>.git``
1.  ``docker run -dit --name resume.site -p 8080:80 my_resume




# Resources:
1. https://docs.docker.com/reference/
2. https://docs.docker.com/engine/reference/builder/
3. https://hub.docker.com/_/httpd
