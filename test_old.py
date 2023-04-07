# from codecs import encode, decode
# sample = u'mon€y\\nröcks'
# result = decode(encode(sample, 'latin-1', 'backslashreplace'), 'unicode-escape')
# print(result)

# records = [
#     ['Daniel'],
#     ['Malene']
# ]
linelist = []
records = []

try:
    # RESET:
    fileHandler = open('data2.tsv', encoding='UTF-8')
    
    for line in fileHandler:
        cleanedLine = line.split(",")
        cleanedLine = repr(line).replace(r'\t', ',').replace(r'\\N', 'NULL').replace(r'\\n', r'').replace(r'\n', r'') #decode(encode(line, 'latin-1', 'backslashreplace'), 'unicode-escape')
        cleanedLine = cleanedLine.lstrip("'")
        cleanedLine = cleanedLine.rstrip("'")
        #cleanedLine = r''+line #decode(line, 'unicode-escape')
        print(cleanedLine)
        linelist.append(cleanedLine)
        print(linelist)
        records.append(linelist)
    #CTRL + æ = goto terminal

except Exception as e:
    print('Error in filepath')
    print(e)
    quit()

# print(records)


