import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.figure(figsize=(16,12),dpi=300)
x=np.array([1,2,3,4,5,6,7,8,9])
x=np.arange(0,10,0.5)
y=np.sin(x)
plt.plot(x,y,label='sine',color='m',linewidth='2',marker='*',markersize='10',markeredgecolor='yellow',linestyle='--')
plt.title('X=Ysqured',fontdict={'fontname': 'Courier New','fontsize':25})
plt.xlabel('X axis',fontdict={'fontname': 'Courier New','fontsize':25})
plt.ylabel('Y axis',fontdict={'fontname': 'Courier New','fontsize':25})
plt.xticks([1,2,3,4,5,6,7])
plt.yticks([-1, -0.5 ,0 ,0.5, 1])
plt.legend()
plt.savefig('mygrap.png')
plt.show()