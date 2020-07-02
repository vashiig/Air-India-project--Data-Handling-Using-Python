# this program is to find the similar rows between final file and tap file
import pandas as pd
import csv
nof = input("enter the name of file 'Jun' ", )
yr = input("enter the name of year file", )
f1 = open("Tap_"+nof+yr+".csv", "r")
f2 = open(nof+"20"+yr+"_finalfile.csv", "r")
f3 = open("res_"+nof+yr+".csv", 'w')

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

file_1 = list(c1)
file_2 = list(c2)

for i in range(1, len(file_1)-1):
    for j in range(1, len(file_2)-1):
        if file_1[i][0:2] == file_2[j][0:2]:
            if file_1[i][3:5] == file_2[j][3:5]:
                res = file_1[i]
                print(res)
                c3.writerow(res)
f1.close()
f2.close()
f3.close()

df = pd.read_csv('res_'+nof+yr+'.csv', header=None)
#df.columns=['Flt_No','Flt_Dt','AC_Reg','Dep_Stn','Arr_Stn','Pay_Max','Pay_Act','ZFW_Max','ZFW_Act','Take_Off_Fuel','TOW_Max','TOW_Act','Trip_Fuel','LW_Max','LW_Act','Pax_F','Pax_C','Pax_Y','Pax_Male','Pax_Female','Pax_Child','Pax_Infant','Pax_Load','Load_Comp','Bag_Load','Cargo_Load','Mail_Load','Engg_Load','Dry_Op_Wt,Cockpit_Crew','Cabin_Crew,Pad_F,Pad_C,Pad_Y','LDM_Dt,RMK,UndLoadBefLMC','ThruBagLoad,ThruCargoLoad','ThruMailLoad,Leg_No','Flt_No_Flt_Dt_Dep_Stn_Arr_Stn']
df.to_csv('res_'+nof+yr+'.csv', index=False)
