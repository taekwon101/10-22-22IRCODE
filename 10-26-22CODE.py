import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import APKCustomFunctions as apk

folderpath = r'CSVs\test1'
normalization_index = 2078

filelist = apk.FileSort(folderpath)

file1 = r'D:\221026_IR\10-26_uncuredx1000dilution_1.csv'
file2 = r'D:\221026_IR\10-26_uncuredx1000dilution_2.csv'
file3 = r'D:\221026_IR\10-26_uncuredx1000dilution_3.csv'
file4 = r'D:\221026_IR\10-26_uncuredx1000dilution_4.csv'
file5 = r'D:\221026_IR\10-26_uncuredx1000dilution_5.csv'
file6 = r'D:\221026_IR\10-26_13Amps1secx1000dilution_1.csv'
file7 = r'D:\221026_IR\10-26_13Amps1secx1000dilution_2.csv'
file8 = r'D:\221026_IR\10-26_13Amps1secx1000dilution_3.csv'
file9 = r'D:\221026_IR\10-26_13Amps1secx1000dilution_4.csv'
file10 = r'D:\221026_IR\10-26_13Amps1secx1000dilution_5.csv'
file11 = r'D:\221026_IR\10-26_13Amps4secx1000dilution_1.csv'
file12 = r'D:\221026_IR\10-26_13Amps4secx1000dilution_2.csv'
file13 = r'D:\221026_IR\10-26_13Amps4secx1000dilution_3.csv'
file14 = r'D:\221026_IR\10-26_13Amps4secx1000dilution_4.csv'
file15 = r'D:\221026_IR\10-26_13Amps4secx1000dilution_5.csv'
file16 = r'D:\221026_IR\10-26_13Amps6secx1000dilution_1.csv'
file17 = r'D:\221026_IR\10-26_13Amps6secx1000dilution_2.csv'
file18 = r'D:\221026_IR\10-26_13Amps6secx1000dilution_3.csv'
file19 = r'D:\221026_IR\10-26_13Amps6secx1000dilution_4.csv'
file20 = r'D:\221026_IR\10-26_13Amps6secx1000dilution_5.csv'
file21 = r'D:\221026_IR\10-26_curedx1000dilution_1.csv'
file22 = r'D:\221026_IR\10-26_curedx1000dilution_2.csv'
file23 = r'D:\221026_IR\10-26_curedx1000dilution_3.csv'
file24 = r'D:\221026_IR\10-26_curedx1000dilution_4.csv'
file25 = r'D:\221026_IR\10-26_curedx1000dilution_5.csv'

df = pd.read_csv(file1, skiprows = 1)
df2 = pd.read_csv(file2, skiprows = 1)
df3 = pd.read_csv(file3, skiprows = 1)
df4 = pd.read_csv(file4, skiprows = 1)
df5 = pd.read_csv(file5, skiprows = 1)
df6 = pd.read_csv(file6, skiprows = 1)
df7 = pd.read_csv(file7, skiprows = 1)
df8 = pd.read_csv(file8, skiprows = 1)
df9 = pd.read_csv(file9, skiprows = 1)
df10 = pd.read_csv(file10, skiprows = 1)
df11 = pd.read_csv(file11, skiprows = 1)
df12 = pd.read_csv(file12, skiprows = 1)
df13 = pd.read_csv(file13, skiprows = 1)
df14 = pd.read_csv(file14, skiprows = 1)
df15 = pd.read_csv(file15, skiprows = 1)

df16 = pd.read_csv(file16, skiprows = 1)
df17 = pd.read_csv(file17, skiprows = 1)
df18 = pd.read_csv(file18, skiprows = 1)
df19 = pd.read_csv(file19, skiprows = 1)
df20 = pd.read_csv(file20, skiprows = 1)
df21 = pd.read_csv(file21, skiprows = 1)
df22 = pd.read_csv(file22, skiprows = 1)
df23 = pd.read_csv(file23, skiprows = 1)
df24 = pd.read_csv(file24, skiprows = 1)
df25 = pd.read_csv(file25, skiprows = 1)

df_norm = df["A"][2078]
df["A"] = df["A"]/df_norm

df2_norm = df2["A"][2078]
df2["A"] = df2["A"]/df2_norm

