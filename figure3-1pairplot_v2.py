import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# 读取Excel数据
file_path = '测试数据.xlsx'

data1 = pd.read_excel(file_path, sheet_name='test01')
data2 = pd.read_excel(file_path, sheet_name='test02')

data1['person'] = 'person1'
data2['person'] = 'person2'
data = pd.concat([data1, data2], ignore_index=True)

columns = ['左眼X', '左眼Y', '右眼X', '右眼Y']

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置图形边框
plt.figure(figsize=(10,8), facecolor='white')
plt.gcf().patch.set_edgecolor('black')
plt.gcf().patch.set_linewidth(3)

def corrfunc(x, y, **kws):
    r, p = stats.pearsonr(x, y)
    ax = plt.gca()
    ax.set_axis_off()
    color = 'red' if p < 0.05 else 'black'
    text = f"{r:.2f}"
    if p < 0.05:
        text += " *"
    ax.annotate(text, xy=(0.5, 0.5), xycoords=ax.transAxes,
                ha='center', va='center', fontsize=12, color=color)

g = sns.PairGrid(data[columns], diag_sharey=False)

g.map_lower(sns.scatterplot, s=10, color='orange')
g.map_diag(sns.kdeplot, color='orange')
g.map_upper(corrfunc)

# 设置子图边框颜色
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for i, ax_row in enumerate(g.axes):
    for j, ax in enumerate(ax_row):
        for spine in ax.spines.values():
            spine.set_color(colors[i%4])
            spine.set_linewidth(2)

plt.suptitle("眼动数据的多变量相关性矩阵图", y=1.0, fontsize=16)
plt.tight_layout()
plt.savefig('眼动数据相关矩阵图_v2.png', dpi=300, bbox_inches='tight')
plt.show()