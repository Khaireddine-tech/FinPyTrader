def calculate_rsi(data, window):
    """
    Calculate Relative Strength Index (RSI) for a given window size.

    Parameters:
    - data (list): List of dictionaries containing historical data.
    - window (int): Size of the window for calculating RSI.

    Returns:
    - list: List of RSI values.
    """
    rsi_values = []

    for i in range(len(data)):
        if i < window:
            rsi_values.append(None)
        else:
            gains = losses = 0

            for j in range(i, i - window, -1):
                close_diff = float(data[j]['Close']) - float(data[j - 1]['Close'])
                if close_diff > 0:
                    gains += close_diff
                else:
                    losses += abs(close_diff)

            avg_gain = gains / window if gains else 0
            avg_loss = losses / window if losses else 0

            if avg_loss == 0:
                rsi = 100
            else:
                relative_strength = avg_gain / avg_loss
                rsi = 100 - (100 / (1 + relative_strength))

            rsi_values.append(rsi)

    return rsi_values
