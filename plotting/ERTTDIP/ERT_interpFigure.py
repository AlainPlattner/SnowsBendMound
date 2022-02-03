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


#### If you would like to create your own interfaces, you can set "wannapick"
#### to True
#wannapick = True
wannapick = False

#showcol = True
showcol = False



###### Import ERT / TDIP
import pybert as pb
import pygimli as pg
from pybert import tdip
import os
savename = os.path.join('..','..','processing','ERTTDIP','inversionResults','SNOWSMOUND-merged')

ip = tdip.TDIPdata()
ip.basename = savename
ip.loadResults(loadColeCole=True)
ip.coverage = np.loadtxt(ip.basename+'.cog')
# Set time gates
delay = 0.01
dt = [0.0166667, 0.0333333, 0.05, 0.0666667, 0.0833333, 0.1, 0.133333, 0.166667, 0.216667, 0.283333, 0.366666, 0.483333, 0.6, 0.8]
# We can't use "set gates", because no IP data is loaded. So just set dt
ip.dt = np.array(dt)
# Calculate Mint
imax = 10
Mint = np.array( (np.matrix(ip.dt[0:imax])*np.matrix(ip.M[0:imax,:])).transpose() ).squeeze()
ip.Mint = Mint

#fig, ax = plt.subplots(figsize=(7.2,4.8))
fig, ax = plt.subplots()



a = pg.show(ip.pd, ip.res, cMin=50, cMax=200, ax=ax, label='res', cMap='cividis', colorBar=False, logScale=True)#True)
figname='interpretation_Res_lines.pdf'
intfcol = 'silver'#'gray'
    
plt.yticks(ticks=[-2,0,2,4])

ax=a[0]
#a[1].remove()


#ax.set_aspect(1.5)

# # Plot the interfaces

lw=1.5

##### If you like you can smooth the lines:
# ipbot = smoothLine(ipbot)
# ipramp =  smoothLine(ipramp)
# iptrans =  smoothLine(iptrans)
# reshumus =  smoothLine(reshumus)
# resburied =  smoothLine(resburied)
# humus = smoothLine(humus)
# summitstruct1 = smoothLine(summitstruct1)
# bottom = smoothLine(bottom)
# summitstruct2 = smoothLine(summitstruct2)


plt.plot(humus[:,0], humus[:,1], '--' ,color=intfcol, linewidth=lw)
plt.plot(summitstruct1[:,0], summitstruct1[:,1], color=intfcol, linewidth=lw)

plt.plot(bottom[:,0], bottom[:,1], color=intfcol, linewidth=lw)
plt.plot(summitstruct2[:,0], summitstruct2[:,1], color=intfcol, linewidth=lw)

plt.plot(ground[:,0], ground[:,1], color=intfcol, linewidth=lw)

plt.plot(maybemound[:,0], maybemound[:,1], ':', color=intfcol, linewidth=lw)


# Plot the mound
ax.plot(mound[:,0], mound[:,1], '-k', linewidth=1.2)

#ax.set_aspect('equal', 'box')
plt.gca().set_aspect(1.5, 'box')
#ax.set_aspect(1.5,'box')

#ax.set_xlabel('profile [m]')
ax.set_ylabel('elevation [m]')
ax.set_ylim([0,5.5])
#plt.ylim([1.2,5.5])
#plt.ylim([-1,5.5])
ax.set_xlim([0,58.5])
#ax.xaxis.set_label_position('top')
ax.get_xaxis().set_ticklabels([])
ax.xaxis.tick_top()

if wannapick:

    coords = plt.ginput(n=-1, timeout=-1)
    # mouse_add=<MouseButton.LEFT: 1>,
    # mouse_pop=<MouseButton.RIGHT: 3>,
    # mouse_stop=<MouseButton.MIDDLE: 2>
    
    points = np.array(coords)

    np.savetxt('picked.txt',points, delimiter='\t')

else:

    if showcol:
        mappable = a[0].collections[0]
        fig = a[0].figure
        cbar_ax = fig.add_axes([0.91, 0.413, 0.01, 0.165])

        cbar = fig.colorbar(mappable, cax=cbar_ax, format='%g',label='resistivity [$\Omega$m]') #, ticks=[50, 70, 100, 140, 200]
        figname='interpretation_Res_lines_colbar.pdf'

    plt.savefig(figname, dpi=600)

    #plt.show()
