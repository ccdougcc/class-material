#! /usr/bin/python


# Program Name: Counter
# Given the number N via the querystring, the program
# outputs the values 0..N

# 1. Consider writing to a logfile
# 2. Consult a configuration file,  .htaccess
# 3. Consult the environments
# 4. Optional read the HTTP request body
# 5. Emit my HTTP response header
# 6. Emit a blank line
# 7. Emit my HTTP response body

if [ -f ./.htaccess ] ; then
  source ./.htaccess
fi

echo "This program run on: $(date)" >> ./counter.log

# Read the value from the Query String
N=${QUERY_STRING}

# emit my HTTP response header
echo "X-generated-by: Andrew"
echo "content-type: text/html"
echo "x-directory: $(pwd)"

# emit a blank line
#echo ""

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

counter=0
while (( counter <= N )) ; do
   echo "<li>$counter </li>"
   (( counter ++ ))
done


# emit some of the HTML Stuff
cat <<EOF
</ul>
</body>
</html>
EOF