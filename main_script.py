!pip install python-dotenv
from google.colab import drive
drive.mount("/content/drive")


#This is to load my sensitive details which i had initialised in a separate environment for security purposes
import os
from dotenv import load_dotenv

load_dotenv("/content/drive/MyDrive/OurVarEnv.env")
my_email = os.getenv("EMAIL_USERN")
my_password = os.getenv("EMAIL_PASSW")

try:
    if my_email and my_password:
        print("Congrats brotherly🚀🚀🚀🚀💯💯,your email and password are accessed successfully and in a secured way")
    else:
        print("damn it,an error occurred on the way,so sorry")

except Exception as e:
    print(f"An error occurred as {e}")
#print(my_email)
#print(my_password)

#Now lets curate a script that would automate the email sending using my email and password i accessed here together with the dummy created details earlier created
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from datetime import datetime

#Lets read in our data
data = pd.read_csv("/content/drive/MyDrive/recipients.csv")
data

# SMTP server configuration (Gmail example)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Initialize the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Secure the connection
server.login(my_email, my_password)

# Iterate through each recipient and send email
for index, row in data.iterrows():
    recipient_email = row['Email']
    subject = row['Subject']
    message = row['Message']

# Create email content
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

#Send the email
    try:
        server.sendmail(my_email, recipient_email, msg.as_string())
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}")
# Close the SMTP server conne
#server.quit()

#Just as you can see,All mails delivered successfully,only meed a bag of valid and purposeful email address to work with this for real life

