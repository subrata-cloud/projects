data="""
india,asia
china,asia
england,europe
france,europe
south africa,africa
egypt,africa
"""

def does_country_exist_in_continent(data, continent_name, country_name):
  item=data.split('\n')
  key=country_name+','+continent_name
  if key in item:
      return "Yes"
  else:
      return "No"

print(does_country_exist_in_continent(data, "asia", "china"))


def convert_dict(data):
    item=data.split('\n')
    dict1={}
    for key in item:
        if key !='':
            x=key.split(',')
            if x[1] not in dict1:
                dict1[x[1]]=[]
            dict1[x[1]].append(x[0])
    print(dict1)


convert_dict(data)


    

