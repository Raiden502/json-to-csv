import pandas as pd
import csv
import os

path = input("Enter folder path name: (ex: C:\\Users\\aravind\\Downloads\\Folder_name): ")
vv = input("enter csv file name: ")
data_file = open(vv+".csv", 'w', newline='')
csv_writer = csv.writer(data_file)
csv_writer.writerow(["accX", "accY", "accZ"])
for filename in os.listdir(path):
    pdObj = pd.read_json(path+"\\"+filename)
    a = pdObj["payload"]
    c = a["values"]
    for i in c:
        csv_writer.writerow([i[0], i[1], i[2]])
print(vv + ".csv" + " is created at "+path + "\\" + vv+ ".csv")
data_file.close()



