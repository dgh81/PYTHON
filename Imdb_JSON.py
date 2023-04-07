# from Create_IMDB_Titles import records
import json
import timeit

# def my_json_writer():
#     with open('data.json', 'w', encoding='utf-8') as f:
#         json.dump(records, f, ensure_ascii=False, indent=4)

def my_json_reader():
    with open('data.json', 'r', encoding='utf-8') as f:
        global data
        data = json.load(f)
        return data

# print('SendRecordsToSQL: ', timeit.timeit(my_json_writer, number=1), ' seconds')
print('SendRecordsToSQL: ', timeit.timeit(my_json_reader, number=1), ' seconds')

print(data)