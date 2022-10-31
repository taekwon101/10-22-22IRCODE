import matplotlib.pyplot as plt
import APKCustomFunctions as apk

folderpath = r'CSVs\test1'
normalization_index = 2078

filelist = apk.FileSort(folderpath)
df_IR = apk.CSVsToDataframe(filelist, normalization_index)

print(df_IR.head(5))

df_IR.plot()
plt.show()