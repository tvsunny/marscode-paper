import math
import random
import csv

# 固定随机数种子，便于结果复现
random.seed(42)

# 设置相关参数
num_samples = 200  # 在 200 ms 内，每毫秒记录一次
sampling_rate = 1000.0  # 1000 Hz
x_center = 400.0   # X 方向初始位置 (像素)
y_center = 400.0   # Y 方向初始位置 (像素)

# 正弦运动参数 (可根据需求自行调整)
amplitude_x = 2.0   # X 方向正弦波幅度
freq_x = 10.0       # X 方向正弦波频率 (Hz)
amplitude_y = 1.5   # Y 方向正弦波幅度
freq_y = 8.0        # Y 方向正弦波频率 (Hz)

# 噪声水平 (控制模拟随机漂移)
noise_level = 0.3

# 输出 CSV 文件名
output_filename = "eye_data.csv"

# 打开 CSV 文件，写入数据
with open(output_filename, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # 写入表头
    writer.writerow(["Time(ms)", "X(px)", "Y(px)"])
    
    for t in range(num_samples):
        # 当前时刻 (以毫秒为单位)
        time_ms = t  # 0 ~ 199
        
        # 将毫秒转换成秒，便于计算正弦
        time_sec = time_ms / sampling_rate
        
        # 计算 X 方向正弦运动
        sin_x = amplitude_x * math.sin(2.0 * math.pi * freq_x * time_sec)
        # 计算 Y 方向正弦运动，给个相位偏移示例（如 math.pi / 4）
        sin_y = amplitude_y * math.sin(2.0 * math.pi * freq_y * time_sec + math.pi / 4)
        
        # 叠加随机噪声
        noise_x = random.uniform(-noise_level, noise_level)
        noise_y = random.uniform(-noise_level, noise_level)
        
        # 最终像素坐标
        x_t = x_center + sin_x + noise_x
        y_t = y_center + sin_y + noise_y
        
        # 写入一行记录
        writer.writerow([time_ms, f"{x_t:.3f}", f"{y_t:.3f}"])

print(f"CSV 文件已生成: {output_filename}")
