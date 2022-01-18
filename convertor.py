import os
import sys
import subprocess
import pkg_resources

#main process
def processRunner():
	import pandas as pd
	import csv
	from pathlib import Path
	print("enter json file path: ")	
	pdObj = pd.read_json(input())
	print("deleting json['Report Type'] ")
	del pdObj['Report Type']
	print(" enter dummy sheet csv: ")
	vv=input()
	data_file = open(vv, 'w',newline='')
	csv_writer = csv.writer(data_file)
	list1=[]
	list2=[]
	list3=[]
	for i in pdObj:
		for j in pdObj[i]:
			try:
				for k,l in j.items():
					list1.append(k)
					list3.append(i)
					list2.append(l)
			except:
				pass
	for w in range(len(list1)):
		csv_writer.writerow([list1[w],str(','.join(list2[w])),list3[w]])
	print("file is saved at "+vv)
	data_file.close()
	return 0
	

#checking for suitable packages to run the script
print("Checking for package_resources"+"."*60)
required = {'pandas', 'python-csv', 'pathlib'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
if missing:
	print(" "*50)
	print("Found missing packages"+"."*60)
	print("installing packages"+"."*60)
	os.system("pip3 install pandas")
	os.system("pip3 install python-csv")
	os.system("pip install pathlib")
	print(" ")
	print("packages are installed"+"."*60)
	print("running script")
	print("type exit to stop execution else type continue:")
	ki=input()
	a="exit"
	if(ki==str(a)):
		os.system("exit")
	else:
		processRunner()
else:
	print("packages satisfied")
	print("running script")
	print("type exit to stop execution or else type enter [continue/exit]")
	ki=input()
	if(ki=="exit"):
		os.system("exit")
	else:
		processRunner()





