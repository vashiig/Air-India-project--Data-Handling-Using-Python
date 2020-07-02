import pandas as pd
import datetime
import csv
# enter the name of file that is clean final file
nof = input("enter the name of file ", )

df = pd.read_csv(nof+'_finalfile.csv')
group_data = df.groupby(['Flight Number', 'Aircraft Registration Number', 'Departure Airport Code', 'Arrival Airport Code', 'Dom Intl Flag']).sum()
print(group_data)
columns = ['Aircraft Payload', 'Available Payload', 'Maximum Zero Fuel Weight (Kgs)', 'Actual Zero Fuel Weight (Kgs)', 'Take Off Fuel','Maximum Take Off Weight (Kgs)', 'Actual Take Off Weight (Kgs)', 'Trip Fuel Leg', 'Maximum Landing Weight (Kgs)', 'Actual Landing Weight (Kgs)',	'First Class Flown Passenger', 'Business Class Flown Passenger', 'Economy Class Flown Passenger', 'Total Male', 'Total Female',	'Total Children', 'Total Infants', 'Total Passenger Weight (Kgs)', 'Total Compartment Weight (Kgs)', 'Total Baggage Weight Leg (Kgs)','Total Engg Weight Leg (Kgs)',	'Dry Operating Weight (Kgs)',	'Cockpit Crew Count',	'Cabin Crew Count',	'First Class Non Revenue Passenger',	'Business Class Non Revenue Passenger',	'Economy Class Non Revenue Passenger']
group_data = group_data.drop(columns, axis=1)
#print(group_data)
group_data.to_csv('MailFreight_' + nof + '.csv')

# print("here start the cargo and mail report")

f1 = open('MailFreight_' + nof + '.csv', 'r')
f2 = open('Distance.csv', 'r')
f3 = open('MailFreight_' + nof + 'report.csv', 'w')
c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)
my_file = list(c1)
dist = list(c2)
d = 0
for i in range(1, len(my_file)):
    for j in range(1, len(dist)):
       if my_file[i][2:4] == dist[j][1:3]:
            mail = (round((float(my_file[i][6])*float(dist[j][3]))/1000))
            cargo = (round((float(my_file[i][5])*float(dist[j][3]))/1000))
            #print(my_file[i][0] + "\t\t\t" + my_file[i][1] + "\t\t\t" + my_file[i][2]+"\t\t\t" + my_file[i][3]+"\t\t\t" + my_file[i][4]+"\t\t\t" + my_file[i][5]+"\t\t\t" + my_file[i][6]+"\t\t\t"+ str(cargo)+"\t\t\t"+ str(mail))
            res = my_file[i] + [cargo] + [mail]
            c3.writerow(res)
           # print(res)
            d = d+1
print(d)
f1.close()
f2.close()
f3.close()

mf = pd.read_csv('MailFreight_' + nof + 'report.csv', header=None)
mf.columns = ['Flight No', 'AC Type', 'From Sector','To Sector','Int:Dom Flag(Capacity)','Freight/Cargo Weight in Kg','Mail Weight in Kg','Freight/TKM/CTKMS','MTKMS']
mf.to_csv("MailFreight_"+nof+"report.csv", index=False)
new = open('MailFreight_'+nof+'report.csv', 'r')
new = ''.join([i for i in new]).replace("AI9", "9I0")
x = open('MailFreight_'+nof+'report.csv', 'w')
x.writelines(new)
x.close()

#MF = pd.read_csv('MailFreight_'+nof+'report.csv', header=None)
#col_name = ['Flight No','AC Type','From Sector','To Sector','Int:Dom Flag(Capacity)','Freight/Cargo Weight in Kg','Mail Weight in Kg','Freight/TKM/CTKMS','MTKMS']
#col_name[6],col_name[7]=col_name[7],col_name[6]
#print(col_name)
#MF.iloc[:,['Flight No', 'AC Type', 'From Sector', 'To Sector', 'Int:Dom Flag(Capacity)', 'Freight/Cargo Weight in Kg', 'Freight/TKM/CTKMS', 'Mail Weight in Kg', 'MTKMS']]
#MF.to_csv('MailFreight_'+nof+'report.csv', header=None)


#df1 = pd.read_csv('MailFreight_'+nof+'report.csv')
# sorting the file
#df1.sort_values(['Flight No'], axis=0, ascending=True, inplace=True)
# saving the result file
#df1.to_csv('MailFreight_'+nof+'report.csv', index=False)




