import pandas as pd
from calc_between_rows import *
import numpy as np
def create_new_features(animal_data):
    distances = list()
    times = list()
    lateral_dist = list()
    vertical_dist = list()
    for index, row in animal_data.iloc[:-1].iterrows():
        row2 = animal_data.iloc[index+1]
        distances.append(dist_btw_ping(row, row2))
        times.append(time_btw_ping(row, row2))
        lateral_dist.append(lateral_distance(row, row2))
        vertical_dist.append(vertical_distance(row, row2))

    animal_data['distance_between_pings'] = pd.Series(distances)
    animal_data['time_between_pings'] = pd.Series(times)
    animal_data['vertical_dist'] = pd.Series(vertical_dist)
    animal_data['lateral_dist'] = pd.Series(lateral_dist)
    animal_data['is_adult'] = animal_data.stageOfLife == 'Adult'
    animal_data.gender.replace('N/A', np.nan, inplace=True)
    animal_data['distance_between_pings'].fillna(0, inplace=True)
    animal_data.drop(animal_data.tail(1).index, inplace=True)
    animal_data['speeds'] = animal_data.distance_between_pings / animal_data.time_between_pings
    return animal_data
