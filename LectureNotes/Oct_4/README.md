# Lecture Notes for October 4, 2021

## Interview Question:
     * Explain what happens when a user types following into their browser:
       - https://www.domain.com/path/to/document?var=value;var=value#section


## Agenda 4th
  1. Last time:
     - Reviewed the process by which a http request is made and serviced
     - Reviewed some of the major components of the a webserver
     - Attempted to build a baby web-server, but we did not get there!

  1. The Short-term Plan:
     - Containerized Webserver
     - 3-Tier Web App

  1. Today:
     - Docker
       1. Methodology for Deploymet
       2. Images and Containers
       3. Recall from CIT160
          * ``docker run --name hello-world hello-world``
          * ``docker build -t cit160 etc``
          * ``docker create --name cit160 --interactive --tty --volume ${PWD}:/mnt/laptop-cit160 cit160``
       4. ``docker build [OPTIONS] PATH | URL | -``
          * CONTEXT=https://github.com/csuntechlab/docker-cgi.examples.git
          * ``docker build $CONTEXT``

       5. Docker File:
          - FROM <imageName>
          - COPY
          - ENV 
          - WORDIR
          - ADD


       6. Composer
           * https://github.com/csuntechlab/calstatepays


