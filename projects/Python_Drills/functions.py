def is_prime(n):
    flag=1
    for key in range(2,n):
        if n%key==0:
            flag=0
            break
    if flag==1:
        return True
    else:
        return False

def n_digit_primes(digit):
    data=[]
    for item in range(10**(digit-1),10**digit):
        flag=1
        for key in range(2,item):
            if item%key==0:
                flag=0
                break
        if flag==1:
            data.append(item)
    return data

def one_digit_primes(n):
    data=[]
    for item in range(10**(n-1),10**n):
        flag=1
        for key in range(2,item):
            if item%key==0:
                flag=0
                break
        if flag==1 and item!=1:
            data.append(item)
    return data