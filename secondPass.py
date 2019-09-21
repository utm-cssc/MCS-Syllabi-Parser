import fitz
import os
import csv
import re
from pprint import pprint

def SecondPassParse(inputList):
    counter = 0
    masterList = []
    tempList = []
    #better date matching
    dateMatch = re.compile('([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))')
    for row in inputList:
        if row and '.pdf' in row[0]:
            masterList.append(tempList)
            tempList = []
            tempList.append(row[0].split('_')[1][0:6])
            continue
        for strings in row:
            if strings:
                #check if date in the index where the date should be
                result = dateMatch.search(strings[2]) or dateMatch.search(strings[1])
            if result:
                tempList.append(strings)
    
    masterList.append(tempList)
    with open('out.csv','w',newline='') as write:
        writer = csv.writer(write)
        currName = ''
        writer.writerow(['Type','Description', 'Date','Percentage','Course'])
        for i in masterList[1:]:
            currName = i[0]
            count = 0
            for c in i[1:]:
                if len(c) == 4:
                    writer.writerow(c+[currName])
                else:
                    writer.writerow([c[0],'NA',c[1],c[2],currName])
                count += 1
            if count == 0:
                writer.writerow(['N/A', 'Error','No items found',currName])
            writer.writerow([])