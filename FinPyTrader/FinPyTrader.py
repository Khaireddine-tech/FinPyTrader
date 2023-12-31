# Task-1: Load historical data from orcl.csv into a list of dictionaries
historical_data = []

# Read the spreadsheet "orcl.csv"
with open("orcl.csv", "r") as file:
    # Read the header to get column names
    header = file.readline().strip().split(',')

    # Read data line by line and create dictionaries for each entry
    for line in file:
        data = line.strip().split(',')
        entry = {header[i]: data[i] for i in range(len(header))}
        historical_data.append(entry)

# Task-2: Calculate technical indicators (SMA and RSI)

# Task-2.1: Simple Moving Averages (SMA) for a 5-day window
def calculate_sma(data, window):
    """
    Calculate Simple Moving Averages (SMA) for a given window size.

    Parameters:
    - data (list): List of dictionaries containing historical data.
    - window (int): Size of the window for calculating SMA.

    Returns:
    - list: List of SMA values.
    """
    # Initialize an empty list to store SMA values
    sma_values = []

    # Iterate over each data point in the historical data
    for i in range(len(data)):
        # Check if there are enough data points to calculate SMA for the current window
        if i < window - 1:
            sma_values.append(None)  # Not enough data for the first window
        else:
            # Extract the closing prices for the last 'window' days
            close_prices = [float(entry['Close']) for entry in data[i - window + 1 : i + 1]]

            # Calculate SMA as the average of closing prices
            sma = sum(close_prices) / window

            # Append the calculated SMA to the list
            sma_values.append(sma)

    # Return the list of SMA values
    return sma_values


# Task-2.2: Relative Strength Index (RSI) for a 14-day window
def calculate_rsi(data, window):
    """
    Calculate Relative Strength Index (RSI) for a given window size.

    Parameters:
    - data (list): List of dictionaries containing historical data.
    - window (int): Size of the window for calculating RSI.

    Returns:
    - list: List of RSI values.
    """
    # Initialize an empty list to store RSI values
    rsi_values = []

    # Iterate over each data point in the historical data
    for i in range(len(data)):
        # Check if there are enough data points to calculate RSI for the current window
        if i < window:
            rsi_values.append(None)  # Not enough data for the first window
        else:
            # Initialize variables to track gains and losses
            gains = losses = 0

            # Iterate over the last 'window' days to calculate gains and losses
            for j in range(i, i - window, -1):
                close_diff = float(data[j]['Close']) - float(data[j - 1]['Close'])
                if close_diff > 0:
                    gains += close_diff
                else:
                    losses += abs(close_diff)

            # Calculate average gain and average loss over the window
            avg_gain = gains / window if gains else 0
            avg_loss = losses / window if losses else 0

            # Calculate relative strength and RSI
            if avg_loss == 0:
                rsi = 100
            else:
                relative_strength = avg_gain / avg_loss
                rsi = 100 - (100 / (1 + relative_strength))

            # Append the calculated RSI to the list
            rsi_values.append(rsi)

    # Return the list of RSI values
    return rsi_values

# Task-3: Write indicators to files (orcl-sma.csv and orcl-rsi.csv)

# Task-3.1: Write SMA values to orcl-sma.csv
sma_values = calculate_sma(historical_data, window=5)

with open("orcl-sma.csv", "w") as sma_file:
    sma_file.write("Date,SMA\n")
    for i in range(len(historical_data)):
        sma_file.write(f"{historical_data[i]['Date']},{sma_values[i]}\n")

# Task-3.2: Write RSI values to orcl-rsi.csv
rsi_values = calculate_rsi(historical_data, window=14)

with open("orcl-rsi.csv", "w") as rsi_file:
    rsi_file.write("Date,RSI\n")
    for i in range(len(historical_data)):
        rsi_file.write(f"{historical_data[i]['Date']},{rsi_values[i]}\n")

print("4th Homework Assignment: 2281524")