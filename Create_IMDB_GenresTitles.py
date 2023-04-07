import timeit
# import numpy as np
newRecord = []
records = []
genreIndex = {'Documentary': 1, 
'Short': 2,
'Animation': 3,
'Comedy': 4,
'Romance': 5,
'Sport': 6,
'News': 7,
'Drama': 8,
'Fantasy': 9,
'Horror': 10,
'Biography': 11,
'Music': 12,
'War': 13,
'Crime': 14,
'Western': 15,
'Family': 16,
'Adventure': 17,
'Action': 18,
'History': 19,
'Mystery': 20,
'NULL': 21,
'Sci-Fi': 22,
'Musical': 23,
'Thriller': 24,
'Film-Noir': 25,
'Talk-Show': 26,
'Game-Show': 27,
'Reality-TV': 28,
'Adult': 29,
'Experimental': 30}

# TODO: OMDØB i, x, y TIL BEDRE NAVNE
y = 1
def CreateGenresTitlesRecords():
    global records
    with open("data_1.tsv", 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            # print(i)
            line = lines[i].replace('\t','myDelimiter').replace(r'\N','NULL').replace('\n','').split('myDelimiter')
            if len(line) == 9:
                genres = line[8].split(',')
                countGenres = len(genres)
                global newRecord
                for x in range(countGenres):
                    # global y
                    # newRecord.append(y)
                    primaryKey = line[0]
                    newRecord.append(primaryKey)
                    # newRecord.append(genres[x])
                    newRecord.append(genreIndex[genres[x]])
                    records.append(newRecord)
                    print(newRecord)
                    newRecord = []
                    # y += 1

print('CreateGenresTitlesRecords: ', timeit.timeit(CreateGenresTitlesRecords, number=1), ' seconds')
# CreateGenresTitlesRecords()
# print('records: ',records)

# ALT DATA FRA DATA.TSV:
# CreateGenresTitlesRecords:  1544.7346382999967  seconds (26 min)
