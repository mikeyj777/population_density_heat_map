import numpy as np
import pandas as pd
from db_connection import get_data_table_return_as_dataframe
from geospatial import GeoSpatial

grid_size = 100
grid_spacing_m = 30
# grid_origin_lat_long = [36.509145, -82.558015]
grid_origin_lat_long = [36.55072, -82.525554]
geosp = GeoSpatial(grid_size=grid_size, grid_side_length_m=grid_spacing_m, grid_origin_lat_long=grid_origin_lat_long)
grid = geosp.grid


haz_study = get_data_table_return_as_dataframe('HazardStudy')

# get the grid points that equate to the approx lat/long of the target table release points.  
    # confirm that the point isn't too far from the grid lat/long.
# apply the population density to the grid cell and surrounding cells
    # if the cells have higher densities already, do not overwrite.



for _, row in haz_study.iterrows():
    lat = row['ApproxLatitude']
    if pd.isna(lat):
        continue
    long = row['ApproxLongitude']
    if pd.isna(long) is None:
        continue
    day_occ = row['ProcAreaPopDensity']
    night_occ = row['NightProcAreaPopDensity']
    occ = 0
    if not pd.isna(day_occ) and isinstance(day_occ, (int, float)) and not isinstance(day_occ, bool):
        occ = day_occ
    if not pd.isna(night_occ) and isinstance(night_occ, (int, float)) and not isinstance(night_occ, bool):
        occ = max(day_occ, night_occ)
    if occ == 0:
        continue
    grid_point_xy = geosp.get_grid_point_xy_from_lat_long(lat = lat, long=long)
    x = grid_point_xy[0]
    y = grid_point_xy[1]
    if x < 0 or y < 0 or x > grid.shape[0] or y > grid.shape[1]:
        continue
    for i in range(2):
        i_pos = i - 2
        if x + i_pos < 0 or x + i_pos > grid.shape[0]:
            continue
        for j in range(2):
            j_pos = j-2
            if y + j_pos < 0 or y + j_pos > grid.shape[1]:
                continue
            if grid[x + i_pos, y + j_pos] < occ:
                grid[x + i_pos, y + j_pos] = occ
    

apple = 1
