class fraction:
    def __init__(self,ss=0,mm=1):
        self.s=ss
        self.m=mm
    def mul(self,other):
        result=fraction()
        result.s=self.s*other.s
        result.m=self.m*other.m
        return result
    def sum(self,other):
        result=fraction()
        result.s=self.s*other.m+other.s*self.m
        result.m=self.m*other.m
        return result
    def sub(self):
        result=fraction()
        result.s=self.s*other.m-other.s*self.m
        result.m=self.m*other.m
        return result
    def dev(self):
        result=fraction()
        result.s=self.s*other.m
        result.m=self.m*other.s
        return result
    def show(self):
        print(self.s,'/',self.m)

a=fraction(2,3)
a.show()

b=fraction(4,5)
b.show()

c=a.sum(b)
c.show()
d=b.mul(a)
d.show()