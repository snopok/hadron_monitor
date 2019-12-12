# hadron_monitor
NuMI beam line hadron monitor simulation for NOvA

beam_position set of folders: unsuccessful test of moving the beam on target, with pencil beam there is very little effect, see "large_spot" for a simulation with a 1.5-mm beam spot, 1 M PoT

large_spot: moving the beam on target by +/-2 mm, beam spot size 1.5 mm, 1 M PoT

density_*: reducing target density from 100% to 90% using a 2% step size (90% density result looks similar to the missing fin simulation)

missing_fins: fins #18, 19, 20, 21 removed, results are similar to that with the 90% density target

spot_size_*: comparing different spot sizes on target. NOTE: if you need a reference simulation with larger beam spot sizes, pick one of these folders

reference: pencil beam reference simulation

field_maps: a dedicated folder with Horn 1 and Horn 2 field maps. Update "field_map_directory" parameter in G4beamline deck or using a command-line parameter to point to this folder

plots: various PNG/PDF/SVG plots, file names should be self-explanatory. Most of the plots produced using hadron_monitor_analysis.py script in the root folder


