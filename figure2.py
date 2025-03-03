import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# 1. 模拟（或加载）空间频率与对应功率数据
# ---------------------------

# 在 0~60 cpd 范围内均匀取 200 个点
freq = np.linspace(0, 60, 200)

# 设定两种“漂移量”的峰值位置：20 cpd 与 30 cpd
peak_large = 20   # Large Drift Peak
peak_small = 30   # Small Drift Peak

# 宽度参数，可根据需要调整
sigma_large = 7.0
sigma_small = 7.0

# 用高斯函数模拟“归一化动态功率”
# 可以根据实际模型或实验数据替换为真实数值
power_large = np.exp(-(freq - peak_large)**2 / (2 * sigma_large**2)) 
power_small = np.exp(-(freq - peak_small)**2 / (2 * sigma_small**2))

# 为使曲线值在 0.7 ~ 1.0 区间浮动，这里稍加线性变换
power_large = 0.3 * power_large + 0.7
power_small = 0.3 * power_small + 0.7

# ---------------------------
# 2. 创建画布并绘制主曲线
# ---------------------------
fig, ax = plt.subplots(figsize=(6, 5))

# 绘制“大漂移量”曲线（红色）
ax.plot(freq, power_large, color='red', linewidth=2.0,
        label='Large Drift Diffusion Constant')

# 绘制“小漂移量”曲线（绿色）
ax.plot(freq, power_small, color='green', linewidth=2.0,
        label='Small Drift Diffusion Constant')

# ---------------------------
# 3. 绘制蓝色阴影区域（超出可分辨极限的频率）
# ---------------------------
# 假设从 50 cpd 开始为超出人类敏感度的频率（可参考文献 34）
ax.axvspan(50, 60, color='blue', alpha=0.1,
           label='Frequencies beyond resolvable limit')

# ---------------------------
# 4. 在图上添加参考线和文字标注
# ---------------------------

# 4.1 竖直参考线：Critical Frequency
# “Large Drift” 的峰值（约 20 cpd）
ax.axvline(x=peak_large, color='red', linestyle='--', alpha=0.5)
# “Small Drift” 的峰值（约 30 cpd）
ax.axvline(x=peak_small, color='green', linestyle='--', alpha=0.5)

# 4.2 添加示意箭头与文字
# 在两峰之间画一个黑箭头表示频率的转变方向
ax.annotate('Critical Frequency Shift', 
            xy=(25, 0.96),        # 箭头指向坐标
            xytext=(22, 1.02),    # 文字位置
            arrowprops=dict(facecolor='black', shrink=0.05, width=1),
            fontsize=10, color='black')

# ---------------------------
# 5. 设置坐标范围、标签、图例等
# ---------------------------
ax.set_xlim(0, 60)
ax.set_ylim(0.7, 1.05)

ax.set_xlabel('Spatial Frequency (cpd)', fontsize=12)
ax.set_ylabel('Normalized Dynamic Power', fontsize=12)
ax.set_title('Effect of Drift on Retinal Signal Power', fontsize=14)

ax.legend(loc='upper right', fontsize=9)
ax.grid(False)

plt.tight_layout()
plt.show()
