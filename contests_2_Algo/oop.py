import pygame as pg
import sys
class Vector():
    
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    
    def __rmul__(self, other):
        return Vector(self.y * other.y, self.x * other.x)
    
    def __iadd__ (self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __neg__(self):
        return Vector( -self.x, -self.y)
    def __str__(self):
        return 'x = {}, y ={}'.format(self.x, self.y)
    def intpair(self):
        return int(self.x), int(self.y)
    


class Ball():
    
    def __init__(self, x, y, vx , vy, Pt_x, Pt_y):
        self.coords = Vector(x,y)
        self.velocity = Vector(vx,vy)
        self.Pt_x=Pt_x
        self.Pt_y=Pt_y

    def update(self,dt):
        if self.coords.x >= widht -20 or self.coords.x <=20 :
            self.Pt_x*=-1
        if self.coords.y >= hight -20 or self.coords.y <=20 :
            self.Pt_y*=-1
        self.path = Vector(self.Pt_x, self.Pt_y)    
        self.coords += self.velocity*self.path*Vector(dt,dt)

    def render(self, canvas):
        ff=pg.draw.circle(canvas, (0, 0, 200),(f.coords.intpair()), 20)
        return
        
hight = 500
widht = 500

screen = pg.display.set_mode((widht, hight))
pg.display.set_caption('YAHOOOO')
clock = pg.time.Clock()
Ball_buffer=[]
while True:
    
    dt = clock.tick(50) / 1000.0
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT :
            sys.exit()
            
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                sys.exit()
    if pg.mouse.get_pressed()[2]:
        if pg.Rect.collidepoint():
            print('ok')
    if pg.mouse.get_pressed()[0]:
        Ball_buffer.append(Ball(*pg.mouse.get_pos(),0,50,1,1))
        
    screen.fill((0, 0, 0))  
    for f in Ball_buffer:
        f.update(dt)
    
        f.render(screen)
    pg.display.flip()
   
#f = Ball(30,30,10,10,1,1)
#print(f.coords.intpair())
#f.update(10)
#print(f.coords.intpair())
