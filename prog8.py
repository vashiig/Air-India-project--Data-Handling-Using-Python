import pandas as pd
import datetime
#this part is use to convert the date format of month file
nof1 =input("enter the name of file:", )
df=pd.read_csv(nof1+"_finalfile.csv")

df[['Flight Departure Date' ]]= pd.to_datetime(df[['Flight Departure Date']], format='%Y%m%d' )
#df.Flt_Dt = pd.to_datetime(df.Flt_Dt, format='%d/%m/%Y')
print(df)
df.to_csv(nof1+"_finalfile.csv",index=False)