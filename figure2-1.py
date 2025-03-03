import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# 1. 生成模拟数据
# ---------------------------
freq = np.linspace(0, 60, 200)  # 空间频率 (cpd)
peak_large = 20   # 大漂移峰值
peak_small = 30   # 小漂移峰值
sigma_large = 7.0
sigma_small = 7.0

# 用简单高斯模拟归一化功率曲线
power_large = np.exp(-((freq - peak_large)**2) / (2 * sigma_large**2))
power_small = np.exp(-((freq - peak_small)**2) / (2 * sigma_small**2))

# 将值缩放至 0.7~1.0 区间
power_large = 0.3 * power_large + 0.7
power_small = 0.3 * power_small + 0.7

# ---------------------------
# 2. 绘图
# ---------------------------
fig, ax = plt.subplots(figsize=(6, 5))

# (a) 画“Large Drift”曲线（红色）
ax.plot(freq, power_large, color='red', linewidth=2.0, 
        label='Large Drift Diffusion Constant')
# (b) 画“Small Drift”曲线（绿色）
ax.plot(freq, power_small, color='green', linewidth=2.0, 
        label='Small Drift Diffusion Constant')

# (c) 蓝色阴影区：假设超过 50 cpd 属于超人类敏感范围
ax.axvspan(50, 60, color='blue', alpha=0.1, 
           label='Frequencies beyond resolvable limit')

# (d) 竖直参考线：20 cpd 与 30 cpd
ax.axvline(x=peak_large, color='red', linestyle='--', alpha=0.5)
ax.axvline(x=peak_small, color='green', linestyle='--', alpha=0.5)

# 添加箭头注释，用于说明“Critical Frequency Shift”
ax.annotate('Critical Frequency Shift',
            xy=(25, 0.96),         # 箭头指向位置
            xytext=(22, 1.02),     # 文字位置
            arrowprops=dict(facecolor='black', shrink=0.05, width=1),
            fontsize=10, color='black')

# 设置轴范围、标签等
ax.set_xlim(0, 60)
ax.set_ylim(0.7, 1.05)
ax.set_xlabel('Spatial Frequency (cpd)', fontsize=12)
ax.set_ylabel('Normalized Dynamic Power', fontsize=12)
ax.set_title('Effect of Drift on Retinal Signal Power', fontsize=14)
ax.legend(loc='upper right', fontsize=9)

# 布局与输出
plt.tight_layout()

# ---------------------------
# 3. 保存为 PNG 文件
# ---------------------------
plt.savefig('drift_plot.png', dpi=300)  # 300 DPI 分辨率

# 如需在本地弹出查看，可再加上一行：
# plt.show()

print("绘图完成并已保存为 drift_plot.png")
