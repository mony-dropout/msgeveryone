import pandas as pd

# Read the CSV file and specify the columns to use
contacts = pd.read_csv("fcontacts.csv", usecols=["Name", "Phone"])

# Drop rows where 'Phone Number' is blank or NaN
contacts = contacts.dropna(subset=["Phone"])

# Iterate through each contact
for index, row in contacts.iterrows():
    name = row['Name']
    phone = row['Phone']
    print(f"Name: {name}, Phone: {phone}")

