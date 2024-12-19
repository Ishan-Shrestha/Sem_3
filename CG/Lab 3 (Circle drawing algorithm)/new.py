import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Mid-point Circle Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0,0, 0)
 
def circle(x,y,r):
    a = 0 
    b = r 
    d = 1 - r
    while(a<=b):
        screen.set_at((round(a + x), round(b + y)), WHITE) 
        screen.set_at((round(b + x), round(a + y)), WHITE) 
        screen.set_at((round(-b + x), round(a + y)), WHITE) 
        screen.set_at((round(-a + x), round(b + y)), WHITE) 
        screen.set_at((round(-a + x), round(-b + y)), WHITE) 
        screen.set_at((round(-b + x), round(-a + y)), WHITE) 
        screen.set_at((round(b + x), round(-a + y)), WHITE) 
        screen.set_at((round(a + x), round(-b + y)), WHITE) 
        a = a + 1
        if(d < 0):
            d = d + 2*a + 1
        else:
            d = d + 2*a - 2*b + 1
            b = b - 1
        
# Main loop
    # r = int(input("Enter the radius of circle: "))
    # x = int(input("Enter the x-coordinate of center: "))
    # y = int(input("Enter the y-coordinate of circle: "))
    

    # Clear the screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
    circle(50,50,30)

    pygame.display.flip()