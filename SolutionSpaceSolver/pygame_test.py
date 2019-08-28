"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40 
HEIGHT = 40
 
# This sets the margin between each cell
MARGIN = 10

GRID_SIZE = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(GRID_SIZE):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(GRID_SIZE):
        grid[row].append(0)  # Append a cell
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [HEIGHT * GRID_SIZE + (GRID_SIZE+1) * MARGIN , HEIGHT * GRID_SIZE + (GRID_SIZE+1) * MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

            if ((pos[0] // MARGIN) % ((WIDTH + MARGIN) / MARGIN) == 0):
                print("Click ", pos, "Grid coordinates: ", row, column)
                print("CLICKED SIDE")
            elif ((pos[1] // MARGIN) % ((HEIGHT + MARGIN) / MARGIN) == 0):
                print("Click ", pos, "Grid coordinates: ", row, column)
                print("CLICKED BOTTOM")
            else:
                # Set that location to one
                grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    # Draw the sides
    for row in range(GRID_SIZE):
        for column in range(0, GRID_SIZE + 1):
            color = GREEN
            # if grid[row][column] == 1:
            #     color = RED                              
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              MARGIN,
                              HEIGHT])
    
    # Draw the bottoms
    for row in range(0, GRID_SIZE + 1):
        for column in range(GRID_SIZE):
            color = GREEN
            # if grid[row][column] == 1:
            #     color = RED                              
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row,
                              WIDTH,
                              MARGIN])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()