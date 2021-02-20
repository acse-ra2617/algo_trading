# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:33:10 2021

@author: raula
"""
# package sources:
# https://ta-lib.org/
# https://github.com/mrjbq7/ta-lib
# python wrapper:
# https://mrjbq7.github.io/ta-lib/
# setting ta-lib up for windows
# https://blog.quantinsti.com/install-ta-lib-python/#windows


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
