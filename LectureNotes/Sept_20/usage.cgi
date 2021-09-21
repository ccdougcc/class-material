#! /bin/bash

#  Startup Code
#     Consider writing to a logfile
#     Consult a configuration file,  .htaccess
#     Consult the environment variables
#     Optional read the HTTP request body
#     Emit my HTTP response header
#     Emit a blank line
#    Emit my HTTP response body - consult the environment variables
#  Cleanup Cod

# Startup Code
STDIN_FILE=/tmp/input.txt



#Write to Log
echo "Running usage.cgi program on: $(date)" > ./usage.log


# Consult .htaccess
if [[ -f "./.htaccess"  ]] ; then 
  source ./.htaccess
fi

# Read the HTTP Request body
while read _line ;  do
	echo $_line
done > ${STDIN_FILE}

## Output the three parts of the HTTP box
# 1. Header
# 2. blank line
# 3. Body

# Header
echo "X-access_log_generated_by: $USER"
echo "Content-type: text/html"

# Blank line
echo ""

# emit my HTTP response body
cat <<EOF
<!DOCTYPE html>
<html>
<head>
<title>Simple counter program</title>
</head>
<body>
<ul>
EOF

echo "<pre>"
# Body
cat ${STDIN_FILE} access.log| sed -e 's/^[^\"]*\"//' -e 's|HTTP/1.1.*$||' | sort | uniq -c | sort -nr | grep "${QUERY_STRING}"

echo "</pre>"

#emit some of the HTML Stuff
cat <<EOF
</ul>
</body>
</html>
EOF



# Cleanup Code
#rm ${STDIN_FILE}
echo "Exiting usage.cgi program on:  $(date)" > ./usage.log
