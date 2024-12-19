import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's Line Drawing Algorithm")

# Colors
COLOUR = (0, 200, 255)
BLACK = (0, 0, 0)

# Function to draw a line using bresenham algorithm
def draw_line_bresenham(x1, y1, x2, y2):
    x = x1
    y= y1
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if x2>x1:
        dx=1
    else:
        dx =-1
    if y2>y1:
        dy = 1
    else:
        dy = -1
    if dx>dy:
        p = 2*dy-dx
        while x<=x2:
            screen.set_at((x, y), COLOUR)
            if p<0:
                x=x+dx
                p = p+2*dy
            else:
                x = x+dx
                y = y + dy
                p = p+2*dy - 2*dx
    else:
        p = 2*dx-dy
        while y<=y2:
            screen.set_at((x, y), COLOUR)
            if p<0:
                x=x
                y = y + dy
                p = p +2*dx
            else:
                x = x+dx
                y = y + dy
                p = p+2*dx - 2*dy
      
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw a line using bresenham algorithm
        draw_line_bresenham(20,20 , 100, 100)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()