# First import all the packages we need
import pybert as pb
import pygimli as pg
from pybert import tdip
import matplotlib.pyplot as plt
import numpy as np
import os
from createInterfaceMesh import *

##### Import data

# Here, set which one you want to invert:
# This here is the 50% duty cycle
#filename = os.path.join('data','BACKYARD-PLA-50_Plattner4andDip_data.txt')
# I used the "os.path.join" function because Windows has different backslashes
# Than Linux / Mac

# This here is the data
filename = '../../data/mergedDataERT-TDIP.txt' 

# To save figures
figname =  os.path.join('figures','SNOWSMOUND-merged')

# What name do you want to give the saved results?
savename = os.path.join('inversionResults','SNOWSMOUND-merged')

# Must load and set the time gates. These are given in the header,
# But I don't have a good way of loading them automatically.
# Make sure this is the same as header field "IP_WindowSecList".
# Delay is the first field here, then the dt values of the time integration
# windows

delay = 0.01
dt = [0.0166667, 0.0333333, 0.05, 0.0666667, 0.0833333, 0.1, 0.133333, 0.166667, 0.216667, 0.283333, 0.366666, 0.483333, 0.6, 0.8]

# Now load
ip = tdip.TDIPdata(filename)
ip.setGates(dt=dt, delay=delay)


##### Check data quality

# First you want to check the pseudosections of the apparent resistivity
# and apparent chargeability for the different time windows. Remove data points
# that are bad
#ip.generateDataPDF(basename=figname)
## This only needs to be done once, or when you filter the data!!!


# It is always a good idea to have a look at the decay curves.
# They should be smoothly decaying.
#ip.generateDecayPDF(basename=figname)
## This only needs to be done once, or when you filter the data!!!
## It is quite time consuming, so don't do it each time you run an inversion!

# Sometimes, two decay curves have the same color. To identify which one is
# which, plot both using this:
# ip.showDecay(ab=[31,67],mn=[43,55])
# pg.wait()

# If you need to, you can use the filter function to kick out bad data points
#ip.filter(emax=0.05)
# You can also remove specific measurements or delete time windows from all data
# May not be necessary if the data are good.
### If the same measurement is made twice (e.g. because of merged data),
### then just put the same a,b,m,n twice in the list

badData = np.loadtxt('badData-merged.txt',delimiter=',')
for i in range(0,badData.shape[0]):
    nr = ip.getDataIndex(abmn=badData[i,:])
    print(badData[i,:])
    ip.filter(nr=nr)

    

# #### Invert data
# # You can start with the standard grid and invert both ERT and TDIP together:
#ip.simultaneousInversion()
#ip.individualInversion()

# # You will need to change the grid to better interpret the subsurface. This is just a first check. To change the grid, see instructions in the other codes I had sent you

### Better mesh
#ertmanager = pg.physics.ert.ERTManager()
#mesh = ertmanager.createMesh(data=ip.data, quality=33, area=-1, paraDX=0.05, paraMaxCellSize=0.5,paraDepth=2)
#pg.show(mesh)
#pg.wait()

ertmanager = pg.physics.ert.ERTManager()
mesh = ertmanager.createMesh(data=ip.data, quality=33, area=-1, paraDX=0.08, paraMaxCellSize=0.4,paraDepth=2)

#mesh = createInterfaceMesh(data=ip.data, filename='interface_charg.txt', quality=33, area=-1, paraDX=0.04, paraMaxCellSize=0.3,paraDepth=2)

ip.simultaneousInversion(mesh=mesh,blockyModel=True,robustData=True)

#ip.individualInversion(mesh=mesh,blockyModel=True,robustData=True)


#### See, what sum of the windows shows (integral chargeability)
#Mint = np.sum(ip.M,axis=0)
#### To only use the first k=10 time windows:
# Mint = np.array( (np.matrix(ip.dt[0:10])*np.matrix(ip.M[0:10,:])).transpose() ).squeeze()
#Mint = np.array( (np.matrix(ip.dt)*np.matrix(ip.M)).transpose() ).squeeze()



# # The inversion result gives us IP decay values in the individual cells. This can be difficult to interpret because weak variations can happen between them that are hard to see. What can make interpretation easier is to fit, for each cell, the decay curve with a parameterized curve. A popular choice is the "Cole-Cole Model", which depends on three parameters: Chargeability (m), relaxation time (tau), frequency exponent (c).
# # Let's fit such Cole-Cole models for each cell to obtain these three parameters for each cell:
ip.fitModelDecays(useColeCole=True)




# #### Create figures of results
# # This will create figures of the resistivity, chargeability, relaxation time, and frequency exponent
ip.showColeColeResults()

# # This saves the figures
ip.saveFigures(basename=figname)


# #### Save inversion results. You can plot them later and with different ranges:
# name = os.path.join('results',savename)
ip.saveResults(basename=savename)
# Save coverage
np.savetxt(savename+'.cog',ip.coverage)

# Can recalculate these from the saved inversion results
#np.savetxt(savename+'.Mint',Mint)


# # Also save Cole-Cole results
ip.saveFit(basename=savename)
