# MEM:
import memory_profiler as mem_profile # pip install mem_profile
print('Memory before: ',mem_profile.memory_usage(), 'MB')

import sys
print(sys.executable)

from Create_IMDB_Names import records
import timeit
import pyodbc as odbc
import bcolors




DRIVER_NAME='SQL SERVER'
SERVER_NAME='DESKTOP-7MPM8RT'
DATABASE_NAME='IMDB'

    # Put dem her ned i connection_string hvis de skal bruges (bruges ikke ved local server...):
    # Uid=<username>;
    # Pwd=<password>;

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

# DESKTOP-7MPM8RT

def SendRecordsToSQL():
    try:
        conn = odbc.connect(connection_string)
    except Exception as e:
        print(e)
        print('Task was terminated')
        sys.exit()
    finally:
        cursor = conn.cursor()

    insert_statement = """
        INSERT INTO NAMES
        VALUES(?, ?, ?, ?) 
    """

    try:
        for record in records:
            cursor.execute(insert_statement, record)
    except Exception as e:
        cursor.rollback()
        print(e)
        print(bcolors.bcolors.FAIL + "Failed: Transaction rolled back" + bcolors.bcolors.ENDC)
        # print('Transaction rolled back')
    finally:
        print(bcolors.bcolors.OKGREEN + 'Transaction inserted succesfully' + bcolors.bcolors.ENDC)
        cursor.commit()
        cursor.close() # kun close hvis der ikke skal laves andet, hold åben hvis der skal hentes eller insættes mere...
    conn.close()

print('SendRecordsToSQL: ', timeit.timeit(SendRecordsToSQL, number=1), ' seconds')
print('Memory after: ',mem_profile.memory_usage(), 'MB')