def mul(x,y):
    result={'s':None, 'm':None}

    result['s']=x['s']*y['s']
    result['m']=x['m']*y['m']

    return result

def sum(x,y):
    result={}

    result['s']=x['s']*y['m']+x['m']*y['s']
    result['m']=x['m']*y['m']

    return result


def dev(x,y):
    result={'s':None, 'm':None}

    result['s']=x['s']*y['m']
    result['m']=x['m']*y['s']

    return result   


def sub(x,y):
    result={}

    result['s']=x['s']*y['m']-x['m']*y['s']
    result['m']=x['m']*y['m']

    return result



a={}
b={}
a_s=int(input('enter s for a..'))
a['s']=a_s
a_m=int(input('enter m for a..'))
a['m']=a_m

b_s=int(input('enter s for b..'))
b['s']=b_s
b_m=int(input('enter m for b..'))
b['m']=b_m 


print('1-multiply')
print('2-sum')
print('3-subtraction')
print('4-devide')
print('5-exit')

while True:
    choice=int(input('please enter your choice: '))
    if choice==1:
        r=mul(a,b)
        print(r)
    elif choice==2:
        r=sum(a,b)
        print(r)
    elif choice==3:
        r=dev(a,b)
        print(r)
    elif choice==4:
        r=sub(a,b)
        print(r)
    elif choice==5:
        exit()