import pandas as pd
import ta as ta
import math
import numpy as np

# Simple Moving Avarage
def SMA(data, time, period=5):
  total = (sum(data['PREULT'].iloc[time-period: time]))/5 if time >= period else (sum(data['PREULT'].iloc[0:time]))/(time+1)
  return total

# Weighted Moving Average
def WMA(data, time, period=5):
  total = 0
  div = 1
  for i in range(time):
    total =+ i*data['PREULT'].iloc[time-i]
    div =+ i

  return total/div

# Stochastic Momentum
def SMI(data, time, period=5):
  smi = ta.momentum.stoch(data['PREMAX'], data['PREMIN'], data['PREULT'], n=period, fillna=False)
  return smi.iloc[time]

def RSI(data, time, period=5):
  rsi = ta.momentum.rsi(data['PREULT'], n=period, fillna=False)
  return rsi.iloc[time]

def MACD(data, time):
  macd = ta.trend.macd(data['PREULT'], n_fast=12, n_slow=26, fillna=False)
  res = data['PREMAX'].iloc[time] if math.isnan(macd.iloc[time]) else macd.iloc[time]
  return res

def CCI(data, time, period=5):
  cci = ta.trend.cci(data['PREMAX'], data['PREMIN'], data['PREULT'], n=period, c=0.015, fillna=False)
  return cci.iloc[time]

def AO(data, time):
  ao = ta.momentum.ao(data['PREMAX'], data['PREMIN'], s=5, l=34, fillna=False)
  res = data['PREMAX'].iloc[time] if math.isnan(ao.iloc[time]) else ao.iloc[time]
  return res

class Indicators:

  def getState(self, data, time, period=5):
    return np.array([[SMA(data, time, period),
                      WMA(data, time, period),
                      SMI(data, time, period),
                      RSI(data, time, period),
                      MACD(data, time),
                      CCI(data, time, period),
                      AO(data, time)]])