def sum_items_in_list(x):
    sum=0
    for item in x:
        sum+=item
    return sum

def list_length(x):
    return len(x)

def last_three_items(x):
    if len(x)>=0 and len(x)<=3:
        return x
    else:
        return x[len(x)-3:len(x)]

def first_three_items(x):
    if len(x)>=0 and len(x)<=3:
        return x
    else:
        return x[0:3]

def myFun(e):
    return e

def sort_list(x):
    if len(x)==0 or len(x)==1:
        return x
    else:
        x.sort()
        return x

def append_item(x, item):
    x.append(item)
    return x

def remove_last_item(x):
    x.pop()
    return x


def count_occurrences(x, item):
    c=x.count(item)
    return c

def is_item_present_in_list(x, item):
    return item in x

def append_all_items_of_y_to_x(x, y):
    x.extend(y)
    return x

def list_copy(x):
    y=x.copy()
    return y








