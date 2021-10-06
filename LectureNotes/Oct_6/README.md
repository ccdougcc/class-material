# Lecture Notes: for October 6, 2021 

## Quote:
   ```
   “I cannot teach anybody anything. I can only make them think.”
   ― Socrates
   ```

## Questions:
   1. Lab Instructions-- why on the laptop
   1. Difference between local machine and production server

## Problems that arose
   1. WSL and Mac require the following env: export DOCKER_BUILDKIT=0
      - place this in your \~/.profile
   1. Master versus Main branch
      - docker build: presume the primary branch is called master
      - github: recently (\~12 month), change the name of the primary branch from master to main
      - solution: ``docker build git@github.com:<url-path>#<branch-name>``
   1. Capitalization for Dockerfile verses dockerfile 
   1. COPY command in Dockerfile... 
      - if its a directory you need the trailing slash
      - just like a web URL
   1. Knowing the difference between copying (etc) to your laptop verses your container
   1. Use of docker build with stdin, COPY command don't work COPY ./index.html /var/html/index.html
      1. Compare: #1
         - ``docker build - < Dockerfile`` 
         - Current working directory: is unknown
      1. Compare: #2
         - ``docker build . `` : COPY command does work.
         - Current working directory is: .
      1. Compare : #3
         - ``docker build git@github.com:<url-path>`` 
         - Current working directory is: the top-level directory at ``git@github.com:<url-path>``
   1. tunneling to the cit384-${USER}  does not work well
   1. issues with scp on the command
      - ``scp <CSUN-UID>@ssh.sandbox.csun.edu:\~steve/cit160/etc/dockerfile dockerfile``
   1. https (i.e., TLS) ... not mandatory at this time ...
   1. Got to read the spec for details

## Docker Compose
   1. What does it do?
      - allows you to spin-up multiple containers with associated networking and volumes in one configuration/automation process
      - built on top of docker
        - config file for docker-composer is simpler (Steve's opinion. )


   1. What's the big deal?


   1. Example
      1. https://calstatepays.org
      1. https://github.com/csuntechlab/calstatepays
   1. Tasks:
      1. Install calstatepays on your laptop
      1. Install calstatepays on your "production" VM
      1. Respond to the thread in the slack channel
         - Thread name "calstatepays is up"  (initiated by steve)
         - Response:  the URL of calstatepays on your cit384-${USER} VM

