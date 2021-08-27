class kasr:
    
    def __init__(self,s,m):
        self.s = s
        self.m = m
   
    def sum(self,makhraj):
        res_sum = kasr(None,None)
        res_sum.s = (self.s * makhraj.m) + (makhraj.s * self.m)
        res_sum.m = self.m * makhraj.m
        return res_sum
        

    def minus(self,makhraj):
        res_minus = kasr(None,None)
        res_minus.s = (self.s * makhraj.m) - (makhraj.s * self.m)
        res_minus.m = self.m * makhraj.m
        return res_minus

    def mul(self,makhraj):
        res= kasr(None,None)
        res.s = self.s * makhraj.s
        res.m = self.m * makhraj.m
        return res

    def div(self,makhraj):
        res= kasr(None,None)
        res.s = self.s * makhraj.m
        res.m = self.m * makhraj.s
        return res
    
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

    kasr1 = kasr(s1,m1)
    kasr2 = kasr(s2,m2)
    show_menu()
    choice = int(input('Please choose a Menu Item='))
    if choice==1:
        ans_sum = kasr1.sum(kasr2)
        print("Your Answer is=",ans_sum.s,"/",ans_sum.m)
        
    elif choice==2:
        ans_minus= kasr1.minus(kasr2)
        print("Your Answer is=",ans_minus.s,"/",ans_minus.m)
    elif choice==3:
        ans_mul= kasr1.mul(kasr2)
        print("Your Answer is=",ans_mul.s,"/",ans_mul.m)
    elif choice==4:
        ans_div = kasr1.div(kasr2)
        print("Your Answer is=",ans_div.s,"/",ans_div.m)
    elif choice==5:
        break
