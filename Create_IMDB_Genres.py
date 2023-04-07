import timeit

# TODO:
# OMDØB ALLE CREATE_IMDB FUNKTIONER TIL NOGET MED RECORDS
# LAV GENERISK FUNKTION I STEDET FOR CONNECTTOSQL1, 2, 3, etc... (KRÆVER ÆNDRING I ConnectToSQL3 FRA DICT TIL LIST)
# LAGR NULL SOM None

records = []

def CreateGenreRecords():
    global records
    with open("data.tsv", 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            print(i)
            line = lines[i].replace('\t','myDelimiter').replace(r'\N','NULL').replace('\n','').split('myDelimiter')
            if len(line) == 9:
                genres = line[8].split(',')
                for genre in genres:
                    if genre not in records:
                        records.append(genre)
                    # TODO:
                    # Tæl antal genre
                        # Ny fil? - kan være næsten magen til denne i struktur/logik:
                            # træk unik liste af genre fra data.tsv
                            # konverter genre til tal
                    # loop for hver genre og skab record med pågældende tal

print('CreateGenreRecords: ', timeit.timeit(CreateGenreRecords, number=1), ' seconds')
# CreateGenreRecords()
print('records: ',records)

# CreateGenreRecords:  2341.4272347999795  seconds
# records:  ['Documentary', 'Short', 'Animation', 
#           'Comedy', 'Romance', 'Sport', 
#           'News', 'Drama', 'Fantasy', 
#           'Horror', 'Biography', 'Music', 
#           'War', 'Crime', 'Western', 
#           'Family', 'Adventure', 'Action', 
#           'History', 'Mystery', 'NULL', 
#           'Sci-Fi', 'Musical', 'Thriller', 
#           'Film-Noir', 'Talk-Show', 'Game-Show', 
#           'Reality-TV', 'Adult', 'Experimental']