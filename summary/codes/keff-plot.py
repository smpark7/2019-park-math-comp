import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

temp = [900, 950, 1000, 1030, 1050, 1100, 1150, 1200]
keff = [1.01081, 1.00693, 1.00332, 1.00091, 0.999482, 0.995789, 0.992008, \
        0.988428]
reac = [(i-1)/i for i in keff]

slope, intercept, r_value, p_value, std_err = stats.linregress(temp, reac)
line = slope*np.array(temp)+intercept

fig, ax = plt.subplots(figsize=(12,10))
ax.grid()
ax.plot(temp, reac, marker='.', markersize='10', linestyle='None')
ax.plot(temp, line)
#ax.legend(prop={'size': 20})
ax.set_xlabel('Temperature [K]',fontsize=24)
ax.set_ylabel('Reactivity', fontsize=24)
title = 'Reactivity vs Temperature [K]'
plt.title(title, fontsize=26)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.tight_layout()
#plt.savefig('BWR_Quality_and_Critical_Quality', dpi=300)

print(slope)
print((reac[-1] - reac[0]) / 300)