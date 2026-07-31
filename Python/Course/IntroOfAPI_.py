import pandas as pd
import matplotlib.pyplot as plt
dict_ = {'a': [11,21,31],'b':[12,22,32]}
df=pd.DataFrame(dict_)
type(df)
df.head()
df.mean()
# REST APIs it communicates via HTTP requests and responses. It allows different software applications to interact with each other over the web. REST APIs use standard HTTP methods such as GET, POST, PUT, DELETE to perform operations on resources represented in JSON or XML format.
from nba_api.stats.static import teams
import matplotlib.pyplot as plt
def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        