# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 10:18:49 2019

@author: snopok
"""
#%%
from pylab import *
import pandas as pd

rcParams["font.size"] = 12.0

reference=pd.read_csv('reference/hadron.dat',delim_whitespace=True,skiprows=3).values
missing_fins=pd.read_csv('missing_fins/hadron.dat',delim_whitespace=True,skiprows=3).values
density_98=pd.read_csv('density_98/hadron.dat',delim_whitespace=True,skiprows=3).values
density_96=pd.read_csv('density_96/hadron.dat',delim_whitespace=True,skiprows=3).values
density_94=pd.read_csv('density_94/hadron.dat',delim_whitespace=True,skiprows=3).values
density_92=pd.read_csv('density_92/hadron.dat',delim_whitespace=True,skiprows=3).values
density_90=pd.read_csv('density_90/hadron.dat',delim_whitespace=True,skiprows=3).values
spot_size_09=pd.read_csv('spot_size_09/hadron.dat',delim_whitespace=True,skiprows=3).values
spot_size_11=pd.read_csv('spot_size_11/hadron.dat',delim_whitespace=True,skiprows=3).values
spot_size_13=pd.read_csv('spot_size_13/hadron.dat',delim_whitespace=True,skiprows=3).values
spot_size_15=pd.read_csv('spot_size_15/hadron.dat',delim_whitespace=True,skiprows=3).values
spot_size_17=pd.read_csv('spot_size_17/hadron.dat',delim_whitespace=True,skiprows=3).values
beam_position_m02_p00=pd.read_csv('beam_position_-0.2_+0.0/hadron.dat',delim_whitespace=True,skiprows=3).values
beam_position_m01_p00=pd.read_csv('beam_position_-0.1_+0.0/hadron.dat',delim_whitespace=True,skiprows=3).values



#%% missing fins
figure(1)

subplot(221)
reference_hist=hist2d(reference[:,0],reference[:,1],50,vmin=0,vmax=4000,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Reference run (pencil beam)')
colorbar()

subplot(222)
missing_fins_hist=hist2d(missing_fins[:,0],missing_fins[:,1],50,vmin=0,vmax=4000,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Missing fins #18, 19, 20, 21')
colorbar()

subplot(223)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(missing_fins[:,3]**2+missing_fins[:,4]**2+missing_fins[:,5]**2),50,log=True,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Log scale')
title('Log scale momentum distribution')
legend(('Nominal case','Missing fins'))
grid(True)

subplot(224)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(missing_fins[:,3]**2+missing_fins[:,4]**2+missing_fins[:,5]**2),50,log=False,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Linear scale')
title('Linear scale momentum distribution')
legend(('Nominal case','Missing fins'))
grid(True)

#%% changing density
figure(2)

subplot(221)
reference_hist=hist2d(reference[:,0],reference[:,1],50,vmin=0,vmax=4200,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Reference run (pencil beam)')
colorbar()

subplot(222)
density_90_hist=hist2d(density_90[:,0],density_90[:,1],50,vmin=0,vmax=4200,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Density reduced to 90%')
colorbar()

subplot(223)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(density_98[:,3]**2+density_98[:,4]**2+density_98[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(density_96[:,3]**2+density_96[:,4]**2+density_96[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(density_94[:,3]**2+density_94[:,4]**2+density_94[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(density_92[:,3]**2+density_92[:,4]**2+density_92[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(density_90[:,3]**2+density_90[:,4]**2+density_90[:,5]**2),50,log=True,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Log scale')
title('Log scale momentum distribution')
legend(('Nominal case','98% density','96% density','94% density','92% density','90% density'),loc=9)
grid(True)

subplot(224)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(density_98[:,3]**2+density_98[:,4]**2+density_98[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(density_96[:,3]**2+density_96[:,4]**2+density_96[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(density_94[:,3]**2+density_94[:,4]**2+density_94[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(density_92[:,3]**2+density_92[:,4]**2+density_92[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(density_90[:,3]**2+density_90[:,4]**2+density_90[:,5]**2),50,log=False,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Linear scale')
title('Linear scale momentum distribution')
legend(('Nominal case','98% density','96% density','94% density','92% density','90% density'),loc=9)
grid(True)

#%% missing fins vs reduced density
figure(3)

subplot(221)
missing_fins_hist=hist2d(missing_fins[:,0],missing_fins[:,1],50,vmin=0,vmax=4200,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Missing fins #18, 19, 20, 21')
colorbar()

subplot(222)
density_90_hist=hist2d(density_90[:,0],density_90[:,1],50,vmin=0,vmax=4200,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Density reduced to 90%')
colorbar()

subplot(223)
hist(sqrt(missing_fins[:,3]**2+missing_fins[:,4]**2+missing_fins[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(density_90[:,3]**2+density_90[:,4]**2+density_90[:,5]**2),50,log=True,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Log scale')
title('Log scale momentum distribution')
legend(('Missing fins','90% density'),loc=9)
grid('on')

subplot(224)
hist(sqrt(missing_fins[:,3]**2+missing_fins[:,4]**2+missing_fins[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(density_90[:,3]**2+density_90[:,4]**2+density_90[:,5]**2),50,log=False,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Linear scale')
title('Linear scale momentum distribution')
legend(('Missing fins','90% density'),loc=9)
grid('on')

#%% spot_size 0.9 mm
figure(4)

subplot(221)
reference_hist=hist2d(reference[:,0],reference[:,1],50,vmin=0,vmax=3200,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Reference run (pencil beam)')
colorbar()

subplot(222)
spot_size_09_hist=hist2d(spot_size_09[:,0],spot_size_09[:,1],50,vmin=0,vmax=3200,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Spot size 0.9 mm')
colorbar()

subplot(223)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(spot_size_09[:,3]**2+spot_size_09[:,4]**2+spot_size_09[:,5]**2),50,log=True,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Log scale')
title('Log scale momentum distribution')
legend(('Pencil beam','Spot size 0.9 mm'))
grid(True)

subplot(224)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(spot_size_09[:,3]**2+spot_size_09[:,4]**2+spot_size_09[:,5]**2),50,log=False,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Linear scale')
title('Linear scale momentum distribution')
legend(('Pencil beam','Spot size 0.9 mm'))
grid(True)

#%% spot_size 1.5 mm
figure(5)

subplot(221)
reference_hist=hist2d(reference[:,0],reference[:,1],50,vmin=0,vmax=11000,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Reference run (pencil beam)')
colorbar()

subplot(222)
spot_size_15_hist=hist2d(spot_size_15[:,0],spot_size_15[:,1],50,vmin=0,vmax=11000,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Spot size 1.5 mm')
colorbar()

subplot(223)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(spot_size_15[:,3]**2+spot_size_15[:,4]**2+spot_size_15[:,5]**2),50,log=True,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Log scale')
title('Log scale momentum distribution')
legend(('Pencil beam','Spot size 1.5 mm'))
grid(True)

subplot(224)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(spot_size_15[:,3]**2+spot_size_15[:,4]**2+spot_size_15[:,5]**2),50,log=False,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Linear scale')
title('Linear scale momentum distribution')
legend(('Pencil beam','Spot size 1.5 mm'))
grid(True)

#%% changing beam spot size
figure(6)

subplot(231)
spot_size_09_hist=hist2d(spot_size_09[:,0],spot_size_09[:,1],50,vmin=0,vmax=11000,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Spot size 0.9 mm')
colorbar()

subplot(232)
spot_size_11_hist=hist2d(spot_size_11[:,0],spot_size_11[:,1],50,vmin=0,vmax=11000,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Spot size 1.1 mm')
colorbar()

subplot(234)
spot_size_11_hist=hist2d(spot_size_13[:,0],spot_size_13[:,1],50,vmin=0,vmax=11000,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Spot size 1.3 mm')
colorbar()

subplot(235)
spot_size_15_hist=hist2d(spot_size_15[:,0],spot_size_15[:,1],50,vmin=0,vmax=11000,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Spot size 1.5 mm')
colorbar()

subplot(233)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(spot_size_09[:,3]**2+spot_size_09[:,4]**2+spot_size_09[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(spot_size_11[:,3]**2+spot_size_11[:,4]**2+spot_size_11[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(spot_size_13[:,3]**2+spot_size_13[:,4]**2+spot_size_13[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(spot_size_15[:,3]**2+spot_size_15[:,4]**2+spot_size_15[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(spot_size_17[:,3]**2+spot_size_17[:,4]**2+spot_size_17[:,5]**2),50,log=True,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Log scale')
title('Log scale momentum distribution')
legend(('Pencil beam','0.9 mm spot','1.1 mm spot','1.3 mm spot','1.5 mm spot','1.7 mm spot'),loc=9)
grid(True)

subplot(236)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(spot_size_09[:,3]**2+spot_size_09[:,4]**2+spot_size_09[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(spot_size_11[:,3]**2+spot_size_11[:,4]**2+spot_size_11[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(spot_size_13[:,3]**2+spot_size_13[:,4]**2+spot_size_13[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(spot_size_15[:,3]**2+spot_size_15[:,4]**2+spot_size_15[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(spot_size_17[:,3]**2+spot_size_17[:,4]**2+spot_size_17[:,5]**2),50,log=False,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Linear scale')
title('Linear scale momentum distribution')
legend(('Pencil beam','0.9 mm spot','1.1 mm spot','1.3 mm spot','1.5 mm spot','1.7 mm spot'),loc=9)
grid(True)

#%% beam position scan
figure(7)

subplot(221)
reference_hist=hist2d(reference[:,0],reference[:,1],50,vmin=0,vmax=3000,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Reference run (pencil beam)')
colorbar()

subplot(222)
beam_position_m02_p00_hist=hist2d(beam_position_m02_p00[:,0],beam_position_m02_p00[:,1],50,vmin=0,vmax=3000,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Beam position x=-0.2 mm, y=0.0 mm')
colorbar()

subplot(223)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=True,histtype='step',range=(0,125000))
hist(sqrt(beam_position_m02_p00[:,3]**2+beam_position_m02_p00[:,4]**2+beam_position_m02_p00[:,5]**2),50,log=True,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Log scale')
title('Log scale momentum distribution')
legend(('Reference run','x=-0.2 mm'))
grid(True)

subplot(224)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=False,histtype='step',range=(0,125000))
hist(sqrt(beam_position_m02_p00[:,3]**2+beam_position_m02_p00[:,4]**2+beam_position_m02_p00[:,5]**2),50,log=False,histtype='step',range=(0,125000))
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Linear scale')
title('Linear scale momentum distribution')
legend(('Reference run','x=-0.2 mm'))
grid(True)

#%%
figure(8)

ax=subplot(121)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=True,histtype='step',range=(0,20000),linewidth=2)
hist(sqrt(spot_size_09[:,3]**2+spot_size_09[:,4]**2+spot_size_09[:,5]**2),50,log=True,histtype='step',range=(0,20000),linewidth=2)
hist(sqrt(spot_size_11[:,3]**2+spot_size_11[:,4]**2+spot_size_11[:,5]**2),50,log=True,histtype='step',range=(0,20000),linewidth=2)
hist(sqrt(spot_size_13[:,3]**2+spot_size_13[:,4]**2+spot_size_13[:,5]**2),50,log=True,histtype='step',range=(0,20000),linewidth=2)
hist(sqrt(spot_size_15[:,3]**2+spot_size_15[:,4]**2+spot_size_15[:,5]**2),50,log=True,histtype='step',range=(0,20000),linewidth=2)
hist(sqrt(spot_size_17[:,3]**2+spot_size_17[:,4]**2+spot_size_17[:,5]**2),50,log=True,histtype='step',range=(0,20000),linewidth=2)
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Log scale')
title('Log scale momentum distribution')
legend(('Pencil beam','0.9 mm spot','1.1 mm spot','1.3 mm spot','1.5 mm spot','1.7 mm spot'),loc=9)
ax.axis((0,20000,5e2,5e5))
grid(True)

subplot(122)
hist(sqrt(reference[:,3]**2+reference[:,4]**2+reference[:,5]**2),50,log=False,histtype='step',range=(0,20000),linewidth=2)
hist(sqrt(spot_size_09[:,3]**2+spot_size_09[:,4]**2+spot_size_09[:,5]**2),50,log=False,histtype='step',range=(0,20000),linewidth=2)
hist(sqrt(spot_size_11[:,3]**2+spot_size_11[:,4]**2+spot_size_11[:,5]**2),50,log=False,histtype='step',range=(0,20000),linewidth=2)
hist(sqrt(spot_size_13[:,3]**2+spot_size_13[:,4]**2+spot_size_13[:,5]**2),50,log=False,histtype='step',range=(0,20000),linewidth=2)
hist(sqrt(spot_size_15[:,3]**2+spot_size_15[:,4]**2+spot_size_15[:,5]**2),50,log=False,histtype='step',range=(0,20000),linewidth=2)
hist(sqrt(spot_size_17[:,3]**2+spot_size_17[:,4]**2+spot_size_17[:,5]**2),50,log=False,histtype='step',range=(0,20000),linewidth=2)
xlabel('$P_{total}$ [MeV/$c$]')
ylabel('Linear scale')
title('Linear scale momentum distribution')
legend(('Pencil beam','0.9 mm spot','1.1 mm spot','1.3 mm spot','1.5 mm spot','1.7 mm spot'),loc=9)
grid(True)

#%% missing fins vs reduced density - differential histogram
figure(3,figsize=(9,3))

subplot(131)
missing_fins_hist=hist2d(missing_fins[:,0],missing_fins[:,1],50,vmin=0,vmax=4200,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Missing fins #18, 19, 20, 21')
colorbar()

subplot(132)
density_90_hist=hist2d(density_90[:,0],density_90[:,1],50,vmin=0,vmax=4200,range=((-1000.,1000.),(-1000.,1000.)))
xlabel('x [mm]')
ylabel('y [mm]')
title('Density reduced to 90%')
colorbar()

subplot(133)
density_missing_fins_diff_hist=imshow(density_90_hist[0]-missing_fins_hist[0],extent=(-1000,1000,-1000,1000),cmap='jet')
xlabel('x [mm]')
ylabel('y [mm]')
title('Difference between the histograms')
colorbar()
