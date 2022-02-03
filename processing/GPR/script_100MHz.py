import gprpy.gprpy as gp
mygpr = gp.gprpyProfile()
mygpr.importdata('../../data/GPR/line2.dt1')
mygpr.setZeroTime(7)
mygpr.dewow(100)
mygpr.tpowGain(2)
mygpr.setVelocity(0.08)
mygpr.topoCorrect('../../data/GPR/profile_horizontal.txt',delimiter='\t')
#mygpr.printProfile('../figures/100MHz_raw_vel0.08.pdf', color='bwr', contrast=20, yrng=[-3,5], xrng=[0,58.9], dpi=600, asp=1)






import numpy as np
import matplotlib.pyplot as plt
#mygpr.showProfile(color='bwr', contrast=20, yrng=[-3,5], xrng=[0,58.7], asp=1.5)
#plt.yticks(ticks=[-2,0,2,4])
### The above for Paper. The below for talk
mygpr.showProfile(color='bwr', contrast=20, yrng=[-3,5], xrng=[0,58.7], asp=1)



plt.savefig('100MHz_dew100_vel08.pdf', dpi=600)
#plt.savefig('../figures/100MHz_raw_vel08.pdf', dpi=600)


# Show with picked lines

# wid=2

# intf = np.loadtxt('100MHz-dew100_vel08_top1_profile.txt',delimiter='\t')
# plt.plot(intf[:,0], intf[:,1],'--k',linewidth=wid)
# plt.plot(intf[:,0], intf[:,1],'--',color='yellow',linewidth=wid*0.25)

# intf = np.loadtxt('100MHz-dew100_vel08_longbottom_profile.txt',delimiter='\t')
# plt.plot(intf[:,0], intf[:,1],'--k',linewidth=wid)
# plt.plot(intf[:,0], intf[:,1],'--',color='yellow',linewidth=wid*0.25)


# plt.savefig('100MHz_dew100_vel08_showPicked.pdf', dpi=600)
# #plt.savefig('../figures/100MHz_raw_vel08_showPicked.pdf', dpi=600)
