# this program is to merge final file and B-A file in result file
import pandas as pd
import csv
nof = input("enter the name of month 'Jun':", )
yr = input("enter the name of yr '19':", )

f1 = open(nof+"20"+yr+"_finalfile.csv", "r")
f2 = open(nof+"20"+yr+"_finalfile_B-A.csv", "r")
f3 = open("Tap_"+nof+yr+"_res.csv", "w")

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

df = pd.read_csv("Tap_"+nof+yr+"_res.csv", header=None)
df.columns = ['Flt_No', 'Flt_Dt', 'AC_Reg', 'Dep_Stn', 'Arr_Stn', 'Pay_Max', 'Pay_Act', 'ZFW_Max', 'ZFW_Act', 'Take_Off_Fuel', 'TOW_Max', 'TOW_Act', 'Trip_Fuel', 'LW_Max', 'LW_Act', 'Pax_F', 'Pax_C', 'Pax_Y', 'Pax_Male', 'Pax_Female','Pax_Child', 'Pax_Infant', 'Pax_Load', 'Load_Comp', 'Bag_Load', 'Cargo_Load', 'Mail_Load', 'Engg_Load', 'Dry_Op_Wt', 'Cockpit_Crew', 'Cabin_Crew', 'Pad_F', 'Pad_C', 'Pad_Y']
df.sort_values(['Flt_No', 'Flt_Dt'], axis=0, ascending=True, inplace=True)
df.to_csv("Tap_"+nof+yr+"_res.csv", index=False)
# consist of rows present in Apr2019_finalfile_A-A data
a = pd.read_csv("Tap_"+nof+yr+"_res.csv")
# read tap file
b = pd.read_csv("Tap_"+nof+yr+".csv")
# appending tap file data in a file
merged = a.append(b, sort=False)
# print(merged)
merged.to_csv('Tap_'+nof+yr+'_res.csv', index=False)
# reading result file consist of 42 columns
df = pd.read_csv('Tap_'+nof+yr+'_res.csv')
# dropping uneccessary column
df = df.drop(['LDM_Dt', 'RMK', 'UndLoadBefLMC', 'ThruBagLoad', 'ThruCargoLoad', 'ThruMailLoad', 'Leg_No', 'Flt_No_Flt_Dt_Dep_Stn_Arr_Stn'], axis=1)
# sorting the file
df.sort_values(['Flt_No', 'Flt_Dt'], axis=0, ascending=True, inplace=True)
# saving the result file
df.to_csv('Tap_'+nof+yr+'_res.csv', index=False)

