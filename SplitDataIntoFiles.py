import timeit

def myCopy(n):
    lineNumber = 1000000   # resulting file line count
    filename = 'data_' + str(n+1) + '.tsv'
    print(filename)

    with open('namebasics.tsv', 'r', encoding='UTF-8') as rf:
        with open(filename, 'w', encoding='UTF-8') as wf:
            for i, line in enumerate(rf):
                if i >= lineNumber * n and i < lineNumber * (n+1):
                    wf.write(line)

for n in range (15):
    myCopy(n)

# print('Time: ', timeit.timeit(myCopy, number=1))

