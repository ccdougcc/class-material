# Lecture October 27, 2021

## Notes:
   - (A) Cleanup on Limit and Auth for .htaccess
   - (M) Cleanup on Conditional Includes

## Questions:
   - (A) General progress on the lab?

## Last time:
   - Regular Expressions
     - globbing" ``* ?``
       - Metacharacters
         - `` $ ~ #  ! . .. ... * ? ``
         - $var : lookup the value of variable that immediate follows the dollar
         - ~ : lookup the user's home directory, must be the first character of the word
            - ``http://host:port/~steve/foobar``
            - ``/~steve/foobar`` : the ~ must be the first character of the first slug
              - ``/my/file/~steve/location``
        - # : the start of the comment, everything to the right is ignored (and the #)
        - ! : related to the history command
          - #! : This is comment because of the #, but the shell does something special if
             - its on the first line of a script
          - <!--  comment -->
             - This is a comment unless we are doing server sides, then comment is a directive.
        - . : as a separate word/slug, it represents "this", the current directory
        - .. : as a separate word/slug, it represents the parent of the current directory 
        - * : the equivalent regular is ``(.*)``
       - Escaping
         - \$, \n
         - var=hello
         - weak quotes:  echo "$var" --> hello
         - strong quotes echo '$var' --> $var
     - basic reg-expr (obsolete)
     - extended reg-expr
     - perl 
   - Meta characters for RegEx
     - ^ : 
        - within the context of a choice... it negates it...
        - the start of the line, othewise
           - Examples when to use in Apache
             - ``AliasMatch "^/this/start/of/the/URI"  "/~steve"``   #A
             - ``AliasMatch "/this/start/of/the/URI"   "/~Andrew"``  #B
                - https://www.domain.com/this/start/of/the/URI
                   - both A & B matches this 
                - https://www.domain.com/does/it/start/at /this/start/of/the/URI
                   - B matches this
     - $ :
        - the end of the line (" ....   $")
          - Examples when to use in Apache
             - ``AliasMatch "/this/start/of/the/URI$"  "/~steve"``   #A
             - ``AliasMatch "/this/start/of/the/URI"   "/~Andrew"``  #B
                - https://www.domain.com /this/start/of/the/URI/but/there/is/more
                   -  B matches this
                - https://www.domain.com/this/start/of/the/URI
                   - A & B matches this
      - . : 
        - any character, except \n


   - Greedy / Nongreedy
      - If greedy, and if you want to be polite, then ask
        - that is append the notation with a "?"
      - If polite, and if you want to be greed, then grab _more_
        - that is append the notation with a "+"
      - Example
        - (ab){3,4}(ab)(ab){,2}
          - (ab ab ab ab) (ab) (ab ab)  : the longest string that matches
          - ababababab : this matches
            - (ab ab ab) (ab) (ab) 
            - (ab ab ab ab) (ab) ()  -- being greedy with {3,4}
       - (ab){3,4}(ab)c
          - ab ab ab ab ab c  - matches

          - ababababc
            - ( ab ab ab ab ) c  -- Nope  , greedy
            - ( ab ab ab ) ab c  -- Yes, matches,  but under NOT greedy



   - Syntax Sugar 
     - choice:  ( a | b | c ) -> [abc]
       - negation on the choice [^abc]
     - (regexp)* : zero or more of "regexp"
     - (regexp)(regexp)* one or more of "regexp"

     - repetition: aa* == a+ ->  (reg_expr){lower_limit, upper_limit}
       - a* == a{0,}

       - a{5,}: at least 5 or more
       - a{,5}: at most 5
       - a{3,5}: at least 3 but not more than 5


   - Directives
     - ``<FilesMatch perl-regex>``
     - ``<AliasMatch perl-regex>``
     - ``<Directory globbing>``
