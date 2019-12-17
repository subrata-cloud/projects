import math
def integers_from_start_to_end_using_range(start, end, step):
   data=[]
   for item in range(start, end, step):
       data.append(item)
   return data


def integers_from_start_to_end_using_while(start, end, step):
    data=[]
    if step<0:
        while start>end:
            data.append(start)
            start+=step
    else:
        while start<end:
            data.append(start)
            start+=step
    return data

def two_digit_primes():
    data=[]
    for item in range(10,100):
        flag=1
        for key in range(2,item):
            if item%key==0:
                flag=0
                break
        if flag==1:
            data.append(item)
    return data
