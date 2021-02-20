# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:33:10 2021

@author: raula
"""

# https://github.com/mrjbq7/ta-lib
# https://ta-lib.org/
# https://mrjbq7.github.io/ta-lib/
# https://blog.quantinsti.com/install-ta-lib-python/#windows
# https://mrjbq7.github.io/ta-lib/index.html


import numpy as np
import talib

my_data = np.genfromtxt('../data/15minutes.csv', delimiter=',')
print(my_data)

close = my_data[:, 4]
print(close)

"""
close = numpy.random.random(100)
print(close)

moving_average = talib.SMA(close, timeperiod=10)
print(moving_average)
"""
rsi = talib.RSI(close)
print(rsi)
