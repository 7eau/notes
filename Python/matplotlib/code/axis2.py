import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth = 1.0, linestyle = '--')

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1,2,4)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ \alpha\ bad$', r'$bad$', r'$normal$', r'$good$', r'$very good$'])

# gca = 'get current axis'
ax = plt.gca()
# 设置右、上轴消失
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 设置x轴， y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 设置坐标原点
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))


plt.show()