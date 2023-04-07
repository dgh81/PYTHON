import sys
print(sys.executable)

# from Create_IMDB_Titles import records
# import timeit
#from IMDB_UI_insert_movie import insert_new_movie_into_SQL

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
        q = "EXEC search_titles_procedure @searchtext = '" + searchtext + "'"
        cursor.execute(q)
        isResultsCreated = True
        q="SELECT count(*) FROM ##final_row_results"
        r_set=cursor.execute(q)
        data_row=r_set.fetchone()
        print(data_row)
        global no_rec
        no_rec=data_row[0] # Total number of rows in table
        print('no_rec:',no_rec)


    q="select * from ##final_row_results WHERE Number BETWEEN """ + str(offset) + " AND " + str(limit+offset-1)
    r_set=cursor.execute(q)

    i=2 # row value inside the loop

    e = Entry(root, width=20, fg='black')
    e.grid(row=1, column=0)
    e.insert(END, 'Number')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=1)
    e.insert(END, 'tconst')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=2) 
    e.insert(END, 'Genres')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=3) 
    e.insert(END, 'primaryTitle')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=4) 
    e.insert(END, 'originalTitle')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=5) 
    e.insert(END, 'startYear')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=6) 
    e.insert(END, 'endYear')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=7) 
    e.insert(END, 'isAdult')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=8) 
    e.insert(END, 'runtimeMinutes')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=1, column=9) 
    e.insert(END, 'titleType')

    for record in r_set: 
        for j in range(len(record)):
            e = Entry(root, width=20, fg='blue')
            e.bind('<Button-1>', lambda event, btn=e:test(btn))
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

    global new_number_var
    new_number_var = tk.StringVar()
    new_number_var.set("")
    global new_number
    new_number = Entry(root, width=20, fg='red', textvariable=new_number_var)
    new_number.grid(row=14, column=0)
    new_number.insert(END, '')
    e = Entry(root, width=20, fg='black')
    e.grid(row=13, column=0)
    e.insert(END, 'Number')

    global new_tconst_var
    new_tconst_var = tk.StringVar()
    new_tconst_var.set("")
    global new_tconst
    new_tconst = Entry(root, width=20, fg='red', textvariable=new_tconst_var)
    new_tconst.grid(row=14, column=1)
    new_tconst.insert(END, '')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=13, column=1)
    e.insert(END, 'tconst')
    
    global new_genres_var
    new_genres_var = tk.StringVar()
    new_genres_var.set("")
    global new_genres
    new_genres = Entry(root, width=20, fg='red', textvariable=new_genres_var)
    new_genres.grid(row=14, column=2)
    new_genres.insert(END, '')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=13, column=2) 
    e.insert(END, 'Genres')

    global new_priTitle_var
    new_priTitle_var = tk.StringVar()
    new_priTitle_var.set("")
    global new_priTitle
    new_priTitle = Entry(root, width=20, fg='red', textvariable=new_priTitle_var)
    new_priTitle.grid(row=14, column=3)
    new_priTitle.insert(END, '')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=13, column=3) 
    e.insert(END, 'primaryTitle')

    global new_oriTitle_var
    new_oriTitle_var = tk.StringVar()
    new_oriTitle_var.set("")
    global new_oriTitle
    new_oriTitle = Entry(root, width=20, fg='red', textvariable=new_oriTitle_var)
    new_oriTitle.grid(row=14, column=4)
    new_oriTitle.insert(END, '')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=13, column=4) 
    e.insert(END, 'originalTitle')

    global new_startY_var
    new_startY_var = tk.StringVar()
    new_startY_var.set("")
    global new_startY
    new_startY = Entry(root, width=20, fg='red', textvariable=new_startY_var)
    new_startY.grid(row=14, column=5)
    new_startY.insert(END, '')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=13, column=5) 
    e.insert(END, 'startYear')

    global new_endY_var
    new_endY_var = tk.StringVar()
    new_endY_var.set("")
    global new_endY
    new_endY = Entry(root, width=20, fg='red', textvariable=new_endY_var)
    new_endY.grid(row=14, column=6)
    new_endY.insert(END, '')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=13, column=6) 
    e.insert(END, 'endYear')

    global new_isA_var
    new_isA_var = tk.StringVar()
    new_isA_var.set("")
    global new_isA
    new_isA = Entry(root, width=20, fg='red', textvariable=new_isA_var)
    new_isA.grid(row=14, column=7)
    new_isA.insert(END, '')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=13, column=7) 
    e.insert(END, 'isAdult')

    global new_runtime_var
    new_runtime_var = tk.StringVar()
    new_runtime_var.set("")
    global new_runtime
    new_runtime = Entry(root, width=20, fg='red', textvariable=new_runtime_var)
    new_runtime.grid(row=14, column=8)
    new_runtime.insert(END, '')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=13, column=8) 
    e.insert(END, 'runtimeMinutes')

    global new_titleType_var
    new_titleType_var = tk.StringVar()
    new_titleType_var.set("")
    global new_titleType
    new_titleType = Entry(root, width=20, fg='red', textvariable=new_titleType_var)
    new_titleType.grid(row=14, column=9)
    new_titleType.insert(END, '')
    e = Entry(root, width=20, fg='black') 
    e.grid(row=13, column=9) 
    e.insert(END, 'titleType')

