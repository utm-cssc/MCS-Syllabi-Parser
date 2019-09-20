import fitz
import os
import csv
import re
from pprint import pprint

def SecondPassParse(inputList):
    counter = 0
    masterList = []
    tempDct = {}
    pat = re.compile('([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))')
    percentRe = re.compile('(\d+(\.\d+)?%)')
    for i in inputList:
        if i and '.pdf' in i[0]:
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
                if perc:
                       tStr = tStr.replace(perc[0],'',1).strip()
                if tStr in tempDct:
                    if perc: 
                        tempDct[tStr].append((result[0],perc[0]))
                    else:
                        tempDct[tStr].append((result[0]))
                else:
                    if perc:
                        tempDct[tStr] = [(result[0],perc[0])]
                    else:
                        tempDct[tStr] = [(result[0])]
    masterList.append(tempDct.copy())
    print(len(masterList))
    write = open('out.csv','w',newline='')
    writer = csv.writer(write)
    currName = ''
    writer.writerow(['Date','Description', 'Percentage','Course'])
    for i in masterList[1:]:
        currName = i['name']
        count = 0
        for c in sorted(i.keys()):
            if c == 'name':
                continue
            for b in i[c]:
                if len(b) == 2:
                    writer.writerow([b[0],c,b[1],currName])
                else:
                    writer.writerow([b[0],c,'N/A',currName])
                count += 1
        if count == 0:
            writer.writerow(['N/A', 'Error','No items found',currName])
        writer.writerow([])
    write.close()