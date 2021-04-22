class time:
    def __init__(self,hh=0,mm=0,ss=0,tt=0):
        self.h=hh
        self.m=mm
        self.s=ss
        self.t=tt

    def time_to_second(self):
        hour=self.h*3600
        min=self.m*60
        sec=self.s
        result=hour+min+sec       
        return result

    def sum(self,other):
        result=time()
        result.h=self.h+other.h
        if (self.m+other.m)<60:
            result.m=self.m+other.m
        else:
            result.m=(self.m+other.m)%60
            result.h+=int((self.m+other.m)/60)
        if (self.s+other.s)<60:
            result.s=self.s+other.s
        else:
            result.s=(self.s+other.s)%60
            result.m+=int((self.m+other.m)/60)       
        return result

    def second_to_time(self):
        result=time()
        result.h=int(self.t/3600)
        result.m=int((self.t%3600)/60)
        result.s=int(result.m%60)
        return result
        
    def sub(self,other):
        result=time()
        if (self.h-other.h)>0:
            result.h=self.h-other.h
        else:
            result.h=0
        if (self.m-other.m)>0:
            result.m=self.m-other.m
        else:
            result.m=0

        if (self.s-other.s)>0:
            result.s=self.s-other.s
        else:
            result.s=0     
        return result
            
    def show(self):
        print(self.h,':',self.m,':',self.s)

a=time(2,50,30)
a.show()
b=time(1,25,30)
b.show()
c=a.sum(b)
c.show()

d=a.sub(b)
d.show()

k=a.time_to_second()
print(k)

k=time(0,0,0,4500)
p=k.second_to_time()
p.show()