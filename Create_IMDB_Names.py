import timeit
newRecord = []
records = []

def CreateNames():
    global records
    with open("name_basics_data_13.tsv", 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            # print(i)
            line = lines[i].replace('\t','myDelimiter').replace(r'\N','NULL').replace('\n','').split('myDelimiter')
            global newRecord
            primaryKey = line[0]
            newRecord.append(primaryKey)
            newRecord.append(line[1])
            newRecord.append(line[2])
            newRecord.append(line[3])
            records.append(newRecord)
            # print(newRecord)
            newRecord = []

print('CreateNamesRecords: ', timeit.timeit(CreateNames, number=1), ' seconds')

