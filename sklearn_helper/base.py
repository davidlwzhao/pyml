import pandas as pd
import numpy as np

import sklearn.preprocessing
from sklearn.pipeline import make_pipeline as mk
from sklearn.compose import ColumnTransformer

import itertools

def make_pipeline(df, num_mapping, str_mapping):
    # check that df is a dataframe
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be pandas dataframe")

    # check that mappings are all columns of the dataframe and types are correct
    for col in num_mapping.keys():
        if col not in df.select_dtypes(include=['float64', 'int']).columns.values:
            raise ValueError(f"{col} is not a numeric column name in input dataframe")

    for col in str_mapping.keys():
        if col not in df.select_dtypes(exclude=['float64', 'int']).columns.values:
            raise ValueError(f"{col} is not a string column name in input dataframe")

    # parse all the transformers needed
    for col, params in itertools.chain(num_mapping.items(), str_mapping.items()):
        print(col, params)

    # for each kind of transformation compose together pre-processing needed
    
    df2 = df[list('abcd')].values
    mms = getattr(sklearn.preprocessing, "MinMaxScaler")().fit(df2)
    df2 = mms.transform(df2)
    
    print(df2)
    
    return 1

def compare_estimators(*args, **kwargs):
    '''
    returns --
    comparison object
    '''
    pass
    
if __name__ == "__main__":
    df_num = pd.DataFrame(1000 * np.random.randn(5,5) + 500, columns=list('abcde'))
    rand_words = [
        ['brian', 'steve', 'brian', 'steve', 'brian'],
        ['high', 'high', 'high', 'low', 'med'],
        ['north', 'west', 'south', 'east', 'west']
    ]
    df_str = pd.DataFrame({col:words for col, words in zip(list('fgh'), rand_words)})
    df = pd.concat([df_num, df_str], axis=1)


    num_mapping = {
        "a": {'scale':'minmax', 'nulls':'drop', 'f':None, "drop":False},
        "b": {'scale':'standard', 'nulls':'mean', 'f':None},
        "c": {'scale':'power', 'nulls':0, 'f':None},
        "d": {'scale':'robust', 'nulls':'median', 'f':np.log},
        "e": {'scale':None, 'nulls':'median', 'f':None}
    }

    str_mapping = {
        "f": {'encode':"onehot", 'nulls':'mode', 'f':None},
        "g": {'encode':"label", 'nulls':'mode', 'f':None, 'order':{
            "low": 0,
            "med": 1,
            "high": 2
        }},
        "h": {'encode':"onehot", 'nulls':'mode', 'f':None},
    }

    make_pipeline(df, num_mapping, str_mapping)