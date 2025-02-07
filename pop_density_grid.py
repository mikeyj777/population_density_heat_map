import numpy as np

from db_connection import get_data_table_return_as_dataframe
from geospatial import GeoSpatial

grid_size = 100
grid_spacing_m = 30
grid_origin_lat_long = [36.509145, -82.558015]

geosp = GeoSpatial(grid_size=grid_size, grid_side_length_m=grid_spacing_m, grid_origin_lat_long=grid_origin_lat_long)
grid = geosp.grid

haz_study = get_data_table_return_as_dataframe('HazardStudy')



apple = 1
