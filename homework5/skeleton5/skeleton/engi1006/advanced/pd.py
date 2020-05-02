import pandas as pd
import numpy as np

def advancedStats(data, labels):
    '''Advanced stats should leverage pandas to calculate
    some relevant statistics on the data.

    data: numpy array of data
    labels: numpy array of labels
    '''
    # convert to dataframe
    df = pd.DataFrame(data)

    # print skew and kurtosis for every column
    for index,(kur,ske) in enumerate(zip(df.kurtosis(axis=1),df.skew(axis=1))):
        print(
"""
  Column {index} statistics:
      Skewness:{ske}    Kurtosis:{kur}
""".format(index=index,ske=ske,kur=kur)
              )
    # assign in labels
    df["labels"] = labels
    
    # print(df.columns)
    # print(df.labels)
    print("\n\nDataframe statistics")

    # groupby labels into "benign" and "malignant"
    BM_mean = df.groupby('labels').mean()
    BM_std = df.groupby('labels').std()
    print(BM_mean)
    print(BM_std)
    # benign = df.loc[df.labels == 'B',:]
    # malignant = df.loc[df.labels == 'M',:]
 
    
    # collect means and standard deviations for columns,
    # grouped by label
    
    # Print mean and stddev for Benign
    print("Benign Stats:")
    print('Mean:\n')
    print(BM_mean.loc['B',:])
    print('Std:\n')
    print(BM_std.loc['B',:])
    
    print("\n")

    # Print mean and stddev for Malignant
    print("Malignant Stats:")
    print('Mean: \n')
    print(BM_mean.loc['M',:])
    print('Std:\n')
    print(BM_std.loc['M',:])
    
