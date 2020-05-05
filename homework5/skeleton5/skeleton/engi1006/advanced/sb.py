import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")


def scatterMatrix(data, labels, count=5):
    '''Use seaborn to produce a pairplot of columns

    data: numpy array of data
    labels: numpy array of labels
    count: number of columns to scatter (larger will result in slower)
    '''
    # convert to dataframe, limit number of columns shown for time reasons
    df = pd.DataFrame(data[:,:count])

    # use labels as class
    print(df.columns)
    # pairplot
   
   
    pair = sns.pairplot(data=df)
    # show plot
    plt.show()

def correlationHeatmap(data):
    '''Use seaborn to produce a heatmap of the columns' correlation

    data: numpy array of data
    '''
    # convert to dataframe
    df = pd.DataFrame(data)
    
    chart2,ax2 = plt.subplots()
    # heatmap of correlations
    """
    rescale, know data
    """
  
    heat = sns.heatmap(data=df,annot=True,linewidths=.5,ax=ax2)
    # show plot
    plt.show()
