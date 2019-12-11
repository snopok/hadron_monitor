# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 10:18:49 2019

@author: snopok
"""
#%%
from pylab import *
import pandas as pd

rcParams["font.size"] = 12.0

peak=1000

reference=pd.read_csv('../spot_size_15/hadron.dat',delim_whitespace=True,skiprows=3).values

magnetic_field=pd.read_csv('hadron.dat',delim_whitespace=True,skiprows=3).values

#%% beam position scan
figure(0)

subplot(221)
axis((-500.,500.,-500.,500.))
#plot(-1000,-1000,'',color='yellow')
#legend(('Max # 11298',))
reference_hist=hist2d(reference[:115160,0],reference[:115160,1],25,vmin=0,vmax=peak,range=((-500.,500.),(-500.,500.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Reference run (spot size 1.5 mm)')
colorbar()

subplot(222)
axis((-500.,500.,-500.,500.))
#plot(-1000,-1000,'',color='yellow')
#legend(('Max # 12469',))
magnetic_field_hist=hist2d(magnetic_field[:,0],magnetic_field[:,1],25,vmin=0,vmax=peak,range=((-500.,500.),(-500.,500.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('With magnetic field in the decay pipe')
colorbar()

# %%
subplot(223)
#plot(-1000,-1000,'',color='yellow')
#legend(('Max # 11826',))
magnetic_field_diff_hist=imshow((magnetic_field_hist[0]-reference_hist[0]).T,extent=(-500,500,-500,500),cmap='jet')
xlabel('x [mm]')
ylabel('y [mm]')
title('Difference histogram')
colorbar()

subplot(224)
#plot(-1000,-1000,'',color='yellow')
#legend(('Max # 9938',))
magnetic_field_ratio_hist=imshow((magnetic_field_hist[0]/reference_hist[0]).T,extent=(-500,500,-500,500),cmap='jet')
xlabel('x [mm]')
ylabel('y [mm]')
title('Ratio histogram')
colorbar()

