my_dict={'id1':
         {'name':['aarav'],
          'class':['6'],
          'subject_intigration':['Math,Science,English']
          },
          'id2':
          {'name':['Akshay'],
           'class':['7'],
           'subject_intigration':['Sciene,GK,English']
           },
          'id3':
           {'name':['sonal'],
            'class':['9'],
           ' subject_intigration':['Sst,Math,English']
           },
         }
result={}
for key,value in my_dict.items():
    if value not in result.values():
        result[key]=value
print(result)    