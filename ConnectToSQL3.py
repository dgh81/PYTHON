# TODO
# TEST BULK INSERT
# SE REF I REGNEARK TIL SQL 

import sys
print(sys.executable)

# from Create_IMDB_Genres import records
import timeit
import pyodbc as odbc

# Kan gøres dynamisk, men tager 2341.4272347999795  seconds at køre fra hele datasættet data.tsv
# TODO: SKIFT NULL TIL None + SKIFT KOLONNEN genreName i GENRES TABELLEN I SQL TIL AT MODTAGE 'NULL'
records = {'Documentary': 1, 
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

DRIVER_NAME='SQL SERVER'
SERVER_NAME='DESKTOP-7MPM8RT'
DATABASE_NAME='IMDB'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

def SendRecordsToSQL():
    try:
        conn = odbc.connect(connection_string)
    except Exception as e:
        print(e)
        print('Task was terminated')
        sys.exit()
    else:
        cursor = conn.cursor()

    # TODO: UNDERSØG HVORDAN MAN SENDER ANDRE KOMMANDER, FX EXEC TIL SQL!

    insert_statement = """
        INSERT INTO GENRES
        VALUES(?, ?) 
    """
    try:
        for record in records:
            print(records[record], record)
            cursor.execute(insert_statement, records[record], record)
    except Exception as e:
        cursor.rollback()
        print(e)
        print('Transaction rolled back')
    else:
        print('Transaction inserted succesfully')
        cursor.commit()
        cursor.close()
    conn.close()

print('SendRecordsToSQL: ', timeit.timeit(SendRecordsToSQL, number=1), ' seconds')