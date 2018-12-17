import xarray as xr
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


TEMP_ctrl=xr.open_dataset('/short/e14/lp0975/processed_CESM/merged_out/v1p2p2_B1850_f19g16_conf9_HybR701.TEMP.000101-018012.nc',decode_times=False, chunks={'time':100,'z_t':20})

TEMP_ctrl=TEMP_ctrl.stack(grid_cells=('nlat', 'nlon'))

TEMP_ctrl = TEMP_ctrl.chunk({'time':100,'z_t':20,'grid_cells':1000})


ngrids=TEMP_ctrl.TEMP.values.shape[2]
ntimes=TEMP_ctrl.TEMP.values.shape[0]

#initialize thermocline depth
TCLN_ctrl=TEMP_ctrl.mean(dim=['time','z_t'])


#function to calculate the thermocline over a TEMP profile (x)
y = TEMP_ctrl.TEMP.z_t.values[:]
def tcln_depth(x):
    mask = ~np.isnan(x) & ~np.isnan(y)
    f=interp1d(x[mask], y[mask], kind='slinear')
    xx=np.linspace(np.min(x[mask]),np.max(x[mask]),x.shape[0]*2)
    g=np.diff(f(xx))/np.diff(xx)
    A=f(xx)[np.where(np.abs(g)==np.min(np.abs(g)))[0]]
    if len(depth)>1:
        depth=np.mean(A)
    elif len(depth)==1
        depth=A[0]
    else
        raise ValueError('depth was not found???... find out why')
    return(depth)


#LOOP? to calculate thermocline everywhere
for t in range(ntimes):
    #apply tcln_depth function in each "grid_cell" to find teh depth of the thermocline around the world oceans

#save the result to a new dataset... the way I normally do it is by replacing the values on TCLN_ctrl.values
#In this way I keep all the previous metadata from the original TEMP file, except for the z_t and time dimensions

#save the processed dataset to netcdf
#END
