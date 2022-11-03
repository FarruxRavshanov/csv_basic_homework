def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    sum = data.split('\n')
    data = sum[0].split(',')
    return len(data)

# Read the csv file
import csv
f = open('data.csv')
reader = csv.reader(f)
for row in reader:
    print(row)