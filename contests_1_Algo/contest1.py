def numbers():
    number=str(input('enter: '))
    z=0
    for x in number:
        z+=int(x)


        
def ferz():
    x1=int(input())
    y1=int(input())
    x2=int(input())
    y2=int(input())
    if x1 == x2 or y1 == y2:
        print('yes')
    if x1 < x2 and y1 < y2:
        while x1 != x2 and y1 != y2:
            x1 += 1
            y1 += 1
            if x1 == x2 and y1 == y2:
                print ('yes')
                break
            if x1 == 9 or y1 == 9:
                print ('no')
                break
        else:
            print('no')
    elif x1 > x2 and y1 > y2:
        while x1 != x2 and y1 != y2:
            x1 -= 1
            y1 -= 1
            if x1 == x2 and y1 == y2:
                print ('yes')
                break
            if x1 == 0 or y1 == 0:
                print ('no')
                break
        else:
            print('no')
            
    elif x1 < x2 and y1 > y2:
        while x1 != x2 and y1 != y2:
            x1 += 1
            y1 -= 1
            if x1 == x2 and y1 == y2:
                print ('yes')
                break
            if x1 == 9 or y1 == 9:
                print ('no')
                break
        else:
            print('no')
    elif x1 > x2 and y1 < y2:
        while x1 != x2 and y1 != y2:
            x1 -= 1
            y1 += 1
            if x1 == x2 and y1 == y2:
                print ('yes')
                break
            if x1 == 0 or y1 == 0:
                print ('no')
                break
        else:
            print('no')


def year():
    x = int(input('year: '))
    if x > 0 and x < 10000 and x%4 == 0 and (x%100 != 0 or x%400 == 0):
        print('yes')
    else:
        
        print('no')


def naturals():
    x = int(input())
    if x <10000:
        for y in range(1,x):
            if x > y**2: print(y**2, end=' ')
    

def squares():
    k=1
    count=1
    x = int(input())
    while x>=k:
        k*=2
        count+=1
    else: print(count-1)

def lenpos():
    strok=[]
    x=1
    counter=0
    while x:
        x=input()
        strok.append(x)
    for y in strok:
        counter+=1
        if y == '0':
            print(counter-1)
            break

def sumpos():
    strok=[]
    x=1
    y=0
    while x:
        x=int(input())
        y+=x
    else: print(y)
    
def chetmass():
    count=0
    x=1
    while x:
        x=int(input())
        if x%2 ==0 and x !=0:
            count+=1
    else: print(count)
def natmass():
    x=1
    l=[]
    while x:        
        x=int(input())
        l.append(x)
    else:
        l.sort()
        print(l[-1])
def natmassmax():
    x=1
    l=[]
    while x:        
        x=int(input())
        l.append(x)
    else:
        l.sort()
        print(l.count(l[-1]))
        


        
    
    
   
