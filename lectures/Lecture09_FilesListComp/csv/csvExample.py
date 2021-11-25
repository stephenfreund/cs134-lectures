import csv

listOfRows = []
with open('roster.csv') as myfile:
    csvf = csv.reader(myfile)
    for row in csvf:
        listOfRows.append(row)

    print(listOfRows)


