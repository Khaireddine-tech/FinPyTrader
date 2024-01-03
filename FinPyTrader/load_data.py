def load_data_from_csv(filename):
    """
    Load historical data from a CSV file into a list of dictionaries.

    Parameters:
    - filename (str): The name of the CSV file to load.

    Returns:
    - list: List of dictionaries containing historical data.
    """
    historical_data = []

    with open(filename, "r") as file:
        header = file.readline().strip().split(',')
        for line in file:
            data = line.strip().split(',')
            entry = {header[i]: data[i] for i in range(len(header))}
            historical_data.append(entry)

    return historical_data
