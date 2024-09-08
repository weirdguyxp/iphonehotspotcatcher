import subprocess
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email_id="your gmail"
sender_email_id_password="your gmail pw"
receiver_email_id="your recipient gmail,your other recipient gmail"

print("i ran")

stdoutdata = subprocess.getoutput("/usr/sbin/iwlist wlan0 scan")
#print("stdoutdata: " + stdoutdata.split()[0])
#print("stdoutdata: " + stdoutdata)

print("after command")

iterator = 0
for i in stdoutdata.split('\n'):
        #print(i)
        #print(iterator)
        if re.match(r".*iPhone.*",i):
                print(i)

                #code to send email
                # creates SMTP session
                s = smtplib.SMTP('smtp.gmail.com', 587)

                # start TLS for security
                s.starttls()

                # Authentication
                s.login(sender_email_id, sender_email_id_password)

                # message to be sent
                message = "Hello\n\n Looks like someone (maybe kid name here) turned on their iphone hotspot.\n SSID details:"+i+"\n\n-The ever-watching Pi"

                #build msg
                rcpt = receiver_email_id.split(",")

                msg=MIMEMultipart('alterative')
                msg['Subject'] = "iPhone hotspot detected"
                msg['To'] = receiver_email_id
                msg['From'] = sender_email_id
                msg.attach(MIMEText(message))

                # sending the mail
                s.sendmail(sender_email_id, rcpt, msg.as_string())

                # terminating the session
                s.quit()



                #failed attempt at getting context below
                #j = iterator
                #l = iterator
                #print(j)
                #print(l)
                #k = int(j) + 10
                #print(k)
                #for j in range (l, k):
                #       print(stdoutdata.split()[j])
                #       print(iterator)
                #       print(j)

                #endloop
                break
        iterator = iterator + 1
        #print(iterator)


