import timeit
import numpy as np
import csv


def Records():
    with open("data_1.tsv", 'r', encoding='UTF-8') as f:
        reader = csv.reader(f, delimiter="\t")
        for line in zip(reader):
            record = []
            fields = list(line[0])
            if len(fields) == 9:
                for field in fields:
                    ff = field.replace(r'\N','NULL').replace('\n','')
                    # print(ff)
                    try:
                        newField = np.int(ff) # numpy int type ellers fejler: # tt21914118 titles: 9223372036854775807,  569936821221962380720
                        record.append(newField)
                    except:
                        if ff == 'NULL':
                            ff = None
                            record.append(ff)
                        else:
                            record.append(ff)
            yield record





# global i
# i = 0
# for x in lines():
#     if i < 10:
#         print(x)
#         i += 1
        