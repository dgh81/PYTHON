import timeit

content = ''
i = 1
x = 0

def read_write_data(chunk):
    global content
    try:
        with open('data.tsv', encoding='UTF-8') as fileHandler:
            lines = fileHandler.readlines()
            global i
            global x
            global slut
            start = x * 10000
            slut = 10000 * chunk
            content = ''

            for line in lines[start:slut]:
                content += line

            # for line in fileHandler:
            #     if i < x:
            #         content += line
            #         # print(i)   
            #         i += 1
            x += 1

    except Exception as e:
        # print('Error in filepath')
        # print(e)
        quit()

    with open('data_2mio.tsv', 'a', encoding='UTF-8') as fileHandler:
        for line in content[:-1]:
            fileHandler.write(line)

def runChunks():
    # for l in range(1,100): #0-1.000.000 rækker
    for l in range(1,3):
        read_write_data(l)
        print('Finished writing chunk', l, 'to file...')


print('timeit runChunks: ', timeit.timeit(runChunks, number=1))
