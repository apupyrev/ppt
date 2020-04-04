#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:13:38 2020

@author: alex
"""

# %%
import yfinance as yf


# %%

cad_etfs_top50_cap = ["ZSP.TO","XIU.TO","XIC.TO","ZAG.TO","XSP.TO","ZCN.TO","XBB.TO",
"XEF.TO","ZEA.TO","VAB.TO","VFV.TO","ZLB.TO","PSA.TO","VUN.TO","VCN.TO","XSB.TO",
"XUS.TO","HXT.TO","XCB.TO","ZPR.TO","ZUE.TO","ZWB.TO","ZLU.TO","ZFL.TO","CSAV.TO",
"PMIF.TO","ZIC.TO","XRE.TO","ZMU.TO","XDV.TO","VIU.TO","HPR.TO","ZCS.TO","ZEM.TO",
"CPD.TO","XIN.TO","XAW.TO","VSC.TO","VSB.TO","VGRO.TO","XUU.TO","ZEB.TO","ZCM.TO",
"XFN.TO","ZDB.TO","VSP.TO","VEE.TO","VBAL.TO","CBO.TO","ZWP.TO"]


# %%

d = {}
for e in cad_etfs_top50_cap:
    d[e] = yf.Ticker(e)

# %%

for key in d:
    try:
        print('ticker:{0} div_yield:{1}'.format(d[key].info['symbol'], d[key].info['yield']))
    except:
        print('{0} does not have data'.format(key))
# %%
k = yf.Ticker

#t = yf.Tickers("XSP.TO XIC.TO")
#dt = t.download()
