import sys
print(sys.executable)

from Create_IMDB_TitleWriters import records
import timeit
import pyodbc as odbc

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

    insert_statement = """
        INSERT INTO TITLEWRITERS
        VALUES(?, ?) 
    """

    try:
        for record in records:
            cursor.execute(insert_statement, record)
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

# CreateTitleWritersRecords:  152.0062475000159  seconds for 1 mio records
# SendRecordsToSQL:  282.4388203000417  seconds for 1 mio records