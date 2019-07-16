import pandas as pd
from Speed_test import Speed_test
from Vertical_Lateral_Dist import *
from Gender_and_adulthood import *
%matplotlib inline
import statsmodels.api as sm
import matplotlib.pyplot as plt

# GET DATA CREATE NEW FEATURES
raw_animal_data = get_animal_data()
animal_data = create_new_features(raw_animal_data)
animal_data.to_csv('animal_data.csv')
# comment above, uncomment below if you have animal_data.csv
# animal_data = pd.read_csv('animal_data.csv')

# FIRST HYPOTHESIS TEST
animal_1 = 'Bull Shark (Carcharhinus leucas)'
animal_2 = 'Dolphin (Delphinus capensis)'
st = Speed_test(animal_data, animal_1, animal_2)
# uncomment to view QQ plot
# sm.qqplot(st.res, line='45', fit=True)
# plt.show()
plt.bar([animal_1, animal_2], [st.animal_1_avg, st.animal_2_avg])
plt.title('Average Speed')
plt.xlabel('Species')
plt.ylabel('Average Speed (MPH)')
plt.show()
print('TEST 1\nIndependent T Test\n\tT = {}\n\tP = {}'.format(st.ttest.statistic, st.ttest.pvalue))
print('Levene Test (for homogeneity of variance)\n\tT = {}\n\tP = {}\n'.format(st.levene.statistic, st.levene.pvalue))

# SECOND HYPOTHESIS TEST
vert_vs_lat = Vertical_Lateral_Dist(animal_data)
print("TEST 2")
for species, tstat in vert_vs_lat.tstats:
    print('{}\n\tT = {}\n\tP = {}'.format(species, tstat.statistic, tstat.pvalue))
vert_vs_lat.graph_ratios()

# THIRD TEST
gender_vs_adulthood = Gender_and_adulthood(animal_data)
print('\nTEST3\nGender vs. Adulthood\n\tZ = {}\n\tP = {}'.format(gender_vs_adulthood.z, gender_vs_adulthood.p))
gender_vs_adulthood.graph_adulthood()
