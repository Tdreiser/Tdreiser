def zad5_1():
    x,y,r=input().split()
    if pow(int(r),2)>pow(int(x),2)+pow(int(y),2):
        print('YES')
    else:
        print('NO')
        
def zad5_2():
    x,p,y=input().split()
    x,p,y=int(x),int(p)/100,int(y)
    cnt=0
    
    while x<y:
        s=str(x*p)
        s=s[0:(s.find('.')+3)] 
        x+=float(s)
        cnt+=1
        
    print(cnt)
  
def zad5_3():
    cnt=0
    maximum=0
    for x in range(int(input())):
        z=input()
        if z == '1':
            cnt+=1
        else:
           
            cnt=0
        if cnt>maximum:
            maximum=cnt
    print(maximum)

def zad5_4():
    mini=float('+inf')
    maxi=float('-inf')
    x='0'
    cnt=0
    trinity=0
    mid_tri=0
    mid_sum=0
    glc=0
    while True:
        x=input()
        if x=='#':
            break
        y=int(x)
        mid_sum+=y
        cnt+=1
        trinity+=y     
        if cnt == 3:
            mid_tri+=trinity%y
            trinity=0
            cnt=0
        if y>maxi:
            maxi=y
        if y<mini:
            mini=y
        glc+=1
        
    mid_sum/=glc
    print(mid_sum,maxi,mini,mid_tri)
    
def zad5_5():
    n=int(input())
    a=[]
    while True:
        x=input()
        if x=='#':
            break
        y=x
        a.append(y.split())
    flg=False
    lst=[]
    buff=0
    for x in range(0,n+1):
        for stud in a:
            if int(stud[0])==x:
                flg=True
                buff+=int(stud[1])
                idi=stud[0]
        if flg:
            flg=False
            lst.append((idi,buff))
        buff=0
    lst.sort(key=lambda x: x[1], reverse=True)
    mid=[]
    for i in lst:
        for y in a:
            if i[0]==y[0]:
                mid.append(int(y[1]))
        mid.sort(reverse=True)
        for l in mid:
            print(l, end=' ')
        mid=[]

def zad5_6():
    n=4
    x=[[0 for a in range(3)] for i in range(n)]
    for i in x:
        print(i)
        
   


