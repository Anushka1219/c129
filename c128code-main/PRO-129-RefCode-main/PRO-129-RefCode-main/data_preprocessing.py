import csv
dataset1=[]
dataset2=[]

with open("final.csv","r") as f:
    csvreader=csv.reader(f) 
    for eachrow in csvreader:
        dataset1.append(eachrow)

with open("archive_dataset_sorted1.csv","r") as f:
    csvreader=csv.reader(f) 
    for eachrow in csvreader:
        dataset2.append(eachrow)

headers1=dataset1[0]
planetdata1=dataset1[1:]

headers2=dataset2[0]
planetdata2=dataset2[1:]

headers=headers1+headers2

planetdata=[]
for index, row in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])

with open("merge.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)     
