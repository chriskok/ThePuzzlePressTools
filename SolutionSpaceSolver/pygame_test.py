"""
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
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

side_grid = []
for row in range(GRID_SIZE):
    side_grid.append([])
    for column in range(GRID_SIZE + 1):
        if (column == 0 or column == GRID_SIZE):
            side_grid[row].append(1)
        else:
            side_grid[row].append(0)  # Append a cell

bottom_grid = []
for row in range(GRID_SIZE + 1):
    bottom_grid.append([])
    for column in range(GRID_SIZE):
        if (row == 0 or row == GRID_SIZE):
            bottom_grid[row].append(1)
        else:
            bottom_grid[row].append(0)  # Append a cell

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

            if ((pos[0] // MARGIN) % ((WIDTH + MARGIN) / MARGIN) == 0):
                row = pos[1] // (HEIGHT + MARGIN)
                column = int((pos[0] // MARGIN) // ((WIDTH + MARGIN) / MARGIN))

                print("Click side", pos, "Grid coordinates: ", row, column)
                if (side_grid[row][column] == 0):
                    side_grid[row][column] = 1
                else:
                    side_grid[row][column] = 0
            elif ((pos[1] // MARGIN) % ((HEIGHT + MARGIN) / MARGIN) == 0):
                row = int((pos[1] // MARGIN) // ((HEIGHT + MARGIN) / MARGIN))
                column = pos[0] // (WIDTH + MARGIN)

                print("Click bottom", pos, "Grid coordinates: ", row, column)
                if (bottom_grid[row][column] == 0):
                    bottom_grid[row][column] = 1
                else:
                    bottom_grid[row][column] = 0
            else:
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)

                # Set that location to one
                print("Click ", pos, "Grid coordinates: ", row, column)
                if (grid[row][column] == 0):
                    grid[row][column] = 1
                else:
                    grid[row][column] = 0
 
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
            if side_grid[row][column] == 1:
                color = RED                              
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
            if bottom_grid[row][column] == 1:
                color = RED                              
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