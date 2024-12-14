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


