#! /bin/bash

# Program Name: Counter
# Given the number N via the querystring, the program
# outputs the values 0..N

# -1. Consider writing to a logfile
# 0. Consult a configuration file,  .htaccess
# 1. consult the environments
# 2. optional read the HTTP body
# 3. emit my HTTP response header
# 4. emit a blank line
# 5. emit my HTTP response body

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