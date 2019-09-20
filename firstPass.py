import fitz
import os
import csv
import re
def FirstPassParse():
    files = ['Syllabi\\'+f for f in os.listdir('Syllabi') if os.path.isfile('Syllabi\\'+f)]
    matcher = re.compile(r'(\d{4}-\d{1,2}-\d{1,2})')
    outputList = []
    for f in files:
        if '.pdf' not in f:
            continue
        doc = fitz.open(f)
        outputList.append([f])
        vals = []
        for i in range(doc.pageCount):
            page = doc.loadPage(i)
            text = page.getText()
            lst = text.split('\n')
            index = 0
            for l in lst:
                j=matcher.search(l)
                if j:
                    concat = ' '.join(lst[index-2:index+1])
                    if concat and concat[-1] != '%':
                        concat = ' '.join(lst[index-1:index+2])
                    if ':' not in concat:
                        vals.append(concat)
                index+=1
        outputList.append(vals)
    return outputList