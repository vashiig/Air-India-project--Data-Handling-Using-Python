# this prog is to find the difference between tap file and final file
import pandas as pd
import csv

nof = input("Enter the name of file ", )
yr = input("Enter the yr(only last 2 digits) ", )
df2 = pd.read_csv("Tap_"+nof+yr+".csv")
df2 = pd.DataFrame(df2, columns=['Flt_No', 'Flt_Dt', 'AC_Reg', 'Dep_Stn', 'Arr_Stn'])
df2['key1'] = df2['Flt_No'] + ',' + df2['Flt_Dt'] + ','+df2['AC_Reg'] + ',' + df2['Dep_Stn'] + ',' + df2['Arr_Stn']
# print((df2.dtypes))

df2.to_csv('a.csv', index=None)
# print(df2)

df = pd.read_csv(nof+"20"+yr+"_finalfile.csv")
df = pd.DataFrame(df, columns=['Flight Number', 'Flight Departure Date', 'Aircraft Registration Number', 'Departure Airport Code', 'Arrival Airport Code'])
df['key1'] = df['Flight Number'] + ',' + df['Flight Departure Date'] + ','+df['Aircraft Registration Number']+','+df['Departure Airport Code']+','+df['Arrival Airport Code']
# df['key1'].astype(int)
# print(df.dtypes)
df.to_csv('b.csv', index=None)
# print(df)

f1 = open("Tap_"+nof+yr+"_A-B.csv", "w")
c1 = csv.writer(f1)
print("here start A-B ")
A = set(pd.read_csv("a.csv", index_col=False, header=None)[5])  #  reads the tap csv file , takes only the key column and creates a set out of it.
B = set(pd.read_csv("b.csv", index_col=False, header=None)[5])  # same for the month file
C = list(A-B)
for i in range(len(C)):
    res = C[i].split(",")
    print(res)
    c1.writerow(res)
f1.close()

print("here start B-A \n ")
f2 = open(nof+'20'+yr+'_finalfile_B-A.csv', 'w')
c2 = csv.writer(f2)
D = list(B-A)
for j in range(1, len(D)):
    res_n = D[j].split(",")
    print(res_n)
    c2.writerow(res_n)
f2.close()


data = pd.read_csv('Tap_'+nof+yr+'_A-B.csv')
data.columns = ['Flt_No', 'Flt_Dt', 'AC_Reg', 'Dep_Stn', 'Arr_Stn']
data.sort_values(['Flt_No', 'Flt_Dt'], axis=0, ascending=True, inplace=True)
data.to_csv('Tap_'+nof+yr+'_A-B.csv', index=False)
# print(data)

data1 = pd.read_csv(nof+"20"+yr+"_finalfile_B-A.csv")
data1.columns = ['Flight Number', 'Flight Departure Date', 'Aircarft Registration Number', 'Departure Airport Code', 'Arrival Airport Code']
data1.sort_values(['Flight Number', 'Flight Departure Date'], axis=0, ascending=True, inplace=True)
data1.to_csv(nof+"20"+yr+"_finalfile_B-A.csv", index=False)
# print(data1)

