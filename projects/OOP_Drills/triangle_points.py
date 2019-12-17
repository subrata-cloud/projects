import math

class Triangle:
    def __init__(self):
        self.x1=0
        self.y1=0
        self.x2=0
        self.y2=0
        self.x3=0
        self.y3=0

    def add_point(self,x1,y1,x2,y2,x3,y3):
        self.x1+=x1
        self.y1+=y1
        self.x2+=x2
        self.y2+=y2
        self.x3+=x3
        self.y3+=y3

    def perimeter(self):
        s1=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        s2=math.sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
        s3=math.sqrt((self.x1-self.x3)**2+(self.y1-self.y3)**2)
        return round((s1+s2+s3),2)
    
    #def is_equal(self,other):
    def __eq__(self,other):
        if self.x1==other.x1 and self.x2==other.x2 and self.x3==other.x3:
            if  self.y1==other.y1 and self.y2==other.y2 and self.y3==other.y3:
                return True
            else:
                return False
        else:
            return False

t1=Triangle()
t1.add_point(0,0,0,3,4,0)
print(t1.perimeter())
t2=Triangle()
t2.add_point(1,2,2,1,1,5)
print(t2.perimeter())
t3=Triangle()
t3.add_point(1,2,2,1,1,5)

#print(t1==t3)
#print(t1.is_equal(t3))
#print(t3.is_equal(t1))

print(t1==t3)


