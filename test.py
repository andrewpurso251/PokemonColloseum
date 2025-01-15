import csv
import ast

moves1 = ['Mega Punch', 'Thunder Punch', 'Thunder Shock', 'Slam', 'Dig']
moveData = []
pokemon_filename = 'moves-data.csv'
header = []
pokemon_moves = {}
with open(pokemon_filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for row in reader:
        if row[0] in moves1:
            moveData.append(row)
            
        
print(moveData)