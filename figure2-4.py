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

# Matplotlib 全局设置：使用指定字体来保证能正确显示中文字符
# 但此处我们想让大部分内容（图例、曲线）用英文，所以后面在
# 需要中文的地方再显式指定 fontproperties=my_font
mpl.rcParams['font.family'] = my_font.get_name()
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# ---------------------------
# 1. 生成 / 模拟数据
# ---------------------------
freq = np.linspace(0, 60, 200)  # 空间频率 (cpd) 范围 0~60
peak_large = 20   # 大漂移峰值
peak_small = 30   # 小漂移峰值
sigma_large = 7.0
sigma_small = 7.0

# 高斯函数模拟两条曲线（仅示例，真实情况请换成您的实验数据）
power_large = np.exp(-((freq - peak_large)**2) / (2 * sigma_large**2))
power_small = np.exp(-((freq - peak_small)**2) / (2 * sigma_small**2))

# 线性缩放至 [0.7, 1.0]
power_large = 0.3 * power_large + 0.7
power_small = 0.3 * power_small + 0.7

# ---------------------------
# 2. 开始绘图
# ---------------------------
fig, ax = plt.subplots(figsize=(6, 5))

# (1) Plot - Large Drift
ax.plot(freq, power_large,
        color='red', linewidth=2.0,
        label='Large Drift Diffusion Constant')  # 英文

# (2) Plot - Small Drift
ax.plot(freq, power_small,
        color='green', linewidth=2.0,
        label='Small Drift Diffusion Constant')  # 英文

# (3) 蓝色阴影区域：在 50 cpd 之后假设超出可分辨极限 (英文说明)
ax.axvspan(50, 60, color='blue', alpha=0.1,
           label='Frequencies beyond resolvable limit')

# (4) 竖直虚线以标记两条曲线峰值
ax.axvline(x=peak_large, color='red', linestyle='--', alpha=0.5)
ax.axvline(x=peak_small, color='green', linestyle='--', alpha=0.5)

# (5) 英文注释箭头
ax.annotate('Critical Frequency Shift',
            xy=(25, 0.96),        # 箭头指向位置
            xytext=(22, 1.02),    # 文字位置
            arrowprops=dict(facecolor='black', shrink=0.05, width=1),
            fontsize=10, color='black')

# ---------------------------
# 3. 仅标题、X/Y 轴标签用中文
# ---------------------------
ax.set_xlim(0, 60)
ax.set_ylim(0.7, 1.05)

ax.set_xlabel('空间频率 (cpd)', fontproperties=my_font, fontsize=12)     # 中文
ax.set_ylabel('归一化动态功率', fontproperties=my_font, fontsize=12)   # 中文
ax.set_title('漂移对视网膜信号功率的影响', fontproperties=my_font, fontsize=14)  # 中文

# 图例 (保持英文)
ax.legend(loc='upper right', fontsize=9)

# 布局
plt.tight_layout()

# ---------------------------
# 4. 保存并/或显示
# ---------------------------
plt.savefig('part_chinese_part_english.png', dpi=300)
# 如需在窗口中预览，请取消注释：
# plt.show()

print("图已保存为 part_chinese_part_english.png。标题和 X/Y 轴使用了中文，其余为英文。")
