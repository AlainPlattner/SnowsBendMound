import numpy as np
from copy import copy

xyz = np.loadtxt('SnowsMoundElecXYZ.txt', delimiter = '\t')

#xyzloc = np.array([ [xyz[:,0]-np.min(xyz[:,0])], [xyz[:,1]-np.min(xyz[:,1])] , [xyz[:,2]] ])

xyzloc = copy(xyz)
xyzloc[:,0] = xyz[:,0]-np.min(xyz[:,0])
xyzloc[:,1] = xyz[:,1]-np.min(xyz[:,1])

np.savetxt( 'XYZ_local.txt', xyzloc, delimiter='\t' )


xyzall = np.append(xyzloc, xyz, axis=1)

np.savetxt( 'XYZ_loc_glob.txt', xyzall, delimiter='\t' )
