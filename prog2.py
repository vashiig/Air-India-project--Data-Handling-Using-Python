#this program is to sort or convert the date fromat in desired form
import pandas as pd
import datetime
#enter the name of tap file
nof=input("enter the name of tap file ", )
#enter the name of month file
nof1=input("enter the name of  file ", )

#this part is use for converting the date format of tap file if format is already in desired form then it will show the error
df=pd.read_csv("Tap_"+nof+".csv")
df.Flt_Dt = pd.to_datetime(df.Flt_Dt, format='%d/%m/%Y')
df.to_csv("Tap_"+nof+".csv",index=False)

#this part is use to convert the date format of month file
#df=pd.read_csv(nof1+"_finalfile.csv")
#df=df.rename(columns={ "Flight Departure Date" : "Flight_Departure_Date"})
#df.Flight_Departure_Date = pd.to_datetime(df.Flight_Departure_Date)
#df.to_csv(nof1+"_finalfile.csv",index=False)

#this part of code is used to convertthe AI9 to 9I0 format
new=open(nof1+'_finalfile.csv','r')
new=''.join([i for i in new]).replace("AI9","9I0")
x=open(nof1+'_finalfile.csv','w')
x.writelines(new)
x.close()
# this part of code is used to sort the csv file
df = pd.read_csv(nof1+'_finalfile.csv')
df.sort_values(['Flight Number','Flight Departure Date'],axis = 0, ascending = True,
                 inplace = True)
print(df)
df.to_csv(nof1+'_finalfile.csv',index=False)

