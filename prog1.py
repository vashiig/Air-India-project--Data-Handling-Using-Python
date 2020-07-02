# this program is to clean the data
import pandas as pd
import csv

Name_of_file = input("Enter the name of file you want to clean ", )

# this program is for single na data only
d = 0
file = open(Name_of_file + ".csv", "r")
file1 = open(Name_of_file + "_na_data_single.csv", 'w')
my_list = list(csv.reader(file))
c2 = csv.writer(file1)
print("Here start the data without duplicate")
for i in range(0, len(my_list)):
    if my_list[i][2] == "N/A":
         if ((my_list[i][0:2] == my_list[i+1][0:2]) and (my_list[i][3:5] == my_list[i+1][3:5])) == False :
                result_row = my_list[i]
              #  print("\n")
              #  print(result_row)
                c2.writerow(result_row)
                d = d + 1
print(d)
file.close()
file1.close()
# this program is for duplicate data with na
f1 = open(Name_of_file + "_duplicate_data_with_na.csv", 'w')
f2 = open(Name_of_file + ".csv", "r")
c = 0
e = 0
my_file = list(csv.reader(f2))
c3=csv.writer(f1)
print("\nHere start the na with duplicate data")
for i in range(0, len(my_file)):
    if my_file[i][2] == "N/A":
        e = e + 1
        for j in range(0, len(my_file)):
            if i == j:
                continue
            else:
                if my_file[i][0] == my_file[j][0]:
                    if my_file[i][1] == my_file[j][1]:
                        if my_file[i][3] == my_file[j][3]:
                            if my_file[i][4] == my_file[j][4]:
                                result = my_file[i]
                                result_next = my_file[j]
                                #  print(result)
                                #  print(result_next)
                                c3.writerow(result)
                                c3.writerow(result_next)
                                c = c + 1
print(c)
print(e)
f1.close()
f2.close()
# this prog is for file duplicate data without na
f = 0
g = 0
f3 = open(Name_of_file + "_duplicate_data_without_na.csv", 'w')
f4 = open(Name_of_file + ".csv", "r")
my_file = list(csv.reader(f4))
c4 = csv.writer(f3)
print("\nHere starts the duplicate data only")
for i in range(0, len(my_file)):
    if my_file[i][2] == "N/A":
        g = g + 1
        for j in range(0, len(my_file)):
            if i == j:
                continue
            else:
                if my_file[i][0] == my_file[j][0]:
                    if my_file[i][1] == my_file[j][1]:
                        if my_file[i][3] == my_file[j][3]:
                            if my_file[i][4] == my_file[j][4]:
                               # result = my_file[i]
                                result_next = my_file[j]
                                # print(result)
                                # print(result_next)
                                # c4.writerow(result)
                                c4.writerow(result_next)
                                f = f + 1
print(f, g)
f3.close()
f4.close()


na_data_only = pd.read_csv(Name_of_file + '_na_data_single.csv', header=None)
na_data_only.columns = ['Flight Number','Flight Departure Date','Aircraft Registration Number','Departure Airport Code','Arrival Airport Code','Aircraft Payload','Available Payload','Maximum Zero Fuel Weight (Kgs)','Actual Zero Fuel Weight (Kgs)','Take Off Fuel','Maximum Take Off Weight (Kgs)','Actual Take Off Weight (Kgs)','Trip Fuel Leg','Maximum Landing Weight (Kgs)','Actual Landing Weight (Kgs)','First Class Flown Passenger','Business Class Flown Passenger','Economy Class Flown Passenger','Total Male','Total Female','Total Children','Total Infants','Total Passenger Weight (Kgs)','Total Compartment Weight (Kgs)','Total Baggage Weight Leg (Kgs)','Total Cargo Weight Leg (Kgs)','Total Mail Weight Leg (Kgs)','Total Engg Weight Leg (Kgs)','Dry Operating Weight (Kgs)','Cockpit Crew Count','Cabin Crew Count','First Class Non Revenue Passenger','Business Class Non Revenue Passenger','Economy Class Non Revenue Passenger','Dom Intl Flag']
na_data_only.to_csv(Name_of_file + '_na_data_single.csv', index=False)
dup_with_na = pd.read_csv(Name_of_file + '_duplicate_data_with_na.csv', header=None)
dup_with_na.columns = ['Flight Number','Flight Departure Date', 'Aircraft Registration Number','Departure Airport Code','Arrival Airport Code','Aircraft Payload','Available Payload','Maximum Zero Fuel Weight (Kgs)','Actual Zero Fuel Weight (Kgs)','Take Off Fuel','Maximum Take Off Weight (Kgs)','Actual Take Off Weight (Kgs)','Trip Fuel Leg','Maximum Landing Weight (Kgs)','Actual Landing Weight (Kgs)','First Class Flown Passenger','Business Class Flown Passenger','Economy Class Flown Passenger','Total Male','Total Female','Total Children','Total Infants','Total Passenger Weight (Kgs)','Total Compartment Weight (Kgs)','Total Baggage Weight Leg (Kgs)','Total Cargo Weight Leg (Kgs)','Total Mail Weight Leg (Kgs)','Total Engg Weight Leg (Kgs)','Dry Operating Weight (Kgs)','Cockpit Crew Count','Cabin Crew Count','First Class Non Revenue Passenger','Business Class Non Revenue Passenger','Economy Class Non Revenue Passenger','Dom Intl Flag']
dup_with_na.to_csv(Name_of_file + '_duplicate_data_with_na.csv', index=False)
dup_without_na = pd.read_csv(Name_of_file + '_duplicate_data_without_na.csv', header=None)
dup_without_na.columns = ['Flight Number','Flight Departure Date', 'Aircraft Registration Number','Departure Airport Code','Arrival Airport Code','Aircraft Payload','Available Payload','Maximum Zero Fuel Weight (Kgs)','Actual Zero Fuel Weight (Kgs)','Take Off Fuel','Maximum Take Off Weight (Kgs)','Actual Take Off Weight (Kgs)','Trip Fuel Leg','Maximum Landing Weight (Kgs)','Actual Landing Weight (Kgs)','First Class Flown Passenger','Business Class Flown Passenger','Economy Class Flown Passenger','Total Male','Total Female','Total Children','Total Infants','Total Passenger Weight (Kgs)','Total Compartment Weight (Kgs)','Total Baggage Weight Leg (Kgs)','Total Cargo Weight Leg (Kgs)','Total Mail Weight Leg (Kgs)','Total Engg Weight Leg (Kgs)','Dry Operating Weight (Kgs)','Cockpit Crew Count','Cabin Crew Count','First Class Non Revenue Passenger','Business Class Non Revenue Passenger','Economy Class Non Revenue Passenger','Dom Intl Flag']
dup_without_na.to_csv(Name_of_file + "_duplicate_data_without_na.csv", index=False)

