import timeit
newRecord = []
records = []

professionsIndex = {'actor': 1,
'soundtrack': 2,
'director': 3,
'actress': 4,
'miscellaneous': 5,
'producer': 6,
'writer': 7,
'composer': 8,
'casting_director': 9,
'art_department': 10,
'music_department': 11,
'special_effects': 12,
'costume_department': 13,
'executive': 14,
'make_up_department': 15,
'cinematographer': 16,
'assistant_director': 17,
'editorial_department': 18,
'editor': 19,
'animation_department': 20,
'camera_department': 21,
'stunts': 22,
'production_manager': 23,
'talent_agent': 24,
'sound_department': 25,
'production_designer': 26,
'costume_designer': 27,
'art_director': 28,
'visual_effects': 29,
'casting_department': 30,
'transportation_department': 31,
'set_decorator': 32,
'script_department': 33,
'location_management': 34,
'music_artist': 35,
'manager': 36,
'legal': 37,
'publicist': 38,
'assistant': 39,
'podcaster': 40,
'production_department': 41,
'choreographer': 42,
'electrical_department': 43,
'': 'NULL'}

def CreateNamesProfessions():
    global records
    with open("name_basics_data_13.tsv", 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            # print(i)
            line = lines[i].replace('\t','myDelimiter').replace(r'\N','NULL').replace('\n','').split('myDelimiter')
            professions = line[4].split(',')
            countProfessions = len(professions)
            # print(directors)
            global newRecord
            for x in range(countProfessions):
                primaryKey = line[0]
                newRecord.append(primaryKey)
                # newRecord.append(line[1])
                # newRecord.append(line[2])
                # newRecord.append(line[3])
                # print(professions[x])
                newRecord.append(professionsIndex[professions[x]])
                # newRecord.append(line[5])
                records.append(newRecord)
                # print(newRecord)
                newRecord = []

print('CreateNamesProfessionsRecords: ', timeit.timeit(CreateNamesProfessions, number=1), ' seconds')

