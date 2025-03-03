import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# ---------------------------
# 0. 设置中文字体
# ---------------------------
# 这里设置使用“黑体”SimHei，如需使用其他中文字体，可自行替换
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置为黑体
mpl.rcParams['axes.unicode_minus'] = False    # 正常显示负号

# ---------------------------
# 1. 生成或模拟数据
# ---------------------------
freq = np.linspace(0, 60, 200)  # 空间频率 (cpd)，从 0 ~ 60 均匀取 200 个点

# 设定两条“漂移”曲线的峰值位置
peak_large = 20   # 大漂移量时的峰值
peak_small = 30   # 小漂移量时的峰值
sigma_large = 7.0
sigma_small = 7.0

# 用高斯函数模拟两条曲线在不同中心频率达到最大值
power_large = np.exp(-((freq - peak_large)**2) / (2 * sigma_large**2))
power_small = np.exp(-((freq - peak_small)**2) / (2 * sigma_small**2))

# 将曲线值做线性缩放，使其在 0.7 ~ 1.0 范围内波动
power_large = 0.3 * power_large + 0.7
power_small = 0.3 * power_small + 0.7

# ---------------------------
# 2. 绘图
# ---------------------------
fig, ax = plt.subplots(figsize=(6, 5))

# 画“大漂移量扩散常数”曲线（红色）
ax.plot(freq, power_large,
        color='red', linewidth=2.0,
        label='大漂移量扩散常数')

# 画“小漂移量扩散常数”曲线（绿色）
ax.plot(freq, power_small,
        color='green', linewidth=2.0,
        label='小漂移量扩散常数')

# 蓝色阴影区域：假设大于 50 cpd 部分超过人眼可分辨极限
ax.axvspan(50, 60, color='blue', alpha=0.1,
           label='超出可分辨范围的频段')

# 在 20 和 30 cpd 处加竖直虚线
ax.axvline(x=peak_large, color='red', linestyle='--', alpha=0.5)
ax.axvline(x=peak_small, color='green', linestyle='--', alpha=0.5)

# 添加箭头及注释
ax.annotate('临界频率变化',
            xy=(25, 0.96),         # 箭头指向位置
            xytext=(22, 1.02),     # 注释文字位置
            arrowprops=dict(facecolor='black', shrink=0.05, width=1),
            fontsize=10, color='black')

# 设置坐标轴范围、标题和坐标轴标签
ax.set_xlim(0, 60)
ax.set_ylim(0.7, 1.05)

ax.set_xlabel('空间频率 (cpd)', fontsize=12)
ax.set_ylabel('归一化动态功率', fontsize=12)
ax.set_title('漂移对视网膜信号功率的影响', fontsize=14)

# 图例放在右上角
ax.legend(loc='upper right', fontsize=9)

# 调整布局，避免文字重叠
plt.tight_layout()

# ---------------------------
# 3. 保存为 PNG 文件并/或显示
# ---------------------------
plt.savefig('中文漂移功率图.png', dpi=300)
# 若想在本地查看绘图窗口，可再添加：
# plt.show()

print("已保存为 '中文漂移功率图.png'。若需要在窗口中查看，请取消注释 plt.show()。")
