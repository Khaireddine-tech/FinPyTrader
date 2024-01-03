# FinPyTrader - Python Financial Analysis and Trading Library

**FinPyTrader** is a Python package designed for financial analysis and trading. It provides tools and functions for loading historical financial data from CSV files, calculating technical indicators like Simple Moving Averages (SMA) and Relative Strength Index (RSI), and writing indicator data to CSV files.

## Features

- Load historical financial data from CSV files.
- Calculate Simple Moving Averages (SMA) for a specified window size.
- Calculate Relative Strength Index (RSI) for a specified window size.
- Write calculated indicators to CSV files.

## Installation

You can install **FinPyTrader** using `pip`:

```bash
pip install FinPyTrader
```

## Usage

### Importing the Package

```python
from load_data import load_data_from_csv
from calculate_sma import calculate_sma
from calculate_rsi import calculate_rsi
from write_indicators import write_sma_to_csv, write_rsi_to_csv
```

### Loading Historical Data

```python
# Load historical data from a CSV file
historical_data = load_data_from_csv("orcl.csv")
```

### Calculating Simple Moving Averages (SMA)

```python
# Calculate SMA for a 5-day window
sma_values = calculate_sma(historical_data, window=5)
```

### Calculating Relative Strength Index (RSI)

```python
# Calculate RSI for a 14-day window
rsi_values = calculate_rsi(historical_data, window=14)
```

### Writing Indicator Data to CSV Files

```python
# Write SMA values to a CSV file
write_sma_to_csv(historical_data, sma_values, "orcl-sma.csv")

# Write RSI values to a CSV file
write_rsi_to_csv(historical_data, rsi_values, "orcl-rsi.csv")
```

## Documentation

For detailed information on the available functions and their parameters, please refer to the documentation.
