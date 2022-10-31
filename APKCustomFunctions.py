import pandas as pd
import numpy as np
import glob, os

def FileSort(folder_readpath):
    '''takes a folder path as input and returns the alphabetically sorted list of CSVs within that folder'''
    
    os.chdir(folder_readpath)
    filelist = sorted(glob.glob('*.csv'))
    
    return filelist


def ConvertTransToAbs(trans_raw):
    '''takes list-like IR data and if it looks like transmittance (fractional, not %), converts it to absorbance'''
    
    if np.amax(trans_raw) > 20:
        transArray = np.array(trans_raw)
        abs_raw = -1 * np.log(transArray)
        return abs_raw
    else:
        return trans_raw


def Normalize(abs_raw, WN_normal):
    '''takes raw absorbance spectra and the array index for its normalization value and returns the normalized array'''
    
    abs_normalized = abs_raw / WN_normal
    
    return abs_normalized


def CSVsToDataframe(CSVList, normalization_index):
    '''Takes list of CSVs and the index of the normalization absorbance and reads them into a Pandas Dataframe'''
    
    # INITIALIZE FILES AND VARIABLES #
    columnname = CSVList[0][0:-4]
    df_IR = pd.read_csv(CSVList[0], skiprows = 2, header = None, names = ['cm-1', columnname], index_col = ['cm-1'])
    df_IR = df_IR.sort_values(by = ['cm-1'], ignore_index = True)

    # LOOP THROUGH CSVs ADDING EACH TO DATAFRAME #
    for CSV in CSVList:
        columnname = CSV[0:-4]
        df_add = pd.read_csv(CSV, skiprows = 2, header = None, names = ['cm-1', columnname])
        df_add = df_add.sort_values(by=['cm-1'], ignore_index = True)
        IR_array = df_add[columnname].to_numpy()
        abs_array = ConvertTransToAbs(IR_array)
        df_IR[columnname] = Normalize(abs_array, df_add[columnname][normalization_index])

    return df_IR