# here start the merging of duplicate data
print("\nHere starts the merge data")
h = 0
k = 0
f5 = open(Name_of_file + "_duplicate_data_with_na.csv", 'r')
f6 = open(Name_of_file + '_merge.csv', 'w')

c5 = csv.reader(f5)
c6 = csv.writer(f6)

file = list(c5)

for i in range(0, len(file)-1):
    h = h+1
    if((file[i][0:2] == file[i+1][0:2])):
        if file[i][3:5] == file[i+1][3:5]:
            file[i+1][15] = file[i][15]
            file[i+1][16] = file[i][16]
            file[i+1][17] = file[i][17]
            file[i+1][18] = file[i][18]
            file[i+1][19] = file[i][19]
            file[i+1][20] = file[i][20]
            file[i+1][21] = file[i][21]
            file[i+1][31] = file[i][31]
            file[i+1][32] = file[i][32]
            file[i+1][33] = file[i][33]
            res = file[i+1]
            c6.writerow(res)
            #print(res)
            k = k + 1
print(h, k)
print(i)
f5.close()
f6.close()

dup_merge_data = pd.read_csv(Name_of_file + '_merge.csv', header=None)
dup_merge_data.columns = ['Flight Number', 'Flight Departure Date', 'Aircraft Registration Number', 'Departure Airport Code', 'Arrival Airport Code', 'Aircraft Payload', 'Available Payload', 'Maximum Zero Fuel Weight (Kgs)', 'Actual Zero Fuel Weight (Kgs)', 'Take Off Fuel', 'Maximum Take Off Weight (Kgs)', 'Actual Take Off Weight (Kgs)', 'Trip Fuel Leg', 'Maximum Landing Weight (Kgs)', 'Actual Landing Weight (Kgs)', 'First Class Flown Passenger', 'Business Class Flown Passenger', 'Economy Class Flown Passenger', 'Total Male', 'Total Female', 'Total Children', 'Total Infants', 'Total Passenger Weight (Kgs)', 'Total Compartment Weight (Kgs)', 'Total Baggage Weight Leg (Kgs)', 'Total Cargo Weight Leg (Kgs)', 'Total Mail Weight Leg (Kgs)', 'Total Engg Weight Leg (Kgs)', 'Dry Operating Weight (Kgs)', 'Cockpit Crew Count', 'Cabin Crew Count', 'First Class Non Revenue Passenger', 'Business Class Non Revenue Passenger', 'Economy Class Non Revenue Passenger', 'Dom Intl Flag']
dup_merge_data.to_csv(Name_of_file + "_merge.csv", index=False)

# here start the prog for final file i.e file consist of only clean data without na and duplicates
flight_data = pd.read_csv(Name_of_file+'.csv')  # filght_data is the variable name used to store original file data values
com_data = flight_data[flight_data['Aircraft Registration Number'].notnull()]
com_data.to_csv(Name_of_file + '_notnull_data.csv', index=False)  #com_data is the variable name used to store notnull() data values
print("\nThis one is the desired output")
l = 0
m = 0

f7 = open(Name_of_file + '_notnull_data.csv', 'r')
f8 = open(Name_of_file + '_merge.csv', 'r')
f9 = open(Name_of_file + '_finalfile.csv', 'w')

c7 = csv.reader(f7)
c8 = csv.reader(f8)
c9 = csv.writer(f9)

file_1 = list(c7)
file_2 = list(c8)
for i in range(len(file_1)):
    l = l + 1
    for j in range(1, len(file_2)):
         if file_1[i][0:5] == file_2[j][0:5]:
            res = file_2[j]
           # print(res)
            c9.writerow(res)
            m = m + 1
    res_n = file_1[i]
    # print(res_n)
    c9.writerow(res_n)

print(l)
print(m)
f7.close()
f8.close()
f9.close()

output = pd.read_csv(Name_of_file + '_finalfile.csv')
output.drop_duplicates(subset=['Flight Number','Flight Departure Date','Aircraft Registration Number','Departure Airport Code','Arrival Airport Code','Dom Intl Flag'], inplace = True)
output.to_csv(Name_of_file + '_finalfile.csv', index=False)
