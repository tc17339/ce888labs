#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




# def permutation(statistic, error):


def mad(arr):
    
        arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
        med = np.median(arr)

        return np.median(np.abs(arr - med))


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	df = df.dropna()

	print(df.columns)
        
	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)
   

	sns_plot.savefig("scate_vehi.png",bbox_inches='tight')
	sns_plot.savefig("scate_vehi.pdf",bbox_inches='tight')

	data = df.values.T[1]
	print(data)
	
	print((("Mean: %f")%(np.mean(data))))
	print((("Median: %f")%(np.median(data))))
	print((("Var: %f")%(np.var(data))))
	print((("std: %f")%(np.std(data))))
	print((("MAD: %f")%(mad(data))))

	plt.clf()
	sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('day') 
	axes.set_ylabel('Millons of pound in sales')

	sns_plot2.savefig("hist_vehi.png",bbox_inches='tight')
	sns_plot2.savefig("hist_vehi.pdf",bbox_inches='tight')
       
       


	
