import sqlite3
import csv

# Measurement Dictionary have key as the ID # and value as the corresponding string
measurementDict = {}
with open('copy of measurement.csv', 'r') as csv_file2:
    reader = csv.reader(csv_file2)
    next(reader, None)
    for row in reader:
        measurementDict[int(row[0])] = str(row[1])
print(measurementDict)
# Food Dictionary have key as the FDC ID # and value as the corresponding string food name
foodDict = {}
with open('copy of food csv.csv', 'r') as csv_file3:
    reader = csv.reader(csv_file3)
    next(reader, None)
    for row in reader:
        foodDict[int(row[0])] = str(row[2]).lower()
print(foodDict)
# Want to create a database w/ Columns for FDC ID (Bookkeeping purposes), food name, amount, imperial measurement
# used, gram weight
conn = sqlite3.connect(r"C:\sqlite\db\foodDensity.db")
# create a table with a column for FOOD and then DENSITY
sqlFoodDensTable = """ CREATE TABLE IF NOT EXISTS foodDensity (
                                        fdc_ID text NOT NULL,
                                        food_name text NOT NULL,
                                        amount real NOT NULL,
                                         measurement_unit text NOT NULL,
                                         gram_weight real NOT NULL
                                        
                                    ); """
cur = conn.cursor()
cur.execute(sqlFoodDensTable)


# Get our values from CSV and insert them into the table
def insert_row(connection, data_row):
    query = ''' INSERT INTO foodDensity(fdc_ID, food_name, amount, measurement_unit, gram_weight) VALUES(?,?,?,?,?) '''
    cursor = connection.cursor()
    cursor.execute(query, data_row)
    connection.commit()


with open('copy of food_portion.csv', 'r') as csv_file4:
    reader = csv.reader(csv_file4)
    next(reader, None)
    for row in reader:
        fdc_id = int(row[1])
        # print(fdc_id)
        food = foodDict[fdc_id]
        # print(food)
        amount = row[3]
        # print(amount)
        measurement = measurementDict[int(row[4])]
        # print(measurement)
        gram_weight = row[7]
        # print(gram_weight)
        data = (fdc_id, food, amount, measurement, gram_weight)
        insert_row(conn, data)

