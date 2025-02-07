import numpy as np

from db_connection import get_data_table_return_as_dataframe
from geospatial import GeoSpatial

grid_size = 100
grid_spacing_m = 30
grid_origin_lat_long = [36.509145, -82.558015]

geosp = GeoSpatial(grid_size=grid_size, grid_side_length_m=grid_spacing_m, grid_origin_lat_long=grid_origin_lat_long)
grid = geosp.grid

haz_study = get_data_table_return_as_dataframe('HazardStudy')

# get the grid points that equate to the approx lat/long of the target table release points.  
    # confirm that the point isn't too far from the grid lat/long.
# apply the population density to the grid cell and surrounding cells
    # if the cells have higher densities already, do not overwrite.

apple = 1
