# impor t n e c e s s a r y l i b r a r i e s
import numpy as np
import matplotlib.pyplot as plt

# 初始化模型参数  
N = 10000  # 总人口  
S = N - 1  # 初始易感人数  
I = 1      # 初始感染人数  
R = 0      # 初始康复人数  
beta = 0.3  # 感染率  
gamma = 0.05  # 恢复率  

# 创建数组记录各时间步的S、I、R数量  
S_array = [S]  
I_array = [I]  
R_array = [R]  

# 模拟1000个时间步  
for _ in range(1000):  
    # 计算易感者感染的概率（beta * 感染者比例）  
    infection_prob = beta * (I / N)  
    # 计算感染者康复的数量  
    recover_num = np.random.choice(range(2), I, p=[1 - gamma, gamma]).sum()  
    # 计算易感者感染的数量  
    infect_num = np.random.choice(range(2), S, p=[1 - infection_prob, infection_prob]).sum()  

    # 更新S、I、R数量  
    S -= infect_num  
    I = I + infect_num - recover_num  
    R += recover_num  

    # 记录结果  
    S_array.append(S)  
    I_array.append(I)  
    R_array.append(R)  

# 绘制结果  
plt.figure(figsize=(6, 4), dpi=150)  
plt.plot(S_array, label='Susceptible')  
plt.plot(I_array, label='Infected')  
plt.plot(R_array, label='Recovered')  
plt.xlabel('Time Step')  
plt.ylabel('Number of People')  
plt.title('SIR Model Simulation')  
plt.legend()  
plt.show()  
# 若需保存图片，取消注释下一行并指定路径  
# plt.savefig('sir_model.png', type='png')  