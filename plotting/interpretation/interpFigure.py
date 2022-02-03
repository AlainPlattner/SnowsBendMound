import matplotlib.pyplot as plt
import numpy as np
from smoothLine import *


mound = np.loadtxt('profile_horizontal_edited.txt')

humus = np.loadtxt('../interfaces/humus.txt')
summitstruct1 =   np.loadtxt('../interfaces/summitStructure1.txt')
bottom = np.loadtxt('../interfaces/bottom.txt')
summitstruct2 =   np.loadtxt('../interfaces/summitStructure2.txt')
ground = np.loadtxt('../interfaces/ground.txt')
maybemound =  np.loadtxt('../interfaces/maybemound.txt')

trench = np.loadtxt('trench.txt')


#### If you want to create your own interface, set
#### wannapick to True
#wannapick = True
wannapick = False


## Smoothing the picked interfaces
# Replace the picked interfaces with oversampled moving averages
# ipbot = smoothLine(ipbot)
# ipramp =  smoothLine(ipramp)
# iptrans =  smoothLine(iptrans)
# reshumus =  smoothLine(reshumus)
# resburied =  smoothLine(resburied)

# # Plot the interfaces
intfcol = 'k' #'gray'
lw=1

plt.plot(humus[:,0], humus[:,1], '--', color=intfcol, linewidth=lw)
plt.plot(summitstruct1[:,0], summitstruct1[:,1], color=intfcol, linewidth=lw)

plt.plot(bottom[:,0], bottom[:,1], color=intfcol, linewidth=lw)
plt.plot(summitstruct2[:,0], summitstruct2[:,1], color=intfcol, linewidth=lw)

plt.plot(ground[:,0], ground[:,1], color=intfcol, linewidth=lw)

plt.plot(maybemound[:,0], maybemound[:,1], ':', color=intfcol, linewidth=lw)


plt.plot(trench[:,0], trench[:,1], '-', color='black', linewidth=lw)

plt.yticks(ticks=[-2,0,2,4])

plt.text(50.5, 2.1, 'U1')

# plot polygons
#ec=None
ec=intfcol


boundL = 33.1
boundR = 39.4

m2bL=32.6
m2bR=37.5

# # Original
# colgrnd = 'brown'
# colst1 = 'g'
# colst2 = 'magenta'
# colsum1 = 'cyan'
# colsum2 =  'yellow'

# colgrnd = '#AA4499'
# colst1 = '#882255'
# colst2 = '#117733'
# colsum1 = '#88CCEE'
# colsum2 =  '#DDCC77'

# colgrnd = '#FFB000'
# colst1 = '#785EF0'
# colst2 = '#DC267F'
# colsum1 = '#648FFF'
# colsum2 =  '#FE6100'

colgrnd = '#800000'
colst2 = '#f58231'
colst1 = '#000075'
colsum2 = '#ffe119'
colsum1 =  '#4363d8'

# Ground surface
top1a = mound[ mound[:,0]<=4.1, :]
deepend = [[60,-5],[0,-5]]
gnd1 = np.append(top1a, ground, axis=0)
gnd = np.append(gnd1, deepend, axis=0)
gndpg = plt.Polygon(gnd, color=colgrnd, alpha=0.5, ec=ec, label='ground')
plt.gca().add_patch(gndpg)


# Stage 2
top1ind = np.logical_and(  mound[:,0]>4.5 , mound[:,0]<m2bL )
top1 = mound[top1ind,:]
top2 = mound[(mound[:,0]>m2bR),:]
stg1 = np.append(bottom, ground[ground[:,0]>47, :] , axis=0)
stg1 = np.append(stg1, np.flipud(top2), axis=0) 
stg2 = np.append(np.flipud(summitstruct1), np.flipud(top1) ,axis=0)
stg2 = np.append(stg2, ground[ground[:,0]<10 ,: ] ,axis=-0)
stg = np.append(stg1, stg2, axis=0)
stgpg = plt.Polygon(stg, color=colst2, alpha=0.5, ec=ec, label='stage2')
plt.gca().add_patch(stgpg)


# Stage 1
top1 = bottom[ (bottom[:,0]<=boundL),:]
top2 = bottom[ (bottom[:,0]>=boundR),:]
top = np.append(np.flipud(top2), np.flipud(summitstruct2), axis=0)
top = np.append(top, np.flipud(top1), axis=0)
stage1botind = np.logical_and((ground[:,0]>=11.5) , (ground[:,0]<=52.5))
stage1bot = ground[stage1botind, :]
stage1 = np.append(stage1bot, top, axis=0)
stage1pg = plt.Polygon(stage1, color=colst1, alpha=0.5, ec=ec, label='stage 1')
plt.gca().add_patch(stage1pg)





# Summit structure 1
topind = np.logical_and((bottom[:,0]>=boundL) , (bottom[:,0]<=boundR))
top = bottom[topind,:]
sstr2 = np.append(summitstruct2, np.flipud(top), axis=0)
sstr2pg = plt.Polygon(sstr2, color=colsum1, alpha=0.5, ec=ec, label='summit structure 1')
plt.gca().add_patch(sstr2pg)

# Summit tructure 2
btopind = np.logical_and(mound[:,0]>=m2bL, mound[:,0]<=m2bR)
burtop = mound[btopind,:]
bur = np.append( burtop, np.flipud(summitstruct1), axis=0 )
burpg = plt.Polygon(bur, color=colsum2, alpha=0.5, ec=ec, label='summit structure 2')
plt.gca().add_patch(burpg)




# Plot the mound
plt.plot(mound[:,0], mound[:,1], '-k', linewidth=1.2)


#plt.gca().set_aspect('equal', 'box')
plt.gca().set_aspect(1.5, 'box')
plt.xlabel('profile [m]')
plt.ylabel('elevation [m]')
plt.ylim([0,5.5])
#plt.ylim([1.2,5.5])
#plt.ylim([-1,5.5])
plt.xlim([0,58.5])
plt.gca().xaxis.set_label_position('top')
plt.gca().xaxis.tick_top()
plt.legend(loc='upper center', ncol=3, fontsize=9, frameon=False, bbox_to_anchor=(0.5,0.07))

if wannapick:

    coords = plt.ginput(n=-1, timeout=-1)
    # mouse_add=<MouseButton.LEFT: 1>,
    # mouse_pop=<MouseButton.RIGHT: 3>,
    # mouse_stop=<MouseButton.MIDDLE: 2>
    
    points = np.array(coords)

    np.savetxt('picked.txt',points, delimiter='\t')

else:

    plt.savefig('interpretation.pdf', dpi=600)

    #plt.show()

