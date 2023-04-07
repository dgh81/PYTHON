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

    global genres_selection
    genres_selection = []
    q="SELECT * FROM GENRES ORDER BY ID"
    r_set=cursor.execute(q)
    for r in r_set:
        genres_selection.append(r[1])


    global titletypes_selection
    titletypes_selection = []
    q="SELECT * FROM TITLETYPES ORDER BY titleTypeID"
    r_set=cursor.execute(q)

    for r in r_set:
        titletypes_selection.append(str(r[1]).strip())

    global titletypes_variable
    titletypes_variable = StringVar(root)
    titletypes_variable.set(titletypes_selection[0]) # default value
    global titleType_field
    titleType_field = OptionMenu(root, titletypes_variable, *titletypes_selection, command=setOption1)
    titleType_field.grid(row=1, column=1)

    global isadult_variable
    isadult_variable = StringVar(root)
    isadult_variable.set('No') # default value
    global isAdult_field
    isAdult_field= OptionMenu(root, isadult_variable, 'No', 'Yes', command=setOption2)
    isAdult_field.grid(row=1, column=4)    



    label1 = Label(root, text="tconst", width=16)
    label1.grid(row=0, column=0)
    label2 = Label(root, text="titleType", width=16)
    label2.grid(row=0, column=1)
    label3 = Label(root, text="primaryTitle", width=16)
    label3.grid(row=0, column=2)
    label4 = Label(root, text="originalTitle", width=16)
    label4.grid(row=0, column=3)
    label5 = Label(root, text="isAdult", width=16)
    label5.grid(row=0, column=4)
    label6 = Label(root, text="startYear", width=16)
    label6.grid(row=0, column=5)
    label7 = Label(root, text="endYear", width=16)
    label7.grid(row=0, column=6)
    label8 = Label(root, text="runtimeMinutes", width=16)
    label8.grid(row=0, column=7)
    label9 = Label(root, text="genres", width=16)
    label9.grid(row=0, column=8)

    global tconst_field
    tconst_field = Entry(root, width=20, fg='blue')
    tconst_field.grid(row=1, column=0)

    # titleType_field = Entry(root, width=20, fg='blue')
    # titleType_field.grid(row=1, column=1)

    global primaryTitle_field
    primaryTitle_field = Entry(root, width=20, fg='blue')
    primaryTitle_field.grid(row=1, column=2)

    global originalTitle_field
    originalTitle_field = Entry(root, width=20, fg='blue')
    originalTitle_field.grid(row=1, column=3)

    # isAdult_field = Entry(root, width=20, fg='blue')
    # isAdult_field.grid(row=1, column=4)

    global startYear_field
    startYear_field = Entry(root, width=20, fg='blue')
    startYear_field.grid(row=1, column=5)

    global endYear_field
    endYear_field = Entry(root, width=20, fg='blue')
    endYear_field.grid(row=1, column=6)

    global runtimeMinutes_field
    runtimeMinutes_field = Entry(root, width=20, fg='blue')
    runtimeMinutes_field.grid(row=1, column=7)

    global genres_field
    genres_field = Entry(root, width=20, fg='blue')
    genres_field.grid(row=1, column=8)

    empty = Label(root, text="", width=16)
    empty.grid(row=3, column=1)
    searchBtn = tk.Button(text='insert!', command=insert_new_movie)
    searchBtn.grid(row=4, column=1)
# def my_display(offset, searchtext):    

def setOption1(selection):
    print(titletypes_variable.get())
    pass

def setOption2(selection):
    print(isadult_variable.get())
    pass

def insert_new_movie():
    print('running click')
    if tconst_field.get() != '' and primaryTitle_field.get() != '':
        tconst = tconst_field.get()
        pTitle = primaryTitle_field.get()

        if originalTitle_field.get() == "":
            orgTitle = None
        else:
            orgTitle = originalTitle_field.get()

        if startYear_field.get() == "":
            strtYear = None
        else:
            strtYear = startYear_field.get()

        if endYear_field.get() == "":
            ndYear = None
        else:
            ndYear = endYear_field.get()

        if runtimeMinutes_field.get() == "":
            rnTm = None
        else:
            rnTm = runtimeMinutes_field.get()

        if len(genres_field.get()) == 0:
            grn = None
        else:
            grn = getGenres()
            print(grn)

    #TODO inkluder i validation stmt ovenfor - ELLER SKIP AL VALIDATION IKKE EN DEL AF OPGAVEN !!!!!!!!!!!!
    #TODO evt put de mere komplekse fra nedenstående linje op sammen de andre ovenfor. Så en var bare er sat til linjen herunder..
    
    #TODO Lav begge prints til sql's og execute...:
    print(tconst, titletypes_selection.index(titletypes_variable.get().strip())+1, pTitle, orgTitle, isAdult(isadult_variable.get()), strtYear, ndYear, rnTm, genres_field.get().capitalize())
    movie_values = tconst, titletypes_selection.index(titletypes_variable.get().strip())+1, pTitle, orgTitle, isAdult(isadult_variable.get()), strtYear, ndYear, rnTm #, genres_field.get().capitalize()
    insert_new_movie_into_SQL(movie_values)
    #OBS! list_of_selected_genres[g] giver genre tal til næste insert...
    for g in range(len(getGenres())):
        print(tconst, list_of_selected_genres[g])
        genrestitles_values = tconst, list_of_selected_genres[g]
        insert_new_genrestitles_into_SQL(genrestitles_values)

        
def insert_new_movie_into_SQL(movie_values):
    insert_statement = "INSERT INTO TITLES VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
    try:
        cursor.execute(insert_statement, movie_values)

    except Exception as e:
        cursor.rollback()
        print(e)
        print('Transaction rolled back')
    finally:
        print('Transaction inserted succesfully')
        cursor.commit()

def insert_new_genrestitles_into_SQL(genrestitles_values):
    insert_statement = "INSERT INTO GENRESTITLES VALUES(?, ?)"
    try:
        cursor.execute(insert_statement, genrestitles_values)

    except Exception as e:
        cursor.rollback()
        print(e)
        print('Transaction rolled back')
    finally:
        print('Transaction inserted succesfully')
        cursor.commit()
        
        #TODO find måde at lukke disse to på...
        #cursor.close() # kun close hvis der ikke skal laves andet, hold åben hvis der skal hentes eller insættes mere...
    #my_conn.close()

def isAdult(text):
    return 0 if text == 'No' else 1

def getGenres():
    # GET GENRES:
    global list_of_selected_genres
    list_of_selected_genres = []
    genres = genres_field.get().split(',')
    print('genres after split:',genres)
    for genre in genres:
        genre = genre.rstrip(' ').lstrip(' ').capitalize()
        print('genre in loop:', genre, '. Table index:', genres_selection.index(genre)+1)
        list_of_selected_genres.append(genres_selection.index(genre)+1)

    # GET LEN OF GENRES FOR LOOP:
    #TODO Code it
    print(list_of_selected_genres)
    print(len(list_of_selected_genres))
    return list_of_selected_genres



main()
root.mainloop()

