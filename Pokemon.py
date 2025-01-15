import csv
import ast


class Pokemon:
    def __init__(self, name, type, hp, attack, defense, height, weight, moves):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.height = height
        self.weight = weight
        self.moves = moves
        self.moveData = []

    def __str__(self):
        return (f"Pokemon(Name: {self.name}, Type: {self.type}, HP: {self.hp}, "
                f"Attack: {self.attack}, Defense: {self.defense}, Height: {self.height}, "
                f"Weight: {self.weight}, Moves: {self.moves})")

    
    def getMoves(self):
        moveData = []
        pokemon_filename = 'moves-data.csv'
        with open(pokemon_filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header = next(reader)
            for row in reader:
                if row[0] in self.moves:
                    moveData.append(row)
        
        self.moveData = moveData
        print(self.moveData)