# TODO Rename!
def test(btn):

    tconst=btn.get()
    global selected_movie
    selected_movie = []
    if tconst[:2]=="tt":
        record = cursor.execute("SELECT * FROM ##final_row_results WHERE tconst = '" + tconst + "'")
        i = 0
        for rec in record:
            for j in range(len(rec)):
                if j == 0:
                    new_number_var.set(rec[0])
                if j == 1:
                    new_tconst_var.set(rec[1])
                if j == 2:
                    new_genres_var.set(rec[2])
                if j == 3:
                    new_priTitle_var.set(rec[3])
                if j == 4:
                    new_oriTitle_var.set(rec[4])
                if j == 5:
                    new_startY_var.set(rec[5])
                if j == 6:
                    new_endY_var.set(rec[6])
                if j == 7:
                    new_isA_var.set(rec[7])
                if j == 8:
                    new_runtime_var.set(rec[8])
                if j == 9:
                    new_titleType_var.set(rec[9])
                i += 1
    

    updateBtn = tk.Button(root, text='Update', command=lambda: update_movie())
    updateBtn.grid(row=15,column=1)
    deleteBtn = tk.Button(root, text='Delete', command=lambda: delete_movie())
    deleteBtn.grid(row=15,column=2)

def delete_movie():
    delete_statement = "DELETE FROM TITLES WHERE tconst = '" + new_tconst.get() + "'"
    try:
        cursor.execute(delete_statement)
    except Exception as e:
        cursor.rollback()
        print(e)
        print('Transaction rolled back')
    finally:
        print('Records deleted succesfully')
        cursor.commit()
    delete_genrestitles_in_SQL(new_tconst.get())

def update_movie():

    genre_list = cursor.execute("SELECT * FROM GENRES ORDER BY ID")
    genres = str(new_genres.get()).split(',')
    print('genres:',genres)
    for i,g in enumerate(genres):
        genres[i] = genres[i].strip().capitalize()

    genreID_list = []
    for genre in genre_list:
        for g in genres:
            g = g.strip()
            if g == genre[1]:
                genreID_list.append(genre[0])

    delete_genrestitles_in_SQL(new_tconst.get())

    print('genreID_list:', genreID_list)
    for i in range(len(genreID_list)):
        values = []
        values.append(new_tconst.get())
        values.append(genreID_list[i])
        print(values)
        create_genrestitles_in_SQL(values)

        #TODO Delete og insert GENRESTITLES: PS values her fejler vist ikke noget...
        # insert_new_genrestitles_into_SQL(values)

    values = [new_tconst.get(), new_titleType.get().strip(), new_priTitle.get(), new_oriTitle.get(), new_isA.get(),
        new_startY.get(), new_endY.get(), new_runtime.get(), ",".join(genres)]
    print(values)

    update_movie_in_SQL(values)

def update_movie_in_SQL(movie_values):
    #TODO: Mangler at implementere titletype ved ændring! (Eller?)
    #TODO: Husk at fjerne genres hvis de fjernes fraetabellen i SQL...
    
    for i,val in enumerate(movie_values):
        if val == '':
            movie_values[i] = 'NULL'

    update_statement = "UPDATE TITLES SET primaryTitle = '" + str(movie_values[2]) + "'," + """
    originalTitle = '""" + str(movie_values[3]) + "'," + """
    isAdult = """ + movie_values[4] + "," + """
    startYear = """ + movie_values[5] + "," + """
    endYear = """ + movie_values[6] + "," + """
    runtimeMinutes = """ + movie_values[7] + """
    WHERE tconst = '""" + str(movie_values[0]) + "'"
    
    print('update_statement',update_statement)
    try:
        cursor.execute(update_statement)

    except Exception as e:
        cursor.rollback()
        print(e)
        print('Transaction rolled back')
    finally:
        print('Transaction inserted succesfully')
        cursor.commit()


def delete_genrestitles_in_SQL(tconst):
    delete_statement = "DELETE FROM GENRESTITLES WHERE tconst = '" + tconst + "'"
    try:
        cursor.execute(delete_statement)
    except Exception as e:
        cursor.rollback()
        print(e)
        print('Transaction rolled back')
    finally:
        print('Records deleted succesfully')
        cursor.commit()

def create_genrestitles_in_SQL(values):
    insert_statement = "INSERT INTO GENRESTITLES VALUES(?, ?)"
    try:
        cursor.execute(insert_statement, values)
    except Exception as e:
        cursor.rollback()
        print(e)
        print('Transaction rolled back')
    finally:
        print('Transaction inserted succesfully')
        cursor.commit()

def searchBtnEvent():
    global searchtext
    global oldSearchtext
    if oldSearchtext == searchfield.get():
        global isResultsCreated
        isResultsCreated = True
        pass # :D
    else:
        searchtext = searchfield.get()
        if searchtext != "":
            oldSearchtext = searchtext
            isResultsCreated = False
            #clean table from prev search
            for i in range(12):
                if i > 1:
                    for j in range(9):
                        e = Entry(root, width=20, fg='blue') 
                        e.grid(row=i, column=j) 
                        e.insert(END, "")

            my_display(1, searchtext)


searchfield = Entry(root, width=20, fg='blue')
searchfield.grid(row=0, column=0)

searchBtn = tk.Button(text='search!', command=searchBtnEvent)
searchBtn.grid(row=0, column=1)

main()
root.mainloop()

