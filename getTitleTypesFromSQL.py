import sys
print(sys.executable)

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

# DESKTOP-7MPM8RT

def getTitleTypes():
    try:
        conn = odbc.connect(connection_string)
    except Exception as e:
        print(e)
        print('Task was terminated')
        sys.exit()
    finally:
        cursor = conn.cursor()

    select_distinct_statement = """
        SELECT [titleTypeID]
        ,[titleType]
        FROM [IMDB].[dbo].[TITLETYPES]
    """

    try:
        cursor.execute(select_distinct_statement)
    except Exception as e:
        cursor.rollback()
        print(e)
        print('Transaction rolled back')
    finally:
        global titletypes
        titletypes = dict()
        for row in cursor.fetchall():
            titletypes[str(row[1]).strip()] = row[0]
        print('titletypes fetched')
        cursor.close()
    conn.close()

getTitleTypes()

print("ran get titletypes from sql")

# print(titletypes)
# print(titletypes.get('short'))