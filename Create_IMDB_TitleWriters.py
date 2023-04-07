import timeit
newRecord = []
records = []

def CreateTitleWriters():
    global records
    with open("title_crew_data_1.tsv", 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            print(i)
            line = lines[i].replace('\t','myDelimiter').replace(r'\N','NULL').replace('\n','').split('myDelimiter')
            writers = line[2].split(',')
            countWriters = len(writers)
            # print(directors)
            global newRecord
            for x in range(countWriters):
                primaryKey = line[0]
                newRecord.append(primaryKey)
                newRecord.append(writers[x])
                records.append(newRecord)
                # print(newRecord)
                newRecord = []

print('CreateTitleWritersRecords: ', timeit.timeit(CreateTitleWriters, number=1), ' seconds')

