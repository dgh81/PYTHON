import timeit
newRecord = []
records = []

def CreateTitleDirectors():
    global records
    with open("title_crew_data_1.tsv", 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            print(i)
            line = lines[i].replace('\t','myDelimiter').replace(r'\N','NULL').replace('\n','').split('myDelimiter')
            directors = line[1].split(',')
            countDirectors = len(directors)
            # print(directors)
            global newRecord
            for x in range(countDirectors):
                primaryKey = line[0]
                newRecord.append(primaryKey)
                newRecord.append(directors[x])
                # newRecord.append(line[2])
                records.append(newRecord)
                # print(newRecord)
                newRecord = []

print('CreateTitleDirectorsRecords: ', timeit.timeit(CreateTitleDirectors, number=1), ' seconds')

