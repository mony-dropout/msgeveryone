import pandas as pd
df=pd.read_csv("full_contacts.csv")
fdf=pd.DataFrame()
fdf['name']=df['First Name']
fdf['phone']=df['Home Phone']
fdf.to_csv('bestever.csv',index=False)


