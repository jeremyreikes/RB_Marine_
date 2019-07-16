import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

class Speed_test:
    def __init__(self, animal_data, animal_1_name, animal_2_name):
        self.animal_data = animal_data
        self.animal_1_name = animal_1_name
        self.animal_2_name = animal_2_name
        self.test_species_speed(animal_1_name, animal_2_name)

    def test_species_speed(self, animal_1_name, animal_2_name):
        indices_to_drop = self.animal_data[self.animal_data.distance_between_pings == 0].index
        speed_data = self.animal_data.drop(indices_to_drop)

        animal_1 = speed_data[speed_data.species == animal_1_name].speeds
        animal_1 = animal_1[animal_1 < 21] # remove outliers
        self.animal_1_avg = animal_1.mean()

        animal_2 = speed_data[speed_data.species == animal_2_name].speeds
        animal_2 = animal_2[animal_2 < 21]
        self.animal_2_avg = animal_2.mean()
        
        shorter_length = len(animal_1) if len(animal_1) < len(animal_2) else len(animal_2)
        animal_1 = np.random.choice(animal_1, size=shorter_length)
        animal_2 = np.random.choice(animal_2, size=shorter_length)

        self.ttest = stats.ttest_ind(animal_1, animal_2)
        self.levene = stats.levene(animal_1, animal_2)
        res = animal_1 - animal_2
        self.res = res
