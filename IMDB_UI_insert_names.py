import sys
print(sys.executable)

# from Create_IMDB_Titles import records
# import timeit
import pyodbc as odbc
import tkinter  as tk 
from tkinter import * 
root = tk.Tk()
root.geometry("1280x500")

def main():

    DRIVER_NAME='SQL SERVER'
    SERVER_NAME='DESKTOP-7MPM8RT'
    DATABASE_NAME='IMDB'

    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
    """

    try:
        my_conn = odbc.connect(connection_string)
    except Exception as e:
        print(e)
        print('Task was terminated')
        sys.exit()
    finally:
        global cursor
        cursor = my_conn.cursor()

    label1 = Label(root, text="nconst", width=16)
    label1.grid(row=0, column=0)
    label2 = Label(root, text="primaryName", width=16)
    label2.grid(row=0, column=1)
    label3 = Label(root, text="birthYear", width=16)
    label3.grid(row=0, column=2)
    label4 = Label(root, text="deathYear", width=16)
    label4.grid(row=0, column=3)

    global nconst_field
    nconst_field = Entry(root, width=20, fg='blue')
    nconst_field.grid(row=1, column=0)

    global primaryName_field
    primaryName_field = Entry(root, width=20, fg='blue')
    primaryName_field.grid(row=1, column=1)

    global birthYear_field
    birthYear_field = Entry(root, width=20, fg='blue')
    birthYear_field.grid(row=1, column=2)

    global deathYear_field
    deathYear_field = Entry(root, width=20, fg='blue')
    deathYear_field.grid(row=1, column=3)

    empty = Label(root, text="", width=16)
    empty.grid(row=2, column=1)
    searchBtn = tk.Button(text='insert!', command=insert_new_name)
    searchBtn.grid(row=3, column=1)


def insert_new_name():
    print('running click')
    if nconst_field.get() != '' and primaryName_field.get() != '':
        nconst = nconst_field.get()
        pName = primaryName_field.get()

        if birthYear_field.get() == "":
            bYear = None
        else:
            bYear = birthYear_field.get()

        if deathYear_field.get() == "":
            dYear = None
        else:
            dYear = deathYear_field.get()

    name_values = nconst, pName, bYear, dYear
    insert_new_name_into_SQL(name_values)
    #OBS! list_of_selected_genres[g] giver genre tal til næste insert...

        
def insert_new_name_into_SQL(name_values):
    insert_statement = "INSERT INTO NAMES VALUES(?, ?, ?, ?)"
    try:
        cursor.execute(insert_statement, name_values)

    except Exception as e:
        cursor.rollback()
        print(e)
        print('Transaction rolled back')
    finally:
        print('Transaction inserted succesfully')
        cursor.commit()

main()
root.mainloop()

