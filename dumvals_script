from faker import Faker #import faker
import csv #We import csv to create the csv file for our test datas
from google.colab import files #We import files to be able to download the crested file later after creating to our local storage


#Next we initialise faker
fake = Faker()

#Now lets name the csv file
file_name = "recipients.csv"

#Now lets create the csv file
with open(file_name, 'w', newline='', encoding= 'utf-8') as my_file:
    writer = csv.writer(my_file)
    #Lets write the hewder row(the names of the columms precisely)
    writer.writerow(['Name', 'Email', 'Subject', 'Message', 'Address'])


    #Now lets generate about 50 rows dummy datas,since we are just going to he testing
    for yo in range(50):
        name = fake.name()
        email = fake.email()
        address = fake.address()
        subject = "Welcome to our test service,sorry for any inconveniences experienced"
        message = f"Hello {name}, we are excited to have you onboard,this is to confirm that {address} is your valid home address, if its noe kindly get back to is as soon as possible "
        #address= fake.address_detail()
        writer.writerow([name , email , subject , message , address])

print(f"dummy values has been created successfully in {file_name}")

#Now lets download our csv file
files.download(file_name)

import pandas as pd
df = pd.read_csv(file_name)
df.head(50)
