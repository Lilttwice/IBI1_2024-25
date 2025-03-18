import matplotlib.pyplot as plt

# 定义英国各地区人口列表
uk_population = [57.11, 3.13, 1.91, 5.45]
# 定义浙江周边省份人口列表
zj_neighbor_population = [65.77, 41.88, 45.28, 61.27, 85.15]

# 对英国各地区人口列表进行排序
sorted_uk_population = sorted(uk_population)
# 对浙江周边省份人口列表进行排序
sorted_zj_neighbor_population = sorted(zj_neighbor_population)

# 打印排序后的列表
print("Sorted UK population:", sorted_uk_population)
print("Sorted Zhejiang - neighboring population:", sorted_zj_neighbor_population)

# 定义英国各地区名称
uk_labels = ['England', 'Wales', 'Northern Ireland', 'Scotland']
# 定义浙江周边省份名称
zj_neighbor_labels = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']

# 设置饼图颜色
uk_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
zj_neighbor_colors = ['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# 绘制英国各地区人口分布饼图
plt.figure(figsize=(8, 8))
plt.pie(uk_population, labels=uk_labels, colors=uk_colors, autopct='%1.1f%%', startangle=140)
plt.title('Population Distribution in UK Countries')
plt.show()

# 绘制浙江周边省份人口分布饼图
plt.figure(figsize=(8, 8))
plt.pie(zj_neighbor_population, labels=zj_neighbor_labels, colors=zj_neighbor_colors, autopct='%1.1f%%', startangle=90)
plt.title('Population Distribution in Zhejiang - neighboring Provinces')
plt.show()
