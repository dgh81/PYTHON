import sys
print(sys.executable)

# from Create_IMDB_Titles import records
# import timeit
import pyodbc as odbc
import tkinter  as tk 
from tkinter import * 
root = tk.Tk()
root.geometry("1280x500")

global limit # TODO Store bogstaver til konstanter
limit = 10; # No of records to be shown per page.

isResultsCreated = False
oldSearchtext = ""

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



def my_display(offset, searchtext):    
    global isResultsCreated

    #TODO Skal kun køres een gang.... DONE!
    if not isResultsCreated:
        q = "EXEC search_names_procedure @searchtext = '" + searchtext + "'"
        cursor.execute(q)
        isResultsCreated = True
        q="SELECT count(*) FROM ##final_names_search_results"
        r_set=cursor.execute(q)
        data_row=r_set.fetchone()
        print(data_row)
        global no_rec
        no_rec=data_row[0] # Total number of rows in table
        print('no_rec:',no_rec)


    q="select * from ##final_names_search_results WHERE Number BETWEEN """ + str(offset) + " AND " + str(limit+offset-1)
    r_set=cursor.execute(q)

    i=2 # row value inside the loop
    # root.columnconfigure(tuple(range(8)), weight=1)
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=0)
    e.insert(END, 'Number')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=1) 
    e.insert(END, 'primaryName')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=2) 
    e.insert(END, 'birthYear')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=3) 
    e.insert(END, 'deathYear')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=4) 
    e.insert(END, 'professions')
    

    for record in r_set: 
        for j in range(len(record)):
            e = Entry(root, width=20, fg='blue') 
            e.grid(row=i, column=j)
            if str(record[j]) == 'None':
                r = ''
            else:
                r = str(record[j])
            e.insert(END, r)
        i=i+1

    while (i<limit+2): # required to blank the balance rows if they are less - skip first 2 rows for buttons and headings
        for j in range(len(record)):
            e = Entry(root, width=20, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, "")
        i=i+1

    # Show buttons 
    back = offset - limit # This value is used by Previous button
    next = offset + limit # This value is used by Next button       
    b1 = tk.Button(root, text='Next >', command=lambda: my_display(next, searchtext))
    b1.grid(row=12,column=2)
    b2 = tk.Button(root, text='< Prev', command=lambda: my_display(back, searchtext))
    b2.grid(row=12,column=1)

    if(no_rec <= (next-1)): 
        b1["state"]="disabled" # disable next button
    else:
        b1["state"]="active"  # enable next button
        
    if(back >= 0):
        b2["state"]="active"  # enable Prev button
    else:
        b2["state"]="disabled"# disable Prev button 

def test():
    print("test:")

def searchBtnEvent():
    global searchtext
    global oldSearchtext
    # print('oldSearchtext:',oldSearchtext== searchfield.get())
    if oldSearchtext == searchfield.get():
        global isResultsCreated
        isResultsCreated = True
        pass
    else:
        searchtext = searchfield.get()
        if searchtext != "":
            oldSearchtext = searchtext
            isResultsCreated = False
            #clean table from prev search
            for i in range(12):
                if i > 1:
                    for j in range(5):
                        e = Entry(root, width=20, fg='blue') 
                        e.grid(row=i, column=j) 
                        e.insert(END, "")
                        # print('i:',i,'j:',j)

            my_display(1, searchtext)


searchfield = Entry(root, width=20, fg='blue')
searchfield.grid(row=0, column=0)

searchBtn = tk.Button(text='search!', command=searchBtnEvent)
searchBtn.grid(row=0, column=1)

main()
root.mainloop()

