# Library needed
import matplotlib.pyplot as plt

# define the population in areas of the UK
uk_population = [57.11, 3.13, 1.91, 5.45]
# define the popularion of nearby provinces of Zhejiang
zj_neighbor_population = [65.77, 41.88, 45.28, 61.27, 85.15]

# sort the population in areas of the UK
sorted_uk_population = sorted(uk_population)
# sort the population of nearby provinces of Zhejiang
sorted_zj_neighbor_population = sorted(zj_neighbor_population)

print("Sorted UK population:", sorted_uk_population)
print("Sorted Zhejiang - neighboring population:", sorted_zj_neighbor_population)

# label the population in areas of the UK
uk_labels = ['England', 'Wales', 'Northern Ireland', 'Scotland']
# label the population of nearby provinces of Zhejiang
zj_neighbor_labels = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']

uk_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
zj_neighbor_colors = ['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# draw figures
# draw pie chart to show the population distribution in areas of the UK
plt.figure(figsize=(8, 8))
plt.pie(uk_population, labels=uk_labels, colors=uk_colors, autopct='%1.1f%%', startangle=140)
plt.title('Population Distribution in UK Countries')
plt.show()
# draw pie chart to show the population distribution in nearby provinces of Zhejiang
plt.figure(figsize=(8, 8))
plt.pie(zj_neighbor_population, labels=zj_neighbor_labels, colors=zj_neighbor_colors, autopct='%1.1f%%', startangle=90)
plt.title('Population Distribution in Zhejiang - neighboring Provinces')
plt.show()
# show the two pie chart into one figure
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.pie(uk_population, labels=uk_labels, colors=uk_colors, autopct='%1.1f%%', startangle=140)
plt.title('Population Distribution in UK Countries')
plt.subplot(1, 2, 2)
plt.pie(zj_neighbor_population, labels=zj_neighbor_labels, colors=zj_neighbor_colors, autopct='%1.1f%%', startangle=90)
plt.title('Population Distribution in Zhejiang - neighboring Provinces')
plt.show()
