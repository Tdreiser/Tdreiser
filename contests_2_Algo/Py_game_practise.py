import sys
import pygame

pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

x1 = 250
y1 = 50
vx_1 = 48
vy_1 = 48

x2 = 50
y2 = 50
vx_2 = 48
vy_2 = 48


Pt_x1 = -1
Pt_y1 = 1

Pt_x2 = 1
Pt_y2 = 1

r=150
g=10
b=50
ax_x=5
ax_y=5
rsx_1=0
rsy_1=0


    
flag=True    
while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sys.exit()

    if pygame.key.get_pressed()[pygame.K_UP]:
        if Pt_y1<0:
            vy_1+=ax_y
        #else:
          #  vy-=ax_y
            
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        if Pt_y1>0:
            vy_1+=ax_y
        #else:
          #  vy-=ax_y
            
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if Pt_x1>0:
            vx_1+=ax_x
        #else:
          #  vx-=ax_x
    
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if Pt_x1<0:
            vx_1+=ax_x
        #else:
          #  vx-=ax_x    
      
    rsx_1=(vx_1**2)/1000
    rsy_1=(vy_1**2)/1000
    ax_x=int(vx_1/rsx_1)
    ax_y=int(vy_1/rsy_1)
    
    x1 += vx_1 * dt*Pt_x1
    y1 += vy_1* dt*Pt_y1

    x2 += vx_2 * dt*Pt_x2
    y2 += vy_2* dt*Pt_y2

    if x1>=width-20 or x1 <=0+20:
       Pt_x1*=-1
    if y1>=height -20 or y1 <=0+20:
        Pt_y1*=-1
        
    if x2>=width-20 or x2 <=0+20:
       Pt_x2*=-1
    if y2>=height -20 or y2 <=0+20:
        Pt_y2*=-1
        
    
         
    screen.fill((0, 0, 0))
    if flag:
        f =pygame.draw.circle(screen, (r, g, b), (int(x1), int(y1)), 20)
        z= pygame.draw.circle(screen, (r, g, b), (int(x2), int(y2)), 20)
        flag=False
    else:
        pygame.Rect.move_ip(f,Pt_x1,Pt_y1)
        pygame.Rect.move_ip(z,Pt_x2, Pt_y2)
        pygame.draw.ellipse(screen,(r,g,b),f)        
        pygame.draw.ellipse(screen,(r,g,b),z)
        pygame.draw.circle(screen, (r, g, b), (int(x1), int(y1)), 20)
    if pygame.mouse.get_pressed()[2]:
        if pygame.Rect.collidepoint(f,*pygame.mouse.get_pos()):
            r=108
            g=230
            b=19
            
    if f.colliderect(z) or z.colliderect(f) :
        if Pt_x1!=Pt_x2 and Pt_y1!=Pt_y2:
            Pt_x1*=-1
            Pt_x2*=-1
            Pt_y1*=-1
            Pt_y2*=-1
        if Pt_x1==Pt_x2 and Pt_y1!=Pt_y2:
            Pt_y1*=-1
            Pt_y2*=-1
        if Pt_x1!=Pt_x2 and Pt_y1==Pt_y2:
            Pt_x1*=-1
            Pt_x2*=-1
    print(int(x1-f.x))

    pygame.display.flip()
    
    
