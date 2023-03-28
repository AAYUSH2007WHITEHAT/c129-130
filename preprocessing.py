import csv
data1 = []
data2 = []
with open("final.csv", "r") as f:
 csvreader = csv.reader(f)
for row in csvreader:
        data1.append(row)

with open("archive_sorted1.csv", "r") as f:
 csvreader = csv.reader(f)
for row in csvreader:
        data2.append(row)
header1=data1[0]
stardata1= data1[1:]        

header2=data2[0]
stardata2= data2[1:]
headers=header1+header2
star_data=[]
for index, data_row in enumerate(stardata1):
    star_data.append(stardata1[index]+stardata2[index])
    
with open ("merged_dataset.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)    
