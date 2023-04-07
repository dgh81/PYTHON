import timeit
import numpy as np
from getTitleTypesFromSQL import titletypes

records = []
def CreateRecords():
    global records
    with open("data_1.tsv", 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            # print(i)
            line = lines[i].replace('\t','myDelimiter').replace(r'\N','NULL').replace('\n','').split('myDelimiter')
            myLine = []
            if len(line) == 9:
                for index,field in enumerate(line):
                    try:
                        newField = np.int(field) # numpy int type ellers fejler: # tt21914118 titles: 9223372036854775807,  569936821221962380720
                        myLine.append(newField)
                    except:
                        if field == 'NULL':
                            field = None
                            myLine.append(field)
                        else:
                            # print(index)
                            if index == 1:
                                newField = titletypes.get(field)
                                myLine.append(newField)
                            else:
                                myLine.append(field)

                records.append(myLine)
            # print(records)
print('CreateRecords: ', timeit.timeit(CreateRecords, number=1), ' seconds')
