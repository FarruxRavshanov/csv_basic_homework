def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    count = 0
    i = 0
    while i < len(data.split('\n')):
        count += 1
        i += 1
        return count

# Read the csv file
import csv
f = open('data.csv')
reader = csv.reader(f)
for row in reader:
    print(row)