import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()


plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1,2,4)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ \alpha\ bad$', r'$bad$', r'$normal$', r'$good$', r'$very good$'])

l1, = plt.plot(x, y2, label = 'up')
l2, = plt.plot(x, y1, color='red', linewidth = 1.0, linestyle = '--', label = 'down')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')




# 图例
plt.legend(handles=[l1, l2], loc='lower left')
# plt.legend()



plt.show()
