from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def processData(ticker):
    ts = TimeSeries('DRLVZJXZ2S4ULOCH', output_format='pandas')
    Monthly_TS_df, meta_data=ts.get_intraday(symbol=ticker,interval='1min', outputsize='full')
    #print(Daily_TS_df.head())
    #Change column names to approprate form, 
    for column in Monthly_TS_df.columns:
        Monthly_TS_df.rename({column: column.split('. ')[1]}, axis=1, inplace=True)

    return Monthly_TS_df

def plot_data(ticker, column):
    fig = Figure()
    df = processData(ticker)
    df.plot(y=column, use_index = True)   
    plt.xlabel(' Date ')
    plt.ylabel(' Price ')
    plt.savefig('./static/'+ticker+'_'+column+".png")
