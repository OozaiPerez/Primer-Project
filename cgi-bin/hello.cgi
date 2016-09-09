#!/bin/bash

echo "Content-type: text/plain"
echo ""
echo "Hello here is your environment"
env
echo "Try to curl here"
#curl a website
/usr/bin/curl -o /tmp/csun  http://www.csun.edu/engineering-computer-science
cat /tmp/csun-jlp70017