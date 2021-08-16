"""
Convert our CSV file to local database using Sqlite3
Only want the FOOD NAME and DENSITY in our database for the purpose of our converter
"""
import sqlite3
import csv
conn = sqlite3.connect(r"C:\sqlite\db\foodDensity.db")
# create a table with a column for FOOD and then DENSITY
sqlFoodDensTable = """ CREATE TABLE IF NOT EXISTS foodDensity (
                                        food text NOT NULL,
                                        density real NOT NULL
                                    ); """
cur = conn.cursor()
cur.execute(sqlFoodDensTable)
#conn.close()
# Get our values from CSV and insert them into the table
def insert_row(connection, row):
    query = ''' INSERT INTO foodDensity(food,density) VALUES(?,?) '''
    cursor = connection.cursor()
    cursor.execute(query, row)
    connection.commit()

with open('Copy of density_DB_v2_0_final-1__1_.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    #skip header
    next(reader, None)
    for row in reader:
        food = row[0]
        density: float = 0.0
        if row[1] != "":
            try:
                density = float(row[1])
            except ValueError:
                densityList = row[1].split("-")
                avg = float(densityList[1]) - float(densityList[0])
                density = float(densityList[0]) + avg


        elif row[2] != "":
            try:
                density = float(row[2])
            except ValueError:
                densityList = row[2].split("-")
                avg = float(densityList[1]) - float(densityList[0])
                density = float(densityList[0]) + avg
        else:
            #if both density and gravity are blank we don't want to add current food to our table
            continue
        sqlRow = (food, density)
        print(sqlRow)
        insert_row(conn, sqlRow)







