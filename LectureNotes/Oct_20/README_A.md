# Lecture October 20, 2021

## Announcements
   1. Lecture today is about Regular Expressions
   1. Lab today is about giving you time to work on your project

## Regular Expression
   1. Machines and Languages
      - Combinational Circuits -- Boolean Algerbra
      - Finite State Machine -- Regular Language (Regular Expressions)
      - PDA (Pushdown Automata) -- Context Free Langague (BNF)
      - Limited Bounded Automata -- Context Sensitve Language 
      - Turing machine --- Recursively Enumerable Language
         - Univeral Computer:
           1. limited tape equivalent to main memory
           1. the control program is placed into main memory
           1. the program is placed into main memory
           1. the input & out is placed into main memory
   1. Regular Languages and Regular Expressions
      - Regular Language:
      ```
        P -> p P
           | a
      
      ```
      - Derivation:  P => p P => p p P => p p p P => p .... p P => p p ... p a
      - Regular Expression : p* a

   1. Practical Syntax of Regular Expressions
      - the shell... globbing...
      - basic regular expression, grep 
        - global reg expression print: sed '/re/pg'
        - obsolete regular expresion
      - POSIX or extended regular expression
        - used by egrep 
      - Perl regular expressions  
        - lots of syntatic sugar
        - used by Apache in rewrite rules 


## Searching for Stuff
  - regular expression for a date :  i.e., what's is format/syntax
    -  mm/dd/yyyy
    -  yyyy/mm/dd
    -  ss/mm/yyy
    - ( 0 | 1)( 0 | 1 | 2| 3 | 4 | 5 | 6 |7 |8 |9 ) "/"
    - ``[01][0-9]"/"[0123][0-9]"/"[0-9]{4}``
    = \d\d"/""\d\d"/"\d{4}"

## Apache Logging
  - AccessLog
  ```
    LogFormat
    CustomLog
  
  ```


## Regular Expressions... Kleene's theory...
  - lambda is regular expression 
  - any single character is a regex
  - ( regex ) is a regex
  - regex . regex is a regex
  - regex | regex is a regex
  - regex * is regex  (regex any number of times.)


## Extra metacharacters
   - . : any character (except for \n )
   - ^ : beginning of the line
   - $ : end of the line

## Syntax Sugar: Choice
  - [0-9]       [[:digit:]]  \d
  - [a-zA-Z]    [[:alpha]:] 
  - [a-zA-Z0-9] [[:alnum:]]  \w 
  - [ \t\v\f]   [[:space:]]  \s  
  - [^0-9]      [^[:digit:]] \D
  - [^a-zA-Z]   [^[:alpha]:] 
  - [^a-zA-Z0-9][^[:alnum:]] \W 
  - [^ \t\v\f]  [^[:space:]] \S

 

### Syntax Sugar (Repetition)
  1. (regexp){0,1} == ? : at most 1, it is either choice or don't choice it.
  1. Greedy
     - (regex){n,m}: at least "n" but not more than "m"
     - (regex){n}  : exactly "n" regex
     - (regex){n,} : at least "n"
     - (regex){,m} : at most "m"
  1. Non-Greedy (Polite)
     - regex * == (regex){0,}?
     - regex + == (regex){1,}?
  1. Gready Equivalence
     - ``(regex){0,} ==  regex *+`` 
     - ``(regex){1,} ==  regex ++``

### Modifies (perl)
  (?i)acess.log((.\d*)(\.gz)?)?

### Example of Greediness
  1. ``AliasMatch "/image/(.*)\.jpg$" "/files/jpg.images/$1.jpg" ``
      - URI: /image/abcd...abc.jpg    -- Match!
   1. ``AliasMatch "/image/(.{0,})\.jpg$" "/files/jpg.images/$1.jpg" ``
      - URI: /image/abcd...abc.jpg    -- does not Match

### KISS


# Resources
  1. The prof highly/strong/emphatically recommends that 
    - you learn regular expressions, and
    - the tools that exploit their power

  1. A free book about [Regular Expressions](https://learning.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/)

  1. A free book on [Sed and Awk](https://learning.oreilly.com/library/view/sed-awk/1565922255/)
  1. https://regex101.com

### Simple Sed example
  1. ``sed 's/#UserDir/UserDir/' httpd.conf >new_http.conf``
     - removes the comment character within your httpd.conf on http container
     - this is one approach to enabling the UserDir directive on your http container


