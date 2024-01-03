from load_data import load_data_from_csv
from calculate_sma import calculate_sma
from calculate_rsi import calculate_rsi
from write_indicators import write_sma_to_csv, write_rsi_to_csv

historical_data = load_data_from_csv("orcl.csv")
sma_values = calculate_sma(historical_data, window=5)
rsi_values = calculate_rsi(historical_data, window=14)
write_sma_to_csv(historical_data, sma_values, "orcl-sma.csv")
write_rsi_to_csv(historical_data, rsi_values, "orcl-rsi.csv")

print("4th Homework Assignment: Done Successfully!!")