'''
complite
'''

def kr1_1():
    f=[int(input()) for x in range(8)]
    ves_truck=f[0]  #1
    hi_truck=f[1]   #2
    ves_piano=f[2]  #3
    hi_piano=f[3]   #4
    ves_holod=f[4]  #5
    hi_holod=f[5]   #6
    max_ves=f[6]    #7
    max_hi=f[7]     #8
    if max_ves >= ves_truck + ves_piano + ves_holod and (max_hi >= hi_truck + hi_piano and max_hi >= hi_truck + hi_holod):
        print('YES')
    elif max_ves < ves_truck + ves_piano or max_hi < hi_truck + hi_holod:
        print('NO')
    elif max_ves>= ves_truck + ves_holod +ves_piano and max_hi>= hi_truck + hi_piano  :
        print('YES')
    elif max_ves>= ves_truck + ves_holod and (max_hi >= hi_truck + hi_piano and max_hi >= hi_truck + hi_holod):
        print('YES')
    elif max_ves>= ves_truck + ves_holod + ves_piano and max_hi>= hi_truck + hi_holod:
        print('YES')
    elif (max_hi >= hi_truck + hi_piano and max_hi >= hi_truck + hi_holod) and max_ves>= ves_truck + ves_holod:
        print('YES')
    else:
        print('NO')
        
def kr1_2():
    f=[int(input()) for x in range(3)]

    f.sort()

    a=f[2]
    b=f[1]
    c=f[0]
    if a + b > c and a + c >b and c +b > a:
        if a**2 == b**2 + c**2:
            print('right')
        elif a**2> b**2 + c**2:
            print('obtuse')
        else:
            print('acute')
    else:
        print('impossible')
        
def kr1_3():
    k=0
    ls=[]
    f=0
    while True:
        s=int(input())
        if s == 0:
            break
        else:
            ls.append(s)
            f+=1
    for i in ls:
        k+=i
    print(round(k/f,2))

def kr1_4():
    ls=[]

    while True:
        s=int(input())
        if s == 0:
            break
        else:
            ls.append(s)
    ls.sort(reverse= True)
    for x in ls:
        if x%2 == 0:
            print(x)
            break
    else:
        print(0)
        
def kr1_5():
    t0=0
    t1=0
    t2=1
    ls=[t0,t1,t2]
    for x in range(100):
        ls.append(ls[0+x]+ls[1+x]+ls[2+x])
    s=input()
    for i in ls:
        if int(s)< i:
            print(ls.index(i))
            break
        
def kr1_6():
    
    a=int(input())
    b=int(input())

    while a!=0 and b!=0:
        if a>b:
            a=a%b
        else:
            b=b%a
    print(a+b)
    
def kr1_7():
    f=[int(input()) for x in range(int(input()))]
    a=0
    b=0
    for x in f:
        if f.count(x)>a:
            a=f.count(x)
            b=x
    print(b)
    
def kr1_8():
    
    def dot_product(N, vector1, vector2):
        prd=0
        while vector1:
            prd += vector1.pop(0)*vector2.pop(0)
        return(prd)

def kr1_9():
    ls=[]
    x=0
    while True:
        s=int(input())
        if s == 0:
            break
        else:
            ls.append(s)
            if len(ls) > 6 :
                if ls[0]<ls[1]:
                    ls.pop(0)
                else:
                    ls.pop(1)
                    
    print(ls[0])
    
def kr1_10():
    days=int(input())
    doski_colors=[]
    if days == 0:
        print('0 '*int(input()))
    else:
        for x in range(days):
            doski_colors.append([int(input()) for x in range(3)])
        m=int(input())
        vasya=[]
        for i in range(m):
            vasya.append(int(input()))
        doski_colors.reverse()
                         
        for y in vasya:
            for z in doski_colors:
                if y >= z[0] and y<= z[1]:
                    print(z[2],end=' ')
                    break
            else:
                print(0,end=' ')
