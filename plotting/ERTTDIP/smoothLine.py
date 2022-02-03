import numpy as np

def smoothLine(xy, npts=500, win=11):
    # win must be odd!!!
    
    # Create high-res version of the x-coordinate
    x = np.linspace(np.min(xy[:,0]), np.max(xy[:,0]), npts)
    # Make the y coordinate high-resolution too
    y = np.interp(x, xy[:,0], xy[:,1])
    # extend the y values to avoid edge effect
    ylong = np.append( y[0]*np.ones( int((win-1)/2) ), np.append(y, y[-1]*np.ones( int((win-1)/2) ) )  )
    ysmooth = np.convolve(ylong, np.ones(win)/win, mode='valid')
    x = x[:,np.newaxis]
    ysmooth = ysmooth[:,np.newaxis]
    
    xysmooth = np.append(x,ysmooth, axis=1)
    
    return xysmooth
