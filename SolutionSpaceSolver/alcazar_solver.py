import ham_cycle
import pygame
import time
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40 
HEIGHT = 40
 
# This sets the margin between each cell
MARGIN = 10
GRID_SIZE = 5
BOTTOM_DIVIDER_HEIGHT = 100

BOTTOM_DIVIDER = HEIGHT * GRID_SIZE + (GRID_SIZE+1) * MARGIN

# Hamiltonian Cycle initializations
board = ham_cycle.producePuzzleBoard(GRID_SIZE)
G = ham_cycle.Graph() 
ham_cycle.createNodes(G, board, 0, 24)


def numberToGrid(number):
    row = number // GRID_SIZE
    column = number % GRID_SIZE

    return row, column

def gridToNumber(row, column):
    number = row * GRID_SIZE + column

    return number


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
 
# Set the WIDTH and HEIGHT of the screen
WINDOW_SIZE = [WIDTH * GRID_SIZE + (GRID_SIZE+1) * MARGIN, HEIGHT * GRID_SIZE + (GRID_SIZE+1) * MARGIN  + BOTTOM_DIVIDER_HEIGHT]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
solution_array = []
remove_node_mode = False

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()

            if (pos[1] > BOTTOM_DIVIDER):

                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)

                if (column == 0):
                    if(remove_node_mode):
                        print("Remove Mode: OFF")
                    else:
                        print("Remove Mode: ON")
                    remove_node_mode = not remove_node_mode

                elif (column == 1):
                    print("Resetting Grid...")
                    # Reset Grid
                    for row in range(GRID_SIZE):
                        for col in range(GRID_SIZE):
                            grid[row][col] = 0

                    print('Hamiltonian Path In Progress...')
                    try:
                        solution_array = G.hamiltonian()
                    except KeyError:
                        print("Please enter a valid entrace or exit index.")

                    if (solution_array is None):
                        print("No solution found")
                        solution_array = []
                    
                elif (column == 2):
                    print("Resetting Grid...")
                    # Reset Grid
                    for row in range(GRID_SIZE):
                        for col in range(GRID_SIZE):
                            grid[row][col] = 0
                    

                
            elif ((pos[0] // MARGIN) % ((WIDTH + MARGIN) / MARGIN) == 0):
                row = pos[1] // (HEIGHT + MARGIN)
                column = int((pos[0] // MARGIN) // ((WIDTH + MARGIN) / MARGIN))

                print("Click side", pos, "Grid coordinates: ", row, column)
                if (side_grid[row][column] == 0):
                    side_grid[row][column] = 1
                    if (column > 0):
                        print("Making wall")
                        cell1 = gridToNumber(row, column)
                        cell2 = gridToNumber(row, column-1)
                        G.removeEdges(cell1, cell2)
                else:
                    side_grid[row][column] = 0
                    if (column > 0):
                        print("Removing wall")
                        cell1 = gridToNumber(row, column)
                        cell2 = gridToNumber(row, column-1)
                        G.add(cell1, cell2)
                
                
            elif ((pos[1] // MARGIN) % ((HEIGHT + MARGIN) / MARGIN) == 0):
                row = int((pos[1] // MARGIN) // ((HEIGHT + MARGIN) / MARGIN))
                column = pos[0] // (WIDTH + MARGIN)

                print("Click bottom", pos, "Grid coordinates: ", row, column)
                if (bottom_grid[row][column] == 0):
                    bottom_grid[row][column] = 1
                    if (row > 0):
                        print("Making wall")
                        cell1 = gridToNumber(row, column)
                        cell2 = gridToNumber(row-1, column)
                        G.removeEdges(cell1, cell2)
                else:
                    bottom_grid[row][column] = 0
                    if (row > 0):
                        print("Removing wall")
                        cell1 = gridToNumber(row, column)
                        cell2 = gridToNumber(row-1, column)
                        G.add(cell1, cell2)

            else:
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)

                # Set that location to one
                print("Click ", pos, "Grid coordinates: ", row, column)
                if (grid[row][column] == 0):
                    if (remove_node_mode):
                        grid[row][column] = 3
                    else:
                        grid[row][column] = 2
                    cell = gridToNumber(row, column)
                else:
                    grid[row][column] = 0
                    cell = gridToNumber(row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = BLUE
            elif grid[row][column] == 3:
                color = RED
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
    
    pygame.draw.rect(screen, (255,0,255), [MARGIN, BOTTOM_DIVIDER + MARGIN, WIDTH, HEIGHT]) # Add reset button
    pygame.draw.rect(screen, (138,43,226), [(MARGIN + WIDTH) + MARGIN, BOTTOM_DIVIDER + MARGIN, WIDTH, HEIGHT]) # Add reset button
    pygame.draw.rect(screen, (128,0,128), [(MARGIN + WIDTH) * 2 + MARGIN, BOTTOM_DIVIDER + MARGIN, WIDTH, HEIGHT]) # Add reset button

    if (len(solution_array) > 0):
        # print(solution_array)
        current_item = solution_array.pop(0)
        current_item_row, current_item_col = numberToGrid(current_item)
        grid[current_item_row][current_item_col] = 1
        time.sleep(0.2)

 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()