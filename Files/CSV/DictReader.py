# 1.Import the csv module.

# 2.Open up the file logger_csv.csv in the temporary variable cool_csv_file.

# 3.Using csv.DictReader read the contents of logger_csv_file into a new variable called logger_csv_dict.

# 4.logger_csv.csv includes a Name of every person in the CSV.
# For each row in logger_csv_dict print out that row’s "Name".

import csv
with open("logger.csv") as logger_csv_file:
    logger_csv_dict = csv.DictReader(logger_csv_file)
    for row in logger_csv_dict:
        print(row['Name'])
