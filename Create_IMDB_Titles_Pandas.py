import timeit
import numpy as np
import pandas as pd
import memory_profiler as mem_profile # pip install mem_profile

# Kun kolonne 1:
# data = pd.read_csv('data_6.tsv', sep='[\t]', usecols=[0], engine='python', nrows=20)

# MEM:
print('Memory before: ',mem_profile.memory_usage(), 'MB')

records = []
# Hvorfor bruger denne ca 15 MB mere end CreateRecords ?
def create_records():
# Bemærk header=None:
    # dataFrame = pd.read_csv('data_6.tsv', sep='[\t]', header=None, engine='python', nrows=20)
    dataFrame = pd.read_csv('data_6.tsv', sep='[\t]', header=None, engine='python')
    # print(dataFrame.loc[0][0])
    # TODO: MANGLER AT TAGE HØJDE FOR OM DER ER 9 FELTER I EN RECORD
    # print(len(dataFrame.index))
    for i in range(len(dataFrame.index)):
        record = []
        for x in dataFrame.loc[i]: # For 1 til 9
            try:            
                record.append(np.int64(x))
                continue
            except:
                if str(x) == r'\N':
                    x = None
                record.append(x)

        global records
        records.append(record)
        # data.append(dataFrame.loc[0][i])


# create_records()
label = '{}{}'.format('create_records (Using Pandas read_csv()):', '\t')
# print(label, timeit.timeit(create_records, number=1), ' seconds')
# print(records)

# --------------------------OLD VERSION--------------------------------------------------------------------------------:
records2 = []
def CreateRecords():
    global records2
    with open("data_6.tsv", 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            # print(i)
            line = lines[i].replace('\t','myDelimiter').replace(r'\N','NULL').replace('\n','').split('myDelimiter')
            myLine = []
            if len(line) == 9:
                for field in line:
                    try:
                        newField = np.int(field) # numpy int type ellers fejler: # tt21914118 titles: 9223372036854775807,  569936821221962380720
                        myLine.append(newField)
                    except:
                        if field == 'NULL':
                            newField = None
                            myLine.append(newField)
                        else:
                            # print('except else: ' + str(field))
                            myLine.append(field)

                records2.append(myLine)

label = '{}{}{}'.format('CreateRecords (Using normal open()):', '\t', '\t')
print(label, timeit.timeit(CreateRecords, number=1), ' seconds')
# MEM:
print('Memory before: ',mem_profile.memory_usage(), 'MB')
# print(records)
# --------------------------OLD VERSION--------------------------------------------------------------------------------: