import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

class Vertical_Lateral_Dist:

    def __init__(self, animal_data):
        self.animal_data = animal_data
        self.ratios, self.tstats = self.get_ratios_and_tstats()

    def get_ratios_and_tstats(self):
        ratios = {}
        tstats = {}
        for genus in self.animal_data.species.unique():
            verts = self.animal_data[self.animal_data.species == genus].vertical_dist
            lats = self.animal_data[self.animal_data.species == genus].lateral_dist
            ratio = verts.sum()/lats.sum()
            t_results = stats.ttest_ind(verts, lats)
            tstats.update({genus: t_results})
            if t_results.pvalue < .05:
                ratios.update({genus: ratio})
        ratios = sorted(ratios.items(), key=lambda kv: kv[1])
        tstats = sorted(tstats.items(), key=lambda kv: kv[1][1])
        # pop where not enough data
        ratios.pop()
        ratios.pop()
        return ratios, tstats

    def graph_ratios(self):
        xs = [ratio[0] for ratio in self.ratios]
        ys = [ratio[1] for ratio in self.ratios]
        ax = sns.barplot(xs, ys)
        loc, labels = plt.xticks()
        ax.set_xticklabels(labels, rotation=90)
        ax.set_ylim(1, 1.8)
        ax.set_xlabel('Species')
        ax.set_ylabel('Vertical/Lateral Distance')
        ax.set_title('Ratio of Vertical Distance to Lateral Distance')
        plt.show()
