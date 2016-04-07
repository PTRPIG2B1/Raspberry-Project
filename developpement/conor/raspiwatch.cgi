#!/bin/bash
echo "Content-type: text/html"
echo ""

if [ "$REQUEST_METHOD" == "GET" ]; then
	/usr/bin/python2 /home/pi/RaspiWatch/bin/cgicontroller.py $QUERY_STRING
else
	STDIN=$(cat)
	/usr/bin/python2 /home/pi/RaspiWatch/bin/cgicontroller.py $STDIN
	echo "POST"
fi


echo "<html><head><title>RASPIWATCH</title>"
echo "<script type='text/javascript'>"
echo "window.open('', '_self', ''); window.close();"
echo "</script></head><body>"
echo "</body></html>"
