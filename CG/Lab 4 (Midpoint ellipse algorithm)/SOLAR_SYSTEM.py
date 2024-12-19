import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

# Colors
ELLIPSE_COLOUR=(255,255,255)
BLACK = (0,0, 0)

def circle(x,y,r,CIRCLE_COLOUR):
    a = 0 
    b = r 
    d = 1 - r
    while(a<=b):
        screen.set_at((round(a + x), round(b + y)), CIRCLE_COLOUR) 
        screen.set_at((round(b + x), round(a + y)), CIRCLE_COLOUR) 
        screen.set_at((round(-b + x), round(a + y)), CIRCLE_COLOUR) 
        screen.set_at((round(-a + x), round(b + y)), CIRCLE_COLOUR) 
        screen.set_at((round(-a + x), round(-b + y)), CIRCLE_COLOUR) 
        screen.set_at((round(-b + x), round(-a + y)), CIRCLE_COLOUR) 
        screen.set_at((round(b + x), round(-a + y)), CIRCLE_COLOUR) 
        screen.set_at((round(a + x), round(-b + y)), CIRCLE_COLOUR) 
        a = a + 1
        if(d < 0):
            d = d + 2*a + 1
        else:
            d = d + 2*a - 2*b + 1
            b = b - 1

def PLANETS(x,y,r):
    a = 0 
    b = r 
    d = 1 - r
    while(a<=b):
        screen.set_at((round(a + x), round(b + y)), 'BLUE') 
        screen.set_at((round(b + x), round(a + y)), 'BLUE') 
        screen.set_at((round(-b + x), round(a + y)), 'BLUE') 
        screen.set_at((round(-a + x), round(b + y)), 'GREEN') 
        screen.set_at((round(-a + x), round(-b + y)), 'GREEN') 
        screen.set_at((round(-b + x), round(-a + y)), 'BLUE') 
        screen.set_at((round(b + x), round(-a + y)), 'BLUE') 
        screen.set_at((round(a + x), round(-b + y)), 'GREEN') 
        a = a + 1
        if(d < 0):
            d = d + 2*a + 1
        else:
            d = d + 2*a - 2*b + 1
            b = b - 1
 
def ellipse(xc,yc,rx,ry):
    x=0
    y=ry
    p1 = ry**2-(rx**2)*ry+0.25*(ry**2)
    dx=2*(ry**2)*x
    dy=2*(rx**2)*y
    while (dx<=dy):
        screen.set_at((x+xc,y+yc), ELLIPSE_COLOUR) 
        screen.set_at((-x+xc,y+yc), ELLIPSE_COLOUR) 
        screen.set_at((x+xc,-y+yc), ELLIPSE_COLOUR) 
        screen.set_at((-x+xc,-y+yc), ELLIPSE_COLOUR) 
        if p1<0:
            dx=2*(ry**2)*x
            dy=2*(rx**2)*y
            x+=1
            y=y
            p1=p1+dx+ry**2
        else:
            dx=2*(ry**2)*x
            dy=2*(rx**2)*y
            x+=1
            y-=1
            p1=p1+dx-dy+ry**2
    p2=ry**2*(x+0.5)**2+rx**2*(y-1)**2-(rx**2)*(ry**2)
    while(y!=0):
        screen.set_at((x+xc,y+yc), ELLIPSE_COLOUR) 
        screen.set_at((-x+xc,y+yc), ELLIPSE_COLOUR) 
        screen.set_at((x+xc,-y+yc), ELLIPSE_COLOUR) 
        screen.set_at((-x+xc,-y+yc), ELLIPSE_COLOUR) 
        if p2>0:
            dx=2*(ry**2)*x
            dy=2*(rx**2)*y
            x=x
            y-=1
            p2=p2-dy+rx**2
        else:
            dx=2*(ry**2)*x
            dy=2*(rx**2)*y
            x+=1
            y-=1
            p2=p2+dx-dy+rx**2
        
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        ellipse(400,300,200,100)
        ellipse(400,300,350,200)
        for r in range(51):
            circle(400,300,r,'YELLOW')
        
        for r in range(26):
            if r<=8:
                circle(400,200,r,'BLUE')
            else:
                PLANETS(400,200,r)

        for r in range(26):
            circle(400,500,r,'ORANGE')
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()