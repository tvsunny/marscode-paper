import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

# 指定字体路径
# 修复：使用原始字符串字面量或双反斜杠来表示路径中的反斜杠
font_path ='simhei.ttf'
# 添加字体
font_manager.fontManager.addfont(font_path)

# 设置字体
plt.rcParams['font.family'] = 'SimHei'

# 绘制图形
plt.plot([1, 2, 3, 4])
plt.xlabel('横轴')
plt.ylabel('纵轴')
plt.title('示例图形')
# 保存图形到本地
plt.savefig('test.png')
# 显示图形
plt.show()