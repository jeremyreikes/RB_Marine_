from statsmodels.stats.proportion import proportions_ztest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class Gender_and_adulthood:
    def __init__(self, animal_data):
        self.animal_data = animal_data
        self.calc_adulthood_by_gender()

    def calc_adulthood_by_gender(self):
        all_males = self.animal_data[self.animal_data['gender'] == 'Male']
        num_adult_males = all_males[all_males['is_adult'] == True].id.nunique()
        self.prop_male_adults = num_adult_males/all_males.id.nunique()

        all_females = self.animal_data[self.animal_data['gender'] == 'Female']
        num_adult_females = all_females[all_females['is_adult']].id.nunique()
        self.prop_female_adults = num_adult_females/all_females.id.nunique()

        self.props = np.array([self.prop_male_adults, self.prop_female_adults])
        self.num_unique = np.array ([all_males.id.nunique(), all_females.id.nunique()])

        self.z, self.p = proportions_ztest(self.props, self.num_unique, alternative='two-sided')
        #p-value > alpha (0.05)

    def graph_adulthood(self):
        data = pd.DataFrame({'gender': ['Male', 'Female'], 'prop': [self.prop_male_adults, self.prop_female_adults]})
        sns.barplot(x = 'gender', y = 'prop', data = data)
        plt.xlabel('Gender')
        plt.ylabel('Ratio of adults vs total animals for each gender')
        plt.title('Proportions of animals classified as adults by gender')
        plt.show()
