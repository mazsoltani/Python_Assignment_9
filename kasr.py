def sum(x,y):
    result = {}
    result['s']=x['s']* y['m'] + y['s'] * x['m']
    result['m']= x['m'] * y['m']
    return result

def minus(x,y):
    result = {}
    result['s']=x['s']* y['m'] - y['s'] * x['m']
    result['m']=x['m'] * y['m']
    return result

def mul(x,y):
    result = {}
    result['s']= x['s'] * y['s']
    result['m']= x['m'] * y['m']
    return result 

def div(x,y):
    result = {}
    result['s']= x['s'] * y['m']
    result['m']= x['m'] * y['s']
    return result

def show_menu():
    print('1-Summation')
    print('2- Minus')
    print('3- Muliplation')
    print('4- Divition')
    print('5- Exit')

while True:
    s1 = int(input('Please Enter Sorate kasre Aval "a" in "a/b"= '))
    m1 = int(input('Please Enter Makhraje kasre Aval "b" in "a/b"='))
    s2 = int(input('Please Enter Sorate kasre Dovom "a" in "a/b"='))
    m2 = int(input('Please Enter Makhraje kasre Dovom "b" in "a/b"='))
    a = {'s':s1 , 'm':m1}
    b = {'s':s2 , 'm':m2}
    show_menu()
    choice = int(input('Please choose a Menu Item='))
    if choice==1:
        sum_res=sum(a,b)
        print(sum_res['s'],'/',sum_res['m'])
    elif choice==2:
        minus_res=minus(a,b)
        print(minus_res['s'],'/',minus_res['m'])
    elif choice==3:
        multi_res = mul(a,b)
        print(multi_res['s'],'/',multi_res['m'])
    elif choice==4:
        div_res=div(a,b)
        print(div_res['s'],'/',div_res['m'])
    elif choice==5:  
        break
