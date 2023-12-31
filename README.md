# FinPyTrader

[![PyPI version](https://badge.fury.io/py/FinPyTrader.svg)](https://badge.fury.io/py/FinPyTrader)

**FinPyTrader** is a Python package for algorithmic trading. It provides tools for loading historical financial data, calculating technical indicators, and implementing trading strategies.

## Installation

You can install **FinPyTrader** using `pip`. Make sure you have Python 3.6 or higher installed.

```bash
pip install FinPyTrader
```
# Usage
## Loading Historical Data
```bash
from FinPyTrader import load_historical_data

# Load historical data from a CSV file
data = load_historical_data('orcl.csv')

# data is a list of dictionaries with columns: Date, Open, High, Low, Close, Adj Close, Volume
```

## Calculating Simple Moving Averages (SMA)
```bash
from FinPyTrader import calculate_sma

# Calculate SMA with a 5-day window
sma_values = calculate_sma(data, window=5)

# sma_values is a list of SMA values
```
## Calculating Relative Strength Index (RSI)
```bash
from FinPyTrader import calculate_rsi

# Calculate RSI with a 14-day window
rsi_values = calculate_rsi(data, window=14)

# rsi_values is a list of RSI values
```

## Writing Indicators to Files
```bash
from FinPyTrader import write_to_csv

# Write SMA values to a CSV file
write_to_csv('sma.csv', data, sma_values)

# Write RSI values to a CSV file
write_to_csv('rsi.csv', data, rsi_values)
```
