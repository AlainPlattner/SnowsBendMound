import matplotlib.pyplot as plt
import numpy as np
from smoothLine import *

#mound = np.loadtxt('profile_horizontal.txt')
mound = np.loadtxt('profile_horizontal_edited.txt')


# ipbot = np.loadtxt('pickedERTIP/picked-combo-ip-bottom.txt')
# ipramp = np.loadtxt('pickedERTIP/edited/picked-combo-ip-onramp.txt')
# #iptop = np.loadtxt('pickedERTIP/picked-combo-ip-top.txt')
# iptrans = np.loadtxt('pickedERTIP/edited/picked-combo-ip-uncertainTransition.txt')
#reshumus = np.loadtxt('pickedERTIP/picked-combo-res-humus.txt')
#reshumus = np.loadtxt('pickedERTIP/edited/newreshumus.txt')
#reshumus_new = np.loadtxt('pickedERTIP/picked-combo-res-humus_new.txt')

humus = np.loadtxt('../interfaces/humus.txt')
summitstruct1 =   np.loadtxt('../interfaces/summitStructure1.txt')
bottom = np.loadtxt('../interfaces/bottom.txt')
summitstruct2 =   np.loadtxt('../interfaces/summitStructure2.txt')
ground = np.loadtxt('../interfaces/ground.txt')
maybemound =  np.loadtxt('../interfaces/maybemound.txt')

#reshumusL = np.loadtxt('pickedERTIP/edited/picked_newreshumusL.txt')
#reshumusR = np.loadtxt('pickedERTIP/edited/picked_newreshumusR.txt')
#resburied = np.loadtxt('pickedERTIP/edited/newburiedstructure.txt')

#wannapick = True
wannapick = False


##### Do GPR
import gprpy.gprpy as gp
mygpr = gp.gprpyProfile()
mygpr.importdata('../../data/GPR/line2.dt1')
mygpr.setZeroTime(7)

mygpr.dewow(100)
mygpr.tpowGain(2)
#mygpr.tpowGain(0)
#mygpr.agcGain(100)
mygpr.setVelocity(0.08)
mygpr.topoCorrect('../../data/GPR/profile_horizontal.txt',delimiter='\t')

mygpr.showProfile(color='bwr', contrast=20, yrng=[-3,5], xrng=[0,58.9], asp=1.5)
#mygpr.showProfile(color='bwr', contrast=10, yrng=[-3,5], xrng=[0,58.9], asp=1.5)

plt.yticks(ticks=[-2,0,2,4])

# # Plot the interfaces
intfcol = 'black'
lw=1.5

#humus = smoothLine(humus)
#summitstruct1 = smoothLine(summitstruct1)

#reshumus =  smoothLine(reshumus)
#resburied =  smoothLine(resburied)
#ipbot = smoothLine(ipbot)
#ipramp =  smoothLine(ipramp)
#iptrans =  smoothLine(iptrans)



plt.plot(humus[:,0], humus[:,1], '--', color=intfcol, linewidth=lw)
plt.plot(summitstruct1[:,0], summitstruct1[:,1], color=intfcol, linewidth=lw)

plt.plot(bottom[:,0], bottom[:,1], color=intfcol, linewidth=lw)
plt.plot(summitstruct2[:,0], summitstruct2[:,1], color=intfcol, linewidth=lw)

plt.plot(ground[:,0], ground[:,1], color=intfcol, linewidth=lw)

plt.plot(maybemound[:,0], maybemound[:,1], ':', color=intfcol, linewidth=lw)


# # plot polygons

# ec=None

# # SummitStructure1 poly
# m2bL=32.6
# m2bR=37.5
# btopind = np.logical_and(mound[:,0]>=m2bL, mound[:,0]<=m2bR)
# burtop = mound[btopind,:]
# bur = np.append( burtop, np.flipud(summitstruct1), axis=0 )
# burpg = plt.Polygon(bur, color='yellow', alpha=0.5, ec=ec)
# plt.gca().add_patch(burpg)

# # Humus
# top1 = mound[(mound[:,0]<m2bL),:]
# top2 = mound[(mound[:,0]>m2bR),:]
# hum1 = np.append(humus, np.flipud(top2), axis=0) 
# hum2 = np.append(np.flipud(summitstruct1), np.flipud(top1) ,axis=0)
# hum = np.append(hum1, hum2, axis=0)
# humpg = plt.Polygon(hum, color='g', alpha=0.5, ec=ec)
# plt.gca().add_patch(humpg)

# # Stage2
# stage2 = np.append(bottom, np.flipud(humus), axis=0)
# # Now add top until first humus point
# topend = mound[(mound[:,0] <= humus[0,0]),:]
# stage2 = np.append(stage2, np.flipud(topend), axis=0)
# st2pg = plt.Polygon(stage2, color='red', alpha=0.5, ec=ec)
# plt.gca().add_patch(st2pg)

# # Summit structure2
# boundL = 33.1
# boundR = 39.4
# topind = np.logical_and((bottom[:,0]>=boundL) , (bottom[:,0]<=boundR))
# top = bottom[topind,:]
# sstr2 = np.append(summitstruct2, np.flipud(top), axis=0)
# sstr2pg = plt.Polygon(sstr2, color='cyan', alpha=0.5, ec=ec)
# plt.gca().add_patch(sstr2pg)

# # Stage1
# stage1 = [[0,-5],[60,-5]]
# top1 = bottom[ (bottom[:,0]<=boundL)]
# top2 = bottom[ (bottom[:,0]>=boundR)]
# top = np.append(np.flipud(top2), np.flipud(summitstruct2), axis=0)
# top = np.append(top, np.flipud(top1), axis=0)
# stage1 = np.append(stage1, top, axis=0)
# stage1pg = plt.Polygon(stage1, color='magenta', alpha=0.5, ec=ec)
# plt.gca().add_patch(stage1pg)






# Plot the mound
plt.plot(mound[:,0], mound[:,1], '-k', linewidth=1.2)


#plt.gca().set_aspect('equal', 'box')
plt.gca().set_aspect(1.5, 'box')
#plt.gca().set_aspect(2, 'box')
#plt.xlabel('profile [m]')
plt.ylabel('elevation [m]')
plt.ylim([0,5.5])
#plt.ylim([1.2,5.5])
#plt.ylim([-1,5.5])
plt.xlim([0,58.5])
plt.gca().get_xaxis().set_ticklabels([])
plt.xlabel('')


if wannapick:

    coords = plt.ginput(n=-1, timeout=-1)
    # mouse_add=<MouseButton.LEFT: 1>,
    # mouse_pop=<MouseButton.RIGHT: 3>,
    # mouse_stop=<MouseButton.MIDDLE: 2>
    
    points = np.array(coords)

    np.savetxt('picked.txt',points, delimiter='\t')

else:

    plt.savefig('interpretation_GPR_lines.pdf', dpi=600)

    #plt.show()


############### Takeouts:

# # Single humus
# m2humL=10
# m2humR=55
# humtopind = np.logical_and(mound[:,0]>m2humL, mound[:,0]<m2humR)
# humtop = mound[ humtopind ,:]
# hum = np.append(humtop, np.flipud(reshumus), axis=0)
# humpg = plt.Polygon(hum, color='g', alpha=0.5)
# plt.gca().add_patch(humpg)
