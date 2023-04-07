# import unicodecsv
import csv

# from read_file_old import *

myList = []
finalList = []

with open("data_1.tsv", encoding='UTF-8') as myFile:
    tsv_file = csv.reader(myFile, delimiter="\t")

# with open("data2.tsv", encoding='UTF-8') as myFile:

    i = 1
    # REFACTOR !!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    # TEST:
    # lines = file.readlines()
    # line_iter = iter(lines)
    # for line in line_iter:

    for line in tsv_file:
    # for line in myFile:
        print(line)
        # test = line.split()
        
        #TEST:
        # tabed_line = csv.reader(myFile, delimiter="\t")
        # print(tabed_line[0])


        if len(line) != 9:
            print("FEJL I TEST!")
            # tsv_file.__next__()

        myList = []
        for x in range(9):
            newItem = ''
            if x == 4 or x == 5 or x == 6 or x == 7:
                # print(line[x])
                try:
                    newItem = int(line[x])
                except:
                    newItem = line[x].replace(r'\N', 'NULL')
                    if newItem == 'NULL':
                        newItem = None
                    else:
                        newItem = line[x]
                    print('Some error')
            else:
                newItem = line[x].replace(r'\N', 'NULL')
                if newItem == 'NULL':
                    newItem = None
                else:
                    newItem = line[x]

            # print(newItem)
            myList.append(newItem)
        finalList.append(myList)

# print(finalList)