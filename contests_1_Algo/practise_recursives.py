

def fac(n):
    if n ==0 :
        return 1
    else:
        return n * fac(n-1)

def fibon(n):
    if n in (1,2):
        return 1
    return fibon(n-1) + fibon(n-2)

import turtle

def draw(l, n):
    if n == 0:
        turtle.left(180)
        return

    x = l / (n + 1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.left(90)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.right(135)
    turtle.forward(x)
    turtle.left(180)
    turtle.forward(l)

'''    
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
'''
def kriv(n,f):
    
    if n == 0:
        turtle.forward(f)

    else:
        
        kriv(n-1,f/3)
        turtle.left(60)    
        kriv(n-1,f/3)   
        turtle.right(120)
        kriv(n-1,f/3)
        turtle.left(60)
        kriv(n-1,f/3)


def snejinka(n,f):
    for i in range(3):
        kriv(n,f)
        turtle.right(120)

def mink(n,f):
    if n==0:
        turtle.forward(f)
        turtle.left(90)
        turtle.forward(f)
        turtle.right(90)
        turtle.forward(f)
        turtle.right(90)
        turtle.forward(f)
        turtle.forward(f)
        turtle.left(90)
        turtle.forward(f)
        turtle.left(90)
        turtle.forward(f)
        turtle.right(90)
        turtle.forward(f)
    else:
        
        mink(n-1,f/8)
        turtle.left(90)
        mink(n-1,f/8)
        turtle.right(90)
        mink(n-1,f/8)
        turtle.right(90)
        mink(n-1,f/8)
        mink(n-1,f/8)
        turtle.left(90)
        mink(n-1,f/8)
        turtle.left(90)
        mink(n-1,f/8)
        turtle.right(90)
        mink(n-1,f/8)
        return


def levi(n,f):
    if n==0:
        turtle.forward(f)
        
    else:
        levi(n-1,f/(2**(1/2)))
        turtle.right(90)
        levi(n-1,f/(2**(1/2)))
        turtle.left(90)
        

turtle.speed('fastest')


def dragon(n,f,sgn=1):
    if n==0:
        turtle.forward(f)
    else:
       
        dragon(n-1,f/(2**(1/2)),1)
        turtle.right(90*sgn)
        dragon(n-1,f/(2**(1/2)),-1)
        
def kantor(n,f,x=0,y=0):
    if n==0:
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.forward(f)
        return
    else:
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.forward(f)
        kantor(n-1,f/3,x,y-20)
        kantor(n-1,f/3,x+(f/3*2),y-20)

    
    


