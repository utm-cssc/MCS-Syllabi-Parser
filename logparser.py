import fitz
import os
import csv
import re
from pprint import pprint
outFile = open('log','r',newline='')
reader = list(csv.reader(outFile))
outFile.close()
counter = 0
masterList = []
tempDct = {}
pat = re.compile('([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))')
percentRe = re.compile('(\d+(\.\d+)?%)')
for i in reader:
    if i and '.pdf' in i[0]:
        #print(i[0])
        masterList.append(tempDct.copy())
        tempDct = {}
        tempDct['name'] = i[0].split('_')[1][0:6]
        continue
    
    for string in i:
        result = pat.search(string)
        if result:
            tStr = string
            res = result[0]
            if 'Assignment Assignment' in tStr:
                tStr = tStr.replace('Assignment Assignment', 'Assignment',1)
            elif 'Quiz Quiz' in tStr:
                tStr = tStr.replace('Quiz Quiz', 'Quiz',1)
            elif 'Term Test Term Test' in tStr:
                tStr = tStr.replace('Term Test Term Test', 'Term Test',1)
            elif "Assignment Homework assignment" in tStr:
                tStr = tStr.replace('Assignment Homework assignment', 'Assignment',1)
            elif "Assignment Problem Set" in tStr:
                tStr = tStr.replace('Assignment Problem Set', 'Assignment',1)
            
            tStr = tStr.replace(res,'',1).strip()            
            perc = percentRe.search(string)
            #print(perc)
            if perc:
                tStr = tStr.replace(perc[0],'',1).strip()
            if tStr in tempDct:
                tempDct[tStr].append(result[0])
            else:
                tempDct[tStr] = [result[0]]
        #print(result)
pprint(masterList)
print(len(masterList))
write = open('out.csv','w',newline='')
writer = csv.writer(write)
currName = ''
for i in masterList[1:]:
    #writer.writerow(['name',i['name']])
    currName = i['name']
    for c in sorted(i.keys()):
        if c == 'name':
            continue
        for b in i[c]:
            writer.writerow([b,c,currName])
    writer.writerow([])
write.close()