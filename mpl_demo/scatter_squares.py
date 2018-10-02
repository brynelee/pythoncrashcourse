#-*-coding:utf-8-*-
import matplotlib
import matplotlib.pyplot as plt

myfont_simhei = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf') #Windows系统，黑体
myfont_simsun = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc') #Windows系统，宋体

#myfont = matplotlib.font_manager.FontProperties(fname='/home/Fonts/simhei.ttf') #Linux系统，黑体

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, s=40)
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=100)
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=100)
plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues,
            edgecolor='none', s=100) # 颜色映射

# 设置图表标题并给坐标轴加上标签
plt.title(u"平方数图表", fontsize=24,fontproperties=myfont_simhei)
plt.xlabel("Value", fontsize=14)
plt.ylabel("平方数", fontsize=14,fontproperties=myfont_simsun)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
# plt.axis([0, 20, 0, 400])

# plt.show() # 显示图表
plt.savefig('squares_plot.png', bbox_inches='tight')