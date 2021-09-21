#! /bin/bash

#Good Morning or Good Evening..
### 
### 
### Write a CGI program that 
###    1. looks at the current time
###    2. if the time is AM, send back a webpage that says Good Morning
###    3. if the time is PM, send back a webpage that says Good Evening
###    4. add the `X-date:` header field that provides the command used to obtain the current time.
### 
###  Notes:
###    - use the date command to get the current time
###    - option one: Get the time with AM or PM provided.  Parse the output to determine what to do.
###      ``$ date +"%r"
###      11:28:52 AM
###      ``
###    - option two: Get the hour of the day (0..23), if the number is <= 11, say Good Morning
###      ``
###      $ date +"%H"
###      ``

_option="$1"

_hour=$(date +"%H")
_is_AM=$(date +"%r" | awk '{ print $2}')


# emit my HTTP response header
echo  "X-date: \$(date +\"%r\" | awk '{ print \$2}' )"

# emit a blank line
echo ""

# emit my HTTP response body
cat <<EOF
<!DOCTYPE html>
<html>
<head>
<title>Dynamic Good Morning / Evening Program</title>
</head>
<body>
<ul>
EOF

echo "<H1>"

# Option #1
if [[ ${_is_AM} == "AM" ]] ; then
  echo "Good Morning"
else
  echo "Good Evening"
fi

# Option #2
#if (( _hour <= 11 )) ; then
#  echo "Good Morning"
#else
#  echo "Good Evening"
#fi

echo "</H1>"



# emit some of the HTML Stuff
cat <<EOF
</ul>
</body>
</html>
EOF