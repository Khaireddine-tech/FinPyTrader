def calculate_sma(data, window):
    """
    Calculate Simple Moving Averages (SMA) for a given window size.

    Parameters:
    - data (list): List of dictionaries containing historical data.
    - window (int): Size of the window for calculating SMA.

    Returns:
    - list: List of SMA values.
    """
    sma_values = []

    for i in range(len(data)):
        if i < window - 1:
            sma_values.append(None)
        else:
            close_prices = [float(entry['Close']) for entry in data[i - window + 1 : i + 1]]
            sma = sum(close_prices) / window
            sma_values.append(sma)

    return sma_values
