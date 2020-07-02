# this program is to merge final file and B-A file in result file
import pandas as pd
import csv
nof = input("enter the name of month 'Jun':", )
yr = input("enter the name of yr '19':", )

f1 = open("Tap_"+nof+yr+".csv", "r")
f2 = open("Tap_"+nof+yr+"_A-B.csv", "r")
f3 = open(nof+yr+"_res.csv", "w")

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

file_1 = list(c1)
file_2 = list(c2)


for i in range(len(file_1)):
    for j in range(len(file_2)):
        if file_1[i][0:5] == file_2[j][0:5]:
            res = file_1[i][0:34]
            # print(res)
            c3.writerow(res)

f1.close()
f2.close()
f3.close()

df = pd.read_csv(nof+yr+"_res.csv", header=None)
df.columns = ['Flight Number', 'Flight Departure Date', 'Aircraft Registration Number', 'Departure Airport Code', 'Arrival Airport Code', 'Aircraft Payload', 'Available Payload', 'Maximum Zero Fuel Weight (Kgs)', 'Actual Zero Fuel Weight (Kgs)', 'Take Off Fuel', 'Maximum Take Off Weight (Kgs)', 'Actual Take Off Weight (Kgs)', 'Trip Fuel Leg', 'Maximum Landing Weight (Kgs)', 'Actual Landing Weight (Kgs)', 'First Class Flown Passenger', 'Business Class Flown Passenger', 'Economy Class Flown Passenger', 'Total Male', 'Total Female', 'Total Children', 'Total Infants', 'Total Passenger Weight (Kgs)', 'Total Compartment Weight (Kgs)', 'Total Baggage Weight Leg (Kgs)', 'Total Cargo Weight Leg (Kgs)', 'Total Mail Weight Leg (Kgs)', 'Total Engg Weight Leg (Kgs)', 'Dry Operating Weight (Kgs)', 'Cockpit Crew Count', 'Cabin Crew Count', 'First Class Non Revenue Passenger', 'Business Class Non Revenue Passenger', 'Economy Class Non Revenue Passenger']
#  df.columns = ['Flt_No', 'Flt_Dt', 'AC_Reg', 'Dep_Stn', 'Arr_Stn', 'Pay_Max', 'Pay_Act', 'ZFW_Max', 'ZFW_Act', 'Take_Off_Fuel', 'TOW_Max', 'TOW_Act', 'Trip_Fuel', 'LW_Max', 'LW_Act', 'Pax_F', 'Pax_C', 'Pax_Y', 'Pax_Male', 'Pax_Female','Pax_Child', 'Pax_Infant', 'Pax_Load', 'Load_Comp', 'Bag_Load', 'Cargo_Load', 'Mail_Load', 'Engg_Load', 'Dry_Op_Wt', 'Cockpit_Crew', 'Cabin_Crew', 'Pad_F', 'Pad_C', 'Pad_Y']
df.sort_values(['Flight Number', 'Flight Departure Date'], axis=0, ascending=True, inplace=True)
print(df)
df.to_csv(nof+yr+"_res.csv", index=False)

a = pd.read_csv(nof+yr+"_res.csv")
b = pd.read_csv(nof+"20"+yr+"_finalfile.csv")

merged = a.append(b, sort=False)
merged.to_csv(nof+yr+'_res.csv', index=False)
df = pd.read_csv(nof+yr+'_res.csv')
# dropping unnecessary column
df = df.drop(['Dom Intl Flag'], axis=1)
# sorting the file
df.sort_values(['Flight Number', 'Flight Departure Date'], axis=0, ascending=True, inplace=True)
# saving the result file
df.to_csv(nof+yr+'_res.csv', index=False)
