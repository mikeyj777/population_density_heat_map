import numpy as np

from db_connection import get_data_table_return_as_dataframe

grid = np.zeros((1000,1000))

haz_study = get_data_table_return_as_dataframe('HazardStudy')

apple = 1
