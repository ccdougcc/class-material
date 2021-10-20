# Lecture October 20, 2021

## Announcements
   1. Lecture today is about Regular Expressions
   1. Lab today is about giving you time to work on your project

## Regular Expression
   1. Machines and Languages
      1. Boolean Algebra & Computational Circuits
      1. Regular Expressions & Finite State Machine 
      1. Context Free Language & Push-down Automate (PDA)
      1. Context Sensitive Languages  & Limited bounded Automate
      1. Recursively Enumerable Language & Turing Machine
         - Universal Computer
           - Tape --> Memory
           - Store the control program, the program, and the input/output

   1. Regular Languages and Regular Expressions
      1. Regular Language Example
        ```
        P -> c P
          | c      
        ```
      1. Derivation for the string "ccc" : P => c P => c c P => c c c

      1. Corresponding Regular Expression
        ```
        c*
      
        ```
   

   1. Practical Syntax of Regular Expressions
      - the shell... globbing
      ```
        Bash itself cannot recognize Regular Expressions. Inside scripts, it is commands and utilities -- such as sed and awk -- that interpret RE's.
      ```
      - basic regular expressions
        - also known as obsolete
        - used, for example, by grep
          - Global Regular Expression Print
      - POSIX or extended regular expressions
        - used by egrep
      - Perl regular expressions
        - more syntax sugar
        - used by Apache in rewrite rules

## Searching for Stuff

## Apache Logging
   - LogFormat
   ```
     LogFormat "%f %h %m"
   
   ```
   - Sample Access Log 

## Simple patterns
  - Month dd, yyyy
  >> - yyyy/mm/dd    :   [0-9]{4}"(/|-)"[0-9]{2}"(/|-)"[0-9]{2}


## Regular Expressions... Kleene's theory...
  - lambda is regular expression 
  - any single character is a regex
  - ( regex ) is a regex
  - regex . regex is a regex
  - regex | regex is a regex
  - regex * is regex  (regex any number of times.)


## RegEx examples
  - 5 a's followed by a "bc"
    - aaaaabc
  - at least 5 's followed be a "bc" and then at least 2 a's
    - aaaaa a* bc aa a*
  - even number of a's followed by "bc" and then followed be an odd number of a's
    - ``(aa)* bc (aa)*a``
  - this : [0-9]{4}"(/|-)"[0-9]{2}"(/|-)"[0-9]{2}
    (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 )    (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 )    (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 )    (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 ) ( / | - )    (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 )    (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 ) ( / | - )     (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 )     (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 )

### Syntax Sugar (Choice)
  - [0-9]  [[:digit:]] \d
  - [a-zA-Z] [[:alpha]:] 
  - [a-zA-Z0-9] [[:alnum:]]  \w 
  - [ \t\v\f]  [[:space:]]  \s  
  - [^0-9]  [^[:digit:]] \D
  - [^a-zA-Z] [^[:alpha]:] 
  - [^a-zA-Z0-9] [^[:alnum:]]  \W 
  - [^ \t\v\f]  [^[:space:]]  \S

### Example
  -   - this : [0-9]{4}"(/|-)"[0-9]{2}"(/|-)"[0-9]{2}
  - \d\d\d\d ("/"| "-" ) \d\d ("/"| "-" ) \d\d

### Syntax Sugar (Repetition)
  1. Greedy
     - (regex){n,m}: at least "n" but not more than "m"
     - (regex){n}  : exactly "n" regex
     - (regex){n,} : at least "n"
     - (regex){,m} : at most "m"
  1. NonGready (polite)
     - regex * == (regex){0,}? : zero or more
     - regex + == (regex)(regex)* == (regex){1,}? : one or more 
  1. Non Greedy with {}
     - ``(regex){0,} == (regex)*+``
     - ``(regex){1,} == (regex)++``


### Example of Greedy and not greedy
   1. ``AliasMatch "^/image/(.*)\.jpg$" "/files/jpg.images/$1.jpg" ``
      - URI: /image/abcd...abc.jpg   -- this matches 

   1. ``AliasMatch "^/image/.{0,}\.jpg$" "/files/jpg.images/$1.jpg" ``
      - URI: /image/abcd...abc.jpg   -- does not match --- because its greedy!

### Modifiers for greediness
   - ? : hmm, do you need this regex later on?  make it polite
   - + : take more... make it greedy

### KISS


# Resources
  1. The prof highly/strong/emphatically recommends that 
    - you learn regular expressions, and
    - the tools that exploit their power
  1. A free book about [Regular Expressions](https://learning.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/)
  1. A free book on [Sed and Awk](https://learning.oreilly.com/library/view/sed-awk/1565922255/)

### Simple Sed example
  1. ``sed 's/#UserDir/UserDir' httpd.conf >new_http.conf``
     - removes the comment character within your httpd.conf on http container
     - this is one approach to enabling the UserDir directive on your http container


