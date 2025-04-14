# libraries needed for SIR model with vaccination
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# define basic concepts
vaccination_percentage = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
beta = 0.3
gamma = 0.05
infected_total = []

# for every vaccination percentage，looping：
for per in vaccination_percentage:
    
    # define basic concept of the model in the loop
    N = [10000]
    infected = [1]
    recovered = [0]
    susceptible = [(N[0] - infected[0] - recovered[0]) * (1 - per)]

    # for 1000 times，loopinng：
    for i in range(1, 1000):

        rd_1 = np.random.choice(range(2), infected[i - 1], p = [1 - gamma, gamma])
        num_recovered = sum(rd_1)

        pro_infect = beta * infected[i - 1] / N[0]
        rd_2 = np.random.choice(range(2), int(susceptible[i - 1]), p = [1 - pro_infect, pro_infect])
        num_infected = sum(rd_2)

        # update the number of infected, recovered and susceptible individuals
        if num_infected > susceptible[i - 1]:
            num_infected = susceptible[i - 1]
        infected.append(infected[i - 1] + num_infected - num_recovered)
        recovered.append(recovered[i - 1] + num_recovered)
        susceptible.append(susceptible[i - 1] - num_infected)
    # add in the list of total, prepare for drawing figure
    infected_total.append(infected)

# draw figure
plt.figure(figsize = (6, 4), dpi = 150)

colormap = cm.get_cmap('plasma', len(vaccination_percentage)) 

plt.plot(infected_total[0], label='0', color = colormap(0))
for i in range(1, 11):
    plt.plot(infected_total[i], label = str(int(vaccination_percentage[i] * 100)) + '%', color = colormap(i))

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()

plt.show()