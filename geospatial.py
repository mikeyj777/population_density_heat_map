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
        # x, y point is the southwest corner of the grid cell.
        self.grid = np.full((self.grid_size, self.grid_size), None)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                ll = self.transform_grid_point_to_lat_long((i, j))
                self.grid[i, j] = {
                    'lat': ll[0],
                    'long': ll[1],
                    'occupancy': 0
                }

        
    def transform_grid_point_to_lat_long(self, grid_point_xy):

        x = grid_point_xy[0]
        y = grid_point_xy[1]
        dist_x = self.grid_side_length_m * x
        dist_y = self.grid_side_length_m * y

        self.get_lat_long_from_origin_offset(dist_x, dist_y)

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
    
    def get_grid_point_xy_from_lat_long(self, lat, long):

        # Radius of the Earth in meters
        R = 6378137

        # Convert latitude and longitude from degrees to radians
        lat1 = radians(self.grid_origin_lat_long[0])
        lon1 = radians(self.grid_origin_lat_long[1])
        lat2 = radians(lat)
        lon2 = radians(long)

        # Compute differences in coordinates
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Calculate the offset in x and y directions
        x_offset = R * dlon * cos((lat1 + lat2) / 2)
        y_offset = R * dlat



        return int(x_offset / self.grid_side_length_m), int(y_offset / self.grid_side_length_m)