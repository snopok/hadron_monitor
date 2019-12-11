# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 10:18:49 2019

@author: snopok
"""
#%%
from pylab import *
import pandas as pd

rcParams["font.size"] = 12.0

peak=8000

reference=pd.read_csv('../spot_size_15/hadron.dat',delim_whitespace=True,skiprows=3).values

beam_position_m02_p00=pd.read_csv('beam_position_-0.2_+0.0/hadron.dat',delim_whitespace=True,skiprows=3).values
beam_position_p02_p00=pd.read_csv('beam_position_+0.2_+0.0/hadron.dat',delim_whitespace=True,skiprows=3).values
beam_position_p00_m02=pd.read_csv('beam_position_+0.0_-0.2/hadron.dat',delim_whitespace=True,skiprows=3).values
beam_position_p00_p02=pd.read_csv('beam_position_+0.0_+0.2/hadron.dat',delim_whitespace=True,skiprows=3).values

#%% beam position scan
figure(0)

subplot(335)
plot(-500,-500,'',color='yellow')
legend(('Max # 11298',))
reference_hist=hist2d(reference[:,0],reference[:,1],25,vmin=0,vmax=peak,range=((-500.,500.),(-500.,500.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Reference run (spot size 1.5 mm)')
colorbar()

subplot(334)
plot(-500,-500,'',color='yellow')
legend(('Max # 12469',))
beam_position_m02_p00_hist=hist2d(beam_position_m02_p00[:,0],beam_position_m02_p00[:,1],25,vmin=0,vmax=peak,range=((-500.,500.),(-500.,500.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Beam position x=-0.2 mm, y=0.0 mm')
colorbar()

subplot(336)
plot(-500,-500,'',color='yellow')
legend(('Max # 11826',))
beam_position_p02_p00_hist=hist2d(beam_position_p02_p00[:,0],beam_position_p02_p00[:,1],25,vmin=0,vmax=peak,range=((-500.,500.),(-500.,500.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Beam position x=+0.2 mm, y=0.0 mm')
colorbar()

subplot(338)
plot(-500,-500,'',color='yellow')
legend(('Max # 9938',))
beam_position_p00_m02_hist=hist2d(beam_position_p00_m02[:,0],beam_position_p00_m02[:,1],25,vmin=0,vmax=peak,range=((-500.,500.),(-500.,500.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Beam position x=0.0 mm, y=-0.2 mm')
colorbar()

subplot(332)
plot(-500,-500,'',color='yellow')
legend(('Max # 14727',))
beam_position_p00_p02_hist=hist2d(beam_position_p00_p02[:,0],beam_position_p00_p02[:,1],25,vmin=0,vmax=peak,range=((-500.,500.),(-500.,500.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Beam position x=0.0 mm, y=+0.2 mm')
colorbar()