df3_norm = df3["A"][2078]
df3["A"] = df3["A"]/df3_norm

df4_norm = df4["A"][2078]
df4["A"] = df4["A"]/df4_norm

df5_norm = df5["A"][2078]
df5["A"] = df5["A"]/df5_norm

df6_norm = df6["A"][2078]
df6["A"] = df6["A"]/df6_norm

df7_norm = df7["A"][2078]
df7["A"] = df7["A"]/df7_norm

df8_norm = df8["A"][2078]
df8["A"] = df8["A"]/df8_norm

df9_norm = df9["A"][2078]
df9["A"] = df9["A"]/df9_norm

df10_norm = df10["A"][2078]
df10["A"] = df10["A"]/df10_norm

df11_norm = df11["A"][2078]
df11["A"] = df11["A"]/df11_norm

df12_norm = df12["A"][2078]
df12["A"] = df12["A"]/df12_norm

df13_norm = df13["A"][2078]
df13["A"] = df13["A"]/df13_norm

df14_norm = df14["A"][2078]
df14["A"] = df14["A"]/df14_norm

df15_norm = df15["A"][2078]
df15["A"] = df15["A"]/df15_norm

df16_norm = df16["A"][2078]
df16["A"] = df16["A"]/df16_norm

df17_norm = df17["A"][2078]
df17["A"] = df17["A"]/df17_norm

df18_norm = df18["A"][2078]
df18["A"] = df18["A"]/df18_norm

df19_norm = df19["A"][2078]
df19["A"] = df19["A"]/df19_norm

df20_norm = df20["A"][2078]
df20["A"] = df20["A"]/df20_norm

df21_norm = df21["A"][2078]
df21["A"] = df21["A"]/df21_norm

df22_norm = df22["A"][2078]
df22["A"] = df22["A"]/df22_norm

df23_norm = df23["A"][2078]
df23["A"] = df23["A"]/df23_norm

df24_norm = df24["A"][2078]
df24["A"] = df24["A"]/df24_norm

df25_norm = df25["A"][2078]
df25["A"] = df25["A"]/df25_norm

ax = df.plot (x='cm-1',y='A')

df2.plot (x='cm-1',y='A', ax=ax)
df3.plot (x='cm-1',y='A', ax=ax)
df4.plot (x='cm-1',y='A', ax=ax)
df5.plot (x='cm-1',y='A', ax=ax)
df6.plot (x='cm-1',y='A', ax=ax)
df7.plot (x='cm-1',y='A', ax=ax)
df8.plot (x='cm-1',y='A', ax=ax)
df9.plot (x='cm-1',y='A', ax=ax)
df10.plot (x='cm-1',y='A', ax=ax)
df11.plot (x='cm-1',y='A', ax=ax)
df12.plot (x='cm-1',y='A', ax=ax)
df13.plot (x='cm-1',y='A', ax=ax)
df14.plot (x='cm-1',y='A', ax=ax)
df15.plot (x='cm-1',y='A', ax=ax)
df16.plot (x='cm-1',y='A', ax=ax)
df17.plot (x='cm-1',y='A', ax=ax)
df18.plot (x='cm-1',y='A', ax=ax)
df19.plot (x='cm-1',y='A', ax=ax)
df20.plot (x='cm-1',y='A', ax=ax)
df21.plot (x='cm-1',y='A', ax=ax)
df22.plot (x='cm-1',y='A', ax=ax)
df23.plot (x='cm-1',y='A', ax=ax)
df24.plot (x='cm-1',y='A', ax=ax)
df25.plot (x='cm-1',y='A', ax=ax)

# plt.legend(['5 amps1', '5 amps2', '5 amps3', '5 amps4', '5 amps5', '10 amps1', '10 amps2', '10 amps3', '10 amps4', '10 amps5', '13 amps1', '13 amps2', '13 amps3', '13 amps4', '13 amps5', 'Uncured1', 'Uncured2', 'Uncured3', 'Uncured4', 'Uncured5', 'Cured1', 'Cured2', 'Cured3', 'Cured4', 'Cured5'])
plt.title("Normalized IR Absorption Readings per cbPDMS Sample")
plt.xlabel("Wavenumber (cm-1)")
plt.ylabel("Absorbance")

plt.show()