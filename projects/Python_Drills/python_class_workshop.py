class Counter:
    def __init__(self):
        self.value=0
    def incr(self):
        self.value+=1
        x=self.value
        return x
    def decr(self):
        self.value-=1
        x=self.value
        return x
    def incrby(self,n):
        self.value+=n
        x=self.value
        return x
    def decrby(self,n):
        self.value-=n
        x=self.value
        return x

obj=Counter()
print(obj.incr())
print(obj.incrby(3))
print(obj.decr())
print(obj.decrby(2))

