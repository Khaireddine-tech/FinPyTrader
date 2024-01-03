def write_sma_to_csv(data, sma_values, filename):
    """
    Write SMA values to a CSV file.

    Parameters:
    - data (list): List of dictionaries containing historical data.
    - sma_values (list): List of SMA values.
    - filename (str): The name of the CSV file to write.

    Returns:
    - None
    """
    with open(filename, "w") as sma_file:
        sma_file.write("Date,SMA\n")
        for i in range(len(data)):
            sma_file.write(f"{data[i]['Date']},{sma_values[i]}\n")

def write_rsi_to_csv(data, rsi_values, filename):
    """
    Write RSI values to a CSV file.

    Parameters:
    - data (list): List of dictionaries containing historical data.
    - rsi_values (list): List of RSI values.
    - filename (str): The name of the CSV file to write.

    Returns:
    - None
    """
    with open(filename, "w") as rsi_file:
        rsi_file.write("Date,RSI\n")
        for i in range(len(data)):
            rsi_file.write(f"{data[i]['Date']},{rsi_values[i]}\n")
