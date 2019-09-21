import fitz
import os
import csv
import re
def FirstPassParse():
    files = ['Syllabi\\'+f for f in os.listdir('Syllabi') if os.path.isfile('Syllabi\\'+f)]

    matchDates = re.compile(r'(\d{4}-\d{1,2}-\d{1,2})')
    outputList = []
    for filename in files:
        if '.pdf' not in filename:
            continue
        document = fitz.open(filename)
        outputList.append([filename])
        vals = []
        for pagenum in range(document.pageCount):
            page = document.loadPage(pagenum)
            text = page.getText().replace(',','')
            allText = text.split('\n')
            index = 0
            for line in allText:
                match=matchDates.search(line)
                if match:
                    if ':' in line:
                        continue
                    #window to get assignment type, assignment description, assignment date, assignment value
                    concat = allText[index-2:index+2]
                    #some profs skip the description, in which case our window will be off by one
                    if not concat:
                        concat = allText[index-1:index+2]
                    ts = ''.join(concat)
                    if concat and (ts.count('%') > 1 or 'Weight' in ts):
                        concat = allText[index-1:index+2]
                    vals.append(concat)
                index+=1
        outputList.append(vals)
    return outputList