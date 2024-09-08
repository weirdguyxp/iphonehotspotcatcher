echo "i ran">/home/pi/out3.txt
printenv >>/home/pi/out3.txt
/usr/bin/python /home/pi/test2.py >> /home/pi/out4.txt 2>&1
