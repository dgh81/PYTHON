# MEM:
# import memory_profiler as mem_profile # pip install mem_profile
# print('Memory before: ',mem_profile.memory_usage(), 'MB')

import sys
print(sys.executable)

import timeit
import pyodbc as odbc

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

    select_statement = "SELECT * FROM TITLESBULK"

    try:
        cursor.execute(select_statement)
        records = cursor.fetchall()
        # print('records:',records)
        # for row in records:
        #     print("row:",row[0])
    except Exception as e:
        print(e)
    finally:
        print('Succesfully selected all records')
        cursor.commit()
        cursor.close() # kun close hvis der ikke skal laves andet, hold åben hvis der skal hentes eller insættes mere...
    conn.close()


print('SendRecordsToSQL: ', timeit.timeit(SendRecordsToSQL, number=1), ' seconds')
# print('done')
# print('Memory after: ',mem_profile.memory_usage(), 'MB')