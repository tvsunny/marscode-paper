import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties

# ---------------------------
# 0. 设置中文字体路径
# ---------------------------
# 假设当前目录下有 simhei.ttf；如果放在其他位置，需要改为绝对路径
font_path = 'simhei.ttf'
# 创建一个 FontProperties 对象
my_font = FontProperties(fname=font_path)

# Matplotlib 全局设置：使用指定字体
mpl.rcParams['font.family'] = my_font.get_name()
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# ---------------------------
# 1. 生成或模拟数据
# ---------------------------
freq = np.linspace(0, 60, 200)  # 空间频率 (cpd) 范围 0~60
peak_large = 20   # 大漂移峰值
peak_small = 30   # 小漂移峰值
sigma_large = 7.0
sigma_small = 7.0

# 用高斯函数模拟两条曲线（仅示例，真实情形可读取实验数据）
power_large = np.exp(-((freq - peak_large)**2) / (2 * sigma_large**2))
power_small = np.exp(-((freq - peak_small)**2) / (2 * sigma_small**2))

# 线性缩放至 [0.7, 1.0]
power_large = 0.3 * power_large + 0.7
power_small = 0.3 * power_small + 0.7

# ---------------------------
# 2. 开始绘图
# ---------------------------
plt.figure(figsize=(10, 6))
plt.plot(freq, power_large, label='大漂移峰值', color='blue')
plt.plot(freq, power_small, label='小漂移峰值', color='red')
plt.xlabel('空间频率 (cpd)', fontproperties=my_font)
plt.ylabel('功率', fontproperties=my_font)
plt.title('漂移峰值示例', fontproperties=my_font)
plt.legend()
plt.grid(True)

# 保存图形到本地
plt.savefig('test.png')

# 显示图形
plt.show()