# sameer saeed
# sending email msg of scraped data, including a screenshot 
# sender and recepient data are in config.py
# scraper data is in ws.py

import smtplib
import config
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from ws import *


subject = 'Product: ' + UPC + ' in: ' + Location
msg = 'Data retrieved at ' + date_time + '.'

with open(filename, 'rb') as f:
    img_data = f.read()

message = MIMEMultipart()
message['From'] = config.email
message['To'] = config.sendto
message['Subject'] = subject

# inputting data to email msg
text = MIMEText("Data retrieved at " + date_time)
message.attach(text)
image = MIMEImage(img_data, name=os.path.basename(filename))
message.attach(image)

# connecting to gmail account and sending msg
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(config.email, config.pw)
s.sendmail(config.email, config.sendto, message.as_string())
s.quit()
print('Mail sent to ' + config.sendto)
