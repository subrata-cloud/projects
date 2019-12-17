def last_3_characters(x):
    if len(x)==0:
        return ""
    elif len(x)>=1 and len(x)<=3:
        return x
    else:
        return x[len(x)-3:len(x)]

def first_10_characters(x):
    if len(x)==0:
        return ""
    elif len(x)>=1 and len(x)<=10:
        return x
    else:
        return x[0:10]

def chars_4_through_10(x):
    if len(x)==0:
        return ""
    elif len(x)<10:
        return ""
    else: 
        return x[4:11]

def str_length(x):
    return len(x)

def words(x):
    if len(x)==0:
        return list(x)
    else:
        return x.split(' ')

def capitalize(x):
    if len(x)==0:
        return ""
    elif len(x)==1:
        return x.upper()
    else:
        return x[0].upper()+x[1:len(x)]

def to_uppercase(x):
    if len(x)==0:
        return ""
    else:
        return x.upper()


