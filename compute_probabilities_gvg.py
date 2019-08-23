# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 23:00:23 2018

@author: Sravani1
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:15:37 2018

@author: Sravani1
"""

from pathlib import Path


years=["2008","2009","2010","2011","2012","2013","2014","2015"]
csv_files=[]
for i in range(1,60):
    for year in years:
        name="ipl_"+year+"match"+str(i)+".csv"
        if Path(name).exists():
            csv_files.append(name)

print(csv_files)

info=dict()

#getting to the form: (Batsman,Bowler):[0s,1s,2s...]
for file in csv_files:
    f=open(file,"r")
    f.readline()
    for line in f:
        line=line.split(',')
        combo=line[:2]
        combo=tuple(combo)
        if combo not in info.keys():
            #0s 1s 2s 3s 4s 6s Dismissal Balls
            new = [int(i) for i in line[2:9]+line[10:11]]
            info[(combo)]=new
        else:
            existing_list=info[(combo)]
            new_list=line[2:9]+line[10:11]
            new_list = [int(i) for i in new_list]
            info[(combo)] = [x + y for x, y in zip(existing_list, new_list)]


# computing probability
            
for key in info.keys():
    existing_list=info[key]
    new_list=[i/(existing_list[7]) for i in existing_list[0:6]]+existing_list[6:7]
    new_list=[round(i,4) for i in new_list]
    info[key]=new_list

print(info)

data=[]

#List of lists for writing into the csvs

for key in info.keys():
    a=[]
    pair=key
    a.append(pair[0])
    a.append(pair[1])
    for val in info[key]:
        a.append(val)
    data.append(a)
    
    
    
import csv
 
 
myFile = open('2_GvG_probabilities.csv', 'w')
with myFile:
    writer = csv.writer(myFile,lineterminator = '\n')
    writer.writerows(data)