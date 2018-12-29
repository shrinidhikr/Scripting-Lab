# import the pandas library
import pandas as pd #'pandas' stands for panel data
import numpy as np #'numpy' stands for numerical python

'''
numpy.random.randn(d0, d1, …, dn) : E.g.random.randn(4, 3) 4 rows and 3 columns
creates an array of specified shape and fills it. Here index has 4 rows and
columns is labelled as 3 'one', 'two', 'three'

With random values as per standard normal distribution.If positive arguments are provided,
'randn' generates an array of shape (d0, d1, …, dn), filled with random floats sampled from
a univariate “normal” (Gaussian) distribution of mean 0 and variance 1.
A single float randomly sampled from the distribution is returned if no argument is provided.
'''

df = pd.DataFrame(np.random.randn(4,3), index=['a', 'c', 'e','h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print ("------Prints the data frame----\n", df)

print ("------Prints True if NULL value in column one ----\n", df['one'].isnull())

print ("------Fills NAN with 0 in the data frame----\n", df.fillna(0))

print ("------Drops the missing values in the data frame----\n", df.dropna())

print ("------Forward fills the missing values in the data frame----\n", df.fillna(method='pad'))

print ("------Backward fills the missing values in the data frame----\n",df.fillna(method='bfill')) 
