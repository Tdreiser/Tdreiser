import graphics as gr
from math import sqrt
SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model",SIZE_X, SIZE_Y)


coords = gr.Point(250,350)



slp_coof=1
coof=1
y=0
r=200

def countpoint():
    x =sqrt(r**2-y**2)
   
    return x


def step(point_1,point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                          point_1.y - point_2.y)
    return new_point
slp=0.001
circle=gr.Circle(coords,10)
circle.setFill('red')

circle.draw(window)
cnt=0
coofx=1
while True: 
    if y == 0:
        coof=-1
        cnt+=1
    elif y == - r:
        coof=1
        cnt+=1
    if cnt==2:
        coofx*=-1
        cnt=0
    realpoint = gr.Point(countpoint(),y)
    y+=2*coof
    
    nextpoint = gr.Point(countpoint(),y)
    
        
    steper = step(realpoint,nextpoint)
    
    print (y,steper.x)
    circle.move(steper.x*coofx,steper.y)
  
    gr.time.sleep(slp)
    '''
    if y == 0:
        slp_coof=2
    elif y == 49.5 or -y == 49.5:
        slp_coof=0.5
    '''
    
window.getMouse()

window.close()










































'''sx=300
sy=500
sz_X=50
sz_Y=20
def kirpich(strt_x=300,strt_y=500,x=0,y=0):
    my_Rectangle=gr.Rectangle(gr.Point(strt_x+2+x,strt_y+2+y),
                              gr.Point(strt_x+sz_X+x,strt_y+sz_Y+y))
    my_Rectangle.setFill('red')
    my_Rectangle.setWidth(2)
    my_Rectangle.setOutline('black')
    my_Rectangle.draw(window)  
def wall(widht,high):   
    for s in range(widht):
        for z in range(high):
            kirpich( x=s*sz_X,y=z*sz_Y)
    return(widht)

def roof(high):
    first_line=gr.Line(gr.Point(sx+2,sy-10),
                       gr.Point(sx+sz_X*widht,sy-10))
    second_line=gr.Line(gr.Point(sx+2,sy-10),
                        gr.Point(sx+2+sz_X*widht/2,sy-high))
    third_line=gr.Line(gr.Point(sx+sz_X*widht,sy-10),
                        gr.Point(sx+2+sz_X*widht/2,sy-high))
    first_line.setWidth(3)
    second_line.draw(window)
    second_line.setWidth(3)
    first_line.draw(window)
    third_line.setWidth(3)
    third_line.draw(window)
    
widht=wall(10,12)
roof(300)'''
