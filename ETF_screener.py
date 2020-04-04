#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:13:38 2020

@author: alex
"""

# %%
# Packages and Imports

import yfinance as yf

# %%
# Symbols universe

with open ("./data/TSX_etfs_20200404.txt") as file:
    tsx_etfs = [x.strip()+'.TO' for x in file]

# %%
# Dictionary of ticker objects

d = {}
for e in tsx_etfs:
    d[e] = yf.Ticker(e)

# %%
# Exampalr dividend yeild extraction

for key in d:
    try:
        print('ticker:{0} div_yield:{1}'.format(d[key].info['symbol'], d[key].info['yield']))
    except:
        print('Exception. {0} does not have data'.format(key))
