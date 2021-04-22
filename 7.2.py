def time_to_second(h,m,s):
    h=h*3600
    m=m*60
    s=s
    sec=h+m+s
    return sec

def second_to_time(t):
    time={}
    time['h']=int(t/3600)
    time['m']=int((t%3600)/60)
    time['s']=int(time['m']%60)
    return time


def sum_time(h1,m1,s1,h2,m2,s2):
    sumt={}
    sumt['h']=h1+h2
    if (m1+m2)<60:
        sumt['m']=m1+m2
    else:
        sumt['m']=(m1+m2)%60
        sumt['h']+=int((m1+m2)/60)
    if (s1+s2)<60:
        sumt['s']=s1+s2
    else:
        sumt['s']=(s1+s2)%60
        sumt['m']+=int((m1+m2)/60)       
    return sumt


def sub_time(h1,m1,s1,h2,m2,s2):
    subt={}
    if (h1-h2)>0:
        subt['h']=h1-h2
    else:
        subt['h']=0
    if (m1-m2)>0:
        subt['m']=m1-m2
    else:
        subt['m']=0

    if (s1-s2)>0:
        subt['s']=s1-s2
    else:
        subt['s']=0     
    return subt


print('1-sum')
print('2-subtraction')
print('3-second to time')
print('4-time to second')
print('5-exit')

while True:
    choice=int(input('please enter your choice: '))
    if choice==1:
        t1={}
        t2={}
        h1=int(input('enter h for time 1..'))
        m1=int(input('enter m for time 1..'))
        s1=int(input('enter s for time 1..'))
        t1['h']=h1
        t1['m']=m1
        t1['s']=s1

        h2=int(input('enter h for time 2..'))
        m2=int(input('enter m for time 2..'))
        s2=int(input('enter s for time 2..'))
        t2['h']=h2
        t2['m']=m2
        t2['s']=s2 
        r=sum_time(h1,m1,s1,h2,m2,s2)
        print(r)
    elif choice==2:
        t1={}
        t2={}
        h1=int(input('enter h for time 1..'))
        m1=int(input('enter m for time 1..'))
        s1=int(input('enter s for time 1..'))
        t1['h']=h1
        t1['m']=m1
        t1['s']=s1

        h2=int(input('enter h for time 2..'))
        m2=int(input('enter m for time 2..'))
        s2=int(input('enter s for time 2..'))
        t2['h']=h2
        t2['m']=m2
        t2['s']=s2 
        r=sub_time(h1,m1,s1,h2,m2,s2)
        print(r)

    elif choice==3:
        t=int(input('enter time ..'))
        r=second_to_time(t)
        print(r)

    elif choice==4:
        h=int(input('enter h ..'))
        m=int(input('enter m ..'))
        s=int(input('enter s ..'))
        r=time_to_second(h,m,s)
        print(r)

    elif choice==5:
        exit()