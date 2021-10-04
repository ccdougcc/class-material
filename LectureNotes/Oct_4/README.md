# Lecture Notes for October 4, 2021

## Interview Question:
     * Explain what happens when a user types following into their browser:
       - https://www.domain.com/path/to/document?var=value;var=value#section


## Agenda 4th
  1. Questions:
     - uid look up was not working on ssh.sandbox.csun.edu
       - devs need to find a work around to copy files
       - ops need to figure out what is wrong and how to fix it
         - root cause of the problem is associated with the LDAP directory -- authentication service

  1. Last time:
     - Reviewed the process by which a http request is made and serviced
     - Reviewed some of the major components of the webserver
     - Attempted to build a baby web-server, but we did not get there!

  1. The Short-term Plan:
     - Containerized Webserver
     - 3-Tier Web App

  1. Today:
     - Interview Questions:
       * Explain what happends when an SRE executes the following command:
         - ``docker run --name inclass hello-world``
     - Docker
       1. Methodology for Deploymet
       2. Images and Containers
          - docker ps: list of all of the active *containers*
          - docker ps -a: list of all of the *containers*
          - docker images:
          - docker rm | rmi: removes an container or a container
          - docker start | stop: starts/stops a container
          - docker run: creates a new container and builds all intermediate images as needed.
            - docker pull: 
            - docker build: build an image
            - docker create: build a container
            - docker start:
            - docker exec:
        

       3. Recall from CIT160
          * ``docker run --name hello-world hello-world``
          * ``docker build -t cit160 etc``
          * ``docker create --name cit160 --interactive --tty --volume ${PWD}:/mnt/laptop-cit160 cit160``

       4. ``docker build [OPTIONS] PATH | URL | -`` < Dockerfile
          * CONTEXT=https://github.com/csuntechlab/docker-cgi.examples.git
          * ``docker build $CONTEXT``
             -  curl http://cit384-steve.csun.edu/

       5. Docker File:
          - ARG VERSION=latest
          - FROM base:${VERSION}
          - LABEL
          - ENV 
          - WORKDIR
          - ADD
          - COPY
          - RUN apt-get update && apt-get install -y  openssh-client
          - ENTRYPOINT | EXEC 


       6. Composer
           * https://github.com/csuntechlab/calstatepays







