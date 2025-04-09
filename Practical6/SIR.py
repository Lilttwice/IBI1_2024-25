# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the initial basic variables of the IRS model
N = 10000 # Population size
S = N-1 # Number of sceptible people, since only one person is infected at the very beginning
I = 1 # One person is infected at the very beginning
R = 0 # Recovered individuals. Nobody has yet recovered.

beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate

# Create arrays for each of the variables to track how they evolve overtime.
S_arr = [S] 
I_arr = [I]
R_arr = [R]

# Time loop: 
# Calculate the probility of infection
# Randomly choose individuals to become infected
# Randomly choose individuals to recover
# Update the number of individuals in each variable
# Record each state in the arrays by adding the updated data using "append"
for t in range(1000):
    p_infection = beta*(I_arr[-1]/N)
# Randomly choose individuals to become infected
    new_infected = np.random.choice([0, 1], S_arr[-1], p=[1 - p_infection, p_infection]).sum() 
# Randomly choose individuals to recover
    new_recovered = np.random.choice([0, 1], I_arr[-1], p=[1 - gamma, gamma]).sum()   
 # Record the current updated state by adding data to the array
    S_arr.append(S_arr[-1]-new_infected)
    I_arr.append(I_arr[-1]+new_infected-new_recovered)
    R_arr.append(R_arr[-1]+new_recovered)
    plt.plot(S_arr, label='Susceptible Individuals')
# Draw and disply the result
plt.figure(figsize=(6, 4), dpi=200)
plt.plot(S_arr, label='Susceptible Individuals')
plt.plot(I_arr, label='Infected Individuals')
plt.plot(R_arr, label='Recovered Individuals')
plt.xlabel('Time')
plt.ylabel('Number of Individuals')
plt.title('SIR Model')
plt.legend()
plt.show()
