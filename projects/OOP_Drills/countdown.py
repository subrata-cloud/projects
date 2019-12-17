class Counter:
    def __init__(self):
        self.value=0
    def incr(self):
        self.value+=1
        return self.value
    def decr(self):
        self.value-=1
        return self.value
    def incrby(self,n):
        self.value+=n
        return self.value
    def decrby(self,n):
        self.value-=n
        return self.value

c1=Counter()
print(c1.incr())
print(c1.incrby(2))
print(c1.decr())
print(c1.decrby(2))