def word_count(s):
    result={}
    words=s.split(' ')
    for word in words:
        if word[-1]==',' or word[-1]=='.':
            word=word[0:-1]
        if word in result:
            result[word]+=1
        else:
            result[word]=1
    return result

def dict_items(d):
    item=[]
    for key in d:        
        item.append((key,d[key]))
    return item
def myFunc(e):
    return e
def dict_items_sorted(d):
   item=[]
   for key in d:
       item.append((key,d[key]))
   item.sort(key=myFunc)
   return item
