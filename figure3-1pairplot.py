import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# 读取Excel数据
file_path = '测试数据.xlsx'  # 请根据你的文件路径修改

# 读取两个sheet
data1 = pd.read_excel(file_path, sheet_name='test01')
data2 = pd.read_excel(file_path, sheet_name='test02')

# 给数据加上标签，方便后续扩展
data1['person'] = 'person1'
data2['person'] = 'person2'

# 合并数据
data = pd.concat([data1, data2], ignore_index=True)

# 只保留需要的列
columns = ['左眼X', '左眼Y', '右眼X', '右眼Y']

# 设置Matplotlib的中文字体（Windows系统可以改为SimHei或微软雅黑）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False  # 负号正常显示


# 相关系数+P值标注的函数
def corrfunc(x, y, **kws):
    r, p = stats.pearsonr(x, y)
    ax = plt.gca()
    ax.set_axis_off()  # 隐藏坐标轴
    color = 'red' if p < 0.05 else 'black'
    text = f"{r:.2f}"
    if p < 0.05:
        text += " *"
    ax.annotate(text, xy=(0.5, 0.5), xycoords=ax.transAxes, 
                ha='center', va='center', fontsize=12, color=color)


# 创建PairGrid
g = sns.PairGrid(data[columns], diag_sharey=False)

# 下三角绘制散点图
g.map_lower(sns.scatterplot, s=10, color='orange')

# 对角线绘制核密度图（KDE）
g.map_diag(sns.kdeplot, color='orange')

# 上三角绘制相关系数
g.map_upper(corrfunc)

# 设置标题
plt.suptitle("眼动数据的多变量相关性矩阵图", y=1.02, fontsize=16)

# 调整布局和保存图
plt.tight_layout()
plt.savefig('眼动数据相关矩阵图.png', dpi=300, bbox_inches='tight')
plt.show()