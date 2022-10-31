import matplotlib.pyplot as plt
import numpy as np
import APKCustomFunctions as apk

folderpath = r'CSVs\test1'
normalization_index = 2078
averaging_index_low = 500
averaging_index_high = 600

filelist = apk.FileSort(folderpath)

df_IR, average_array = apk.CSVsToDataframe(filelist, normalization_index, averaging_index_low, averaging_index_high)

## BRUTE FORCE EXAMPLE FOR AVERAGE/STD DEV BAR GRAPHS ##
name_array = ['condition 1', 'condition 2', 'condition 3']

condition1_means_array = np.array(average_array[0:1])
condition2_means_array = np.array(average_array[2:3])
condition3_means_array = np.array(average_array[4:5])

condition1_mean_of_means = condition1_means_array.mean()
condition2_mean_of_means = condition2_means_array.mean()
condition3_mean_of_means = condition3_means_array.mean()

condition1_stddev_of_means = condition1_means_array.std()
condition2_stddev_of_means = condition2_means_array.std()
condition3_stddev_of_means = condition3_means_array.std()

all_means = [condition1_mean_of_means, condition2_mean_of_means, condition3_mean_of_means]
all_stds = [condition1_stddev_of_means, condition2_stddev_of_means, condition3_stddev_of_means]

plt.bar(name_array, all_means, yerr = all_stds)

## END OF BRUTE FORCE METHOD ##

# df_IR.plot()
plt.show()