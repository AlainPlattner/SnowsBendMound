import pybert as pb
import pygimli as pg
from pybert import tdip
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os


#### Also load electrode locations
elecs3d = np.loadtxt('../../data/XYZ_local.txt')

elecXstep = np.diff(elecs3d[:,0])
elecYstep = np.diff(elecs3d[:,1])
elecprofile = np.cumsum( np.sqrt(np.power(elecXstep,2.)+np.power(elecYstep,2.))  )

elecprofile = np.append(0., elecprofile)
elecelev = elecs3d[:,2]-np.min(elecs3d[:,2])


#elecs = np.append( np.sqrt(np.power(elecs3d[:,0],2.) + np.power(elecs3d[:,1],2.)), ,axis=1 )

figname =  'SNOWSMOUND-merged'
savename = os.path.join('../../processing/ERTTDIP/inversionResults','SNOWSMOUND-merged')
remcol = False
remax = False


ip = tdip.TDIPdata()
ip.basename = savename
# Load results
ip.loadResults(loadColeCole=True)
# Load coverage
ip.coverage = np.loadtxt(ip.basename+'.cog')

#### Renormalize coverage
cov = (ip.coverage - np.min(ip.coverage))/(np.max(ip.coverage) - np.min(ip.coverage)) 

# Set time gates
delay = 0.01
dt = [0.0166667, 0.0333333, 0.05, 0.0666667, 0.0833333, 0.1, 0.133333, 0.166667, 0.216667, 0.283333, 0.366666, 0.483333, 0.6, 0.8]
# We can't use "set gates", because no IP data is loaded. So just set dt
ip.dt = np.array(dt)

# calculate Mint
imax = 10
Mint = np.array( (np.matrix(ip.dt[0:imax])*np.matrix(ip.M[0:imax,:])).transpose() ).squeeze()
ip.Mint = Mint


#### Integrated chargeability


#print(np.min(Mint*1000))
#print(np.max(Mint*1000))
fig, ax = plt.subplots(figsize=(7.2,4.8))
a = pg.show(ip.pd, Mint*1000, cMin=4, cMax=20, ax=ax, cMap='inferno', logScale=True, colorBar=False)#, pad=0.1, size='20%')
#a = pg.show(ip.pd, Mint*1000, cMin=4, cMax=20, label='integrated chargeability [msec]', cMap='inferno', logScale=True, pad=0.2, size='10%')
a[0].set_xlim([0,58])
a[0].set_ylim([-0.7,5.5])
a[0].xaxis.tick_top()
a[0].set_ylabel('elevation [m]')
a[0].xaxis.set_label_position('top')
if remcol:
    a[1].remove()
if remax:
    a[0].get_xaxis().set_ticklabels([])
else:
    a[0].set_xlabel('profile position [m]')
   
a[0].set_yticks(ticks=[-2,0,2,4])  
a[0].set_aspect(1.5,'box')

a[0].plot(elecprofile, elecelev, '|k', markersize=4)
    
mappable = a[0].collections[0]
fig = a[0].figure  
# cbar_ax = fig.add_axes([0.125, 0.34, 0.775, 0.02])
# cbar = fig.colorbar(mappable, cax=cbar_ax, orientation="horizontal", ticks=[4, 6, 9, 13, 20], format='%g', label='integrated chargeability [msec]')

#cbar_ax = fig.add_axes([0.91, 0.395, 0.01, 0.2])
cbar_ax = fig.add_axes([0.91, 0.383, 0.01, 0.225])
cbar = fig.colorbar(mappable, cax=cbar_ax, ticks=[4, 6, 9, 13, 20], format='%g',label='chargeability [msec]')
    
plt.savefig('%s-IntCharg10.pdf' %(figname))

