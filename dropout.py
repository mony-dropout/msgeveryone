import pandas as pd
contacts=pd.read_csv("contacts.csv")
for index, row in contacts.iterrows():
    name=row['name']
    phone=row['phone']
    message = f"Happy New Year {name}!"
    print(message)
