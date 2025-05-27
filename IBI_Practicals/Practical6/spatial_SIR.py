# libraries needed for simulation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation # Show the figures like animation.

# Parameters setup
beta = 0.3  # Infection probability
gamma = 0.05  # Recovery probability
size = 100  # Figure size (100x100)
timesteps = 100  # Duration of simulation

# Initialize population to be two dimensional figure 
# susceptible=0
# infected=1
# recovered=2
# figure type: integer
population = np.zeros((size, size), dtype=int)

# initial infected individual need to be selected randomly as patien zero
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1

# draw figure
plt.figure(figsize=(8, 6), dpi=150)
plt.title("2D Spatial SIR Model") # figure title
plt.xlabel("X Position") # label x axis
plt.ylabel("Y Position") # label y axis

cmap = cm.colors.ListedColormap(['red', 'green', 'blue'])
bounds = [0, 1, 2, 3]
norm = cm.colors.BoundaryNorm(bounds, cmap.N)

# Find all infected individual cells (grid equal to 1)
def find_infected(grid):
    return np.argwhere(grid == 1)

# Find all Infect neighbors
def infect_neighbors(grid, infected_cells):
    new_grid = grid.copy() # Avoid chaging original data
    for cell in infected_cells:
        x, y = cell
        # Check if all 8 neighbors are susceptible (grid equal to 0)
        # If yes, infect them with probability beta
        for i in range(max(0, x-1), min(size, x+2)):
            for j in range(max(0, y-1), min(size, y+2)):
                if (i != x or j != y) and grid[i, j] == 0:  # Don't infect self and only susceptible individuals
                    if np.random.random() < beta:
                        new_grid[i, j] = 1
    return new_grid

# Recover infected individual cells 
def recover_cells(grid, infected_cells):
    new_grid = grid.copy() # Avoid changing original data, replace the infected cells with recovered cells
    # Check if the infected cells are recovered with probability gamma
    for cell in infected_cells:
        if np.random.random() < gamma:
            new_grid[cell[0], cell[1]] = 2
    return new_grid

# Main loop for the stimulation:
for t in range(100):
    # Find all the infected individual cells
    infected_cells = find_infected(population)
    
    # The neighbors infected by the infected cells
    # Using the infect_neighbor function we had defined, check if the neighbors are susceptible (grid equal to 0)
    population = infect_neighbors(population, infected_cells)
    
    # Recover infected cells
    # Using the recover_cells function we had defined, check if the infected cells are recovered
    # If yes, replace the infected cells with recovered cells (grid equal to 2)
    population = recover_cells(population, infected_cells)
    
    # draw the figure of current state
    plt.clf() # Clear previous figure
    plt.imshow(population, cmap=cmap, norm=norm, interpolation='nearest')
    plt.title(f"2D Spatial SIR Model - Time Step {t}")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.colorbar(ticks=[0.5, 1.5, 2.5], label='State', 
                 boundaries=bounds, values=[0, 1, 2])
    plt.pause(0.1)  # Pause to let the figure update
plt.show()  # Show the final figure
# Save the final figure     



