# Browser side activites

## URLs of Note
  1. https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
  1. https://en.wikipedia.org/wiki/List_of_HTTP_header_fields


## Given the URL, what done
  * https://steve@www.csun.edu:6660/~steve/?var=value&var2=value2#ls
  1. DNS lookup on www.csun.edu -> 130.166.238.195
  1. creates a socket
     - 130.166.238.195:6660 130.166.38.161:${Random}
  1. Build the header
     - request VERB: GET
     - URI: /~steve/?var=value&var2=value2
     - HTTP/1.1
     * throw away the fragment
  1. Send header
  1. Send blank
  1. Send body (i.e. this is NoOp)
  1. wait
  1. read the box (Status Line, header, blankline, body)
  1. print the box on stdout or
     * hand the payload to the browser.
     * browser renders the contents

     


