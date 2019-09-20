import fitz
import os
import csv
import re
outFile = open('log','w',newline='')
writer = csv.writer(outFile)
files = [f for f in os.listdir('.') if os.path.isfile(f)]
matcher = re.compile(r'(\d{4}-\d{1,2}-\d{1,2})')
for f in files:
    print(f)
    if '.pdf' not in f:
        continue
    doc = fitz.open(f)
    writer.writerow([f])
    vals = []
    for i in range(doc.pageCount):
        page = doc.loadPage(i)
        text = page.getText()
        lst = text.split('\n')
        index = 0
        for l in lst:
            j=matcher.search(l)
            if j:
                vals.append(' '.join(lst[index-2:index+1]))
            index+=1
    writer.writerow(vals)
outFile.close()