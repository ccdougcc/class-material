# Lecture Notes for September 20 & 22, 2021

## Agenda 20th
  1. Pickup from last time, i.e., questions, etc.
  1. Highlevel HTTP Server.png
  1. CGI Program -- activities
     - Adminstrative steps
       - make a directory for your cgi stuff (\~/public_html/cgi-bin)
       - make the directory read and execute `chmod o+rx \~/public_html/cgi-bin`
       - craft you program (in the repo, make sure it is executable)
         - program name needs to a a file suffix: .cgi
       - `git pull` ( In step 2 you will do a `docker run` )

     - Application steps
       1. Consider writing to a logfile
       2. Consult a configuration file,  .htaccess
       3. Consult the environment value
       4. Optional read the HTTP request body
       5. Emit my HTTP response header
       6. Emit a blank line
       7. Emit my HTTP response body - consult the environment variables

 

## Agenda 22th
  1. Pickup from last time, i.e., questions, etc.



## Quick Lab Assignment: -- you have 15 minutes for this exercise
  1. Look at all of the resumes created by the class
  1. Provide a ranking of your top 5 picks
     - you can use any criteria to rank them
  1. Pick one of them and compare it to your resume
     - You can not pick your own
     - You can not pick a teammates
  1. Send an email to the professors that provides the following information
     - your URL
     - the URL of your top 5 picks, and the criteria used to rank the 
     - the URL of the student's resume in which you are comparing yours to.
     - three things that you like about the other students web page

