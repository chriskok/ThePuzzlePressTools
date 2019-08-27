import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # this is used for the plot the graph 
import seaborn as sns # used for plot interactive graph.

import plotly.offline as py
import plotly.graph_objs as go


data = pd.read_csv('data/2019-08-26-TOP_FREE-GAME_PUZZLE', sep=',', engine='python')

print(data['installs'].describe())

print(data.head(1))