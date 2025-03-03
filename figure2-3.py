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
fig, ax = plt.subplots(figsize=(6, 5))

# 大漂移量曲线（红色）
ax.plot(freq, power_large,
        color='red', linewidth=2.0,
        label='大漂移量扩散常数')

# 小漂移量曲线（绿色）
ax.plot(freq, power_small,
        color='green', linewidth=2.0,
        label='小漂移量扩散常数')

# 蓝色阴影区域：假设超出 50 cpd 人眼不可分辨
ax.axvspan(50, 60, color='blue', alpha=0.1,
           label='超出可分辨范围的频段')

# 竖直虚线：标注峰值位置
ax.axvline(x=peak_large, color='red', linestyle='--', alpha=0.5)
ax.axvline(x=peak_small, color='green', linestyle='--', alpha=0.5)

# 注释箭头
ax.annotate('临界频率变化',
            xy=(25, 0.96),         # 箭头指向坐标
            xytext=(22, 1.02),     # 文字位置
            arrowprops=dict(facecolor='black', shrink=0.05, width=1),
            fontsize=10, color='black')

# 设置坐标范围、标签、标题
ax.set_xlim(0, 60)
ax.set_ylim(0.7, 1.05)

ax.set_xlabel('空间频率 (cpd)', fontsize=12)
ax.set_ylabel('归一化动态功率', fontsize=12)
ax.set_title('漂移对视网膜信号功率的影响', fontsize=14)

# 图例
ax.legend(loc='upper right', fontsize=9)

# 布局
plt.tight_layout()

# ---------------------------
# 3. 保存图片并/或显示
# ---------------------------
plt.savefig('中文漂移功率图.png', dpi=300)
# 如需窗口中预览，请取消下面这行的注释：
# plt.show()

print("图像已保存为 '中文漂移功率图.png'。")
