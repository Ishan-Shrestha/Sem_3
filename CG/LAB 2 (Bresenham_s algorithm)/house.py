import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
COLOUR = (255, 0, 0)
BLACK = (0, 0, 0)

# Function to draw a line using DDA algorithm
def draw_line_dda(x1, y1, x2, y2):
    dx=x2-x1
    dy=y2-y1
    if abs(dx)>abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)
    xinc = dx/step
    yinc = dy/step
    x = x1
    y = y1
    for k in range(step+1):
        screen.set_at((round(x), round(y)), COLOUR) #function for set pixel
        x += xinc
        y += yinc
      
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw a line using DDA algorithm
        draw_line_dda(20,50 , 100, 10)
        draw_line_dda(100,10 , 180, 50)
        draw_line_dda(20,50 , 180, 50)
        draw_line_dda(20,50 , 20, 100)
        draw_line_dda(20,100 , 180,100)
        draw_line_dda(180,50 , 180,100)
        draw_line_dda(50,100 , 50, 80)
        draw_line_dda(50,80 , 120, 80)
        draw_line_dda(120,80 , 120, 100)
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()