import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建一个绘图窗口，大小为8x6英寸
plt.figure(figsize=(8, 6))

# 绘制折线图
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')

# 添加图例，显示在右上角
plt.legend(loc='upper right')

# 添加标题和轴标签
plt.title('Sin and Cos functions')
plt.xlabel('x')
plt.ylabel('y')

# 显示网格线
plt.grid(True)

# 保存图像，支持多种格式，如PNG、PDF、SVG等
plt.savefig('line_plot.png', dpi=300)

# 显示图像
plt.show()
