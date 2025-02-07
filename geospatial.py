import numpy as np
from math import cos, radians, degrees

class GeoSpatial:

    def __init__(self, grid_size, grid_side_length_m, grid_origin_lat_long, make_grid_during_init = True) -> None:
        self.grid_size = grid_size
        self.grid_side_length_m = grid_side_length_m
        self.grid_origin_lat_long = grid_origin_lat_long
        self.grid = None
        if make_grid_during_init:
            self.make_grid()
        
    def make_grid(self):
        self.grid = np.zeros((self.grid_size, self.grid_size))
        
    def transform_grid_point_to_lat_long(self, grid_point_xy):

        x = grid_point_xy[0]
        y = grid_point_xy[1]
        dist_x = self.grid_side_length_m * x
        dist_y = self.grid_side_length_m * y

        return self.get_lat_long_from_origin_offset(dist_x, dist_y)

    def get_lat_long_from_origin_offset(self, x_offset_m, y_offset_m):

        # Radius of the Earth in meters
        R = 6378137
        lat = self.grid_origin_lat_long[0]
        lon = self.grid_origin_lat_long[1]
        # Offsets in radians
        dLat = y_offset_m / R
        dLon = x_offset_m / (R * cos(radians(lat)))

        # New latitude and longitude in degrees
        new_lat = lat + degrees(dLat)
        new_lon = lon + degrees(dLon)

        return new_lat, new_lon