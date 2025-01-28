import pandas as pd
df=pd.read_csv("testing.csv")
df=df.astype(str)
for i,r in df.iterrows():
    n=r['name']
    p=r['phone']
    fname=n.split()[0]
    print(f"{fname}")
    print(f"{n}")
    print(f"{p}")
    df.loc[i,'strings']=True
df.to_csv("billions.csv",index=False)
    
