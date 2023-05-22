# styled with black

import random
import inflect
import csv
from operator import itemgetter
from tabulate import tabulate

p = inflect.engine()
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


# Wizard class with name and patronus
class Wizard:
    def __init__(self, name, patronus=""):
        self.name = name
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} has {p.a(self.patronus)} patronus."

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def patronus(self):
        return self._patronus

    @patronus.setter
    def patronus(self, patronus):
        if patronus == "":
            self._patronus = Patronus.assign()
        else:
            self._patronus = patronus


# Student class inherits from Wizard and in addition has a house for each student
class Student(Wizard):
    def __init__(self, name, patronus="", house=""):
        super().__init__(name, patronus)
        self.house = house

    def __str__(self):
        return f"{self.name} of {self.house} house has patronus {self.patronus}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in houses:
            self._house = Hat.sort_student()
        else:
            self._house = house


# Hat sorts students into houses
class Hat:
    @classmethod
    def sort_student(cls):
        return random.choice(houses)


# Patronus assigns a patronus
class Patronus:
    patronuses = [
        "Unicorn",
        "Butterfly",
        "Hungarian Horntail",
        "Gekko",
        "Duck",
        "Octopus",
        "Golden Retriever",
        "Tarantula",
        "Flobberworm",
        "Dolphin",
    ]

    @classmethod
    def assign(cls):
        return random.choice(cls.patronuses)


# hourglasses keep track of each house's points
class Hourglass:
    def __init__(self, points=0):
        self.points = points

    def __str__(self):
        return f"Housepoints: {self.points}"

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        self._points = points

    def add(self, n):
        self.points += n

    def deduct(self, n):
        if self.points - n >= 0:
            self.points -= n
        else:
            self.points = 0


# instantiate house hourglasses
Gryffindor = Hourglass()
Ravenclaw = Hourglass()
Hufflepuff = Hourglass()
Slytherin = Hourglass()


def main():
    # instantiate known students
    known = []
    with open("students.csv") as known_students:
        reader = csv.DictReader(known_students)
        for row in reader:
            known.append(Student(row["name"], row["patronus"], row["house"]))

    # load potions from file
    potions = []
    potion_ingredients = []
    potions_table = []
    with open("potions.csv") as potion_file:
        reader = csv.reader(potion_file)
        for row in reader:
            potions_table.append(row)
            potions.append(row[0])
            potion_ingredients.append(row[1:])

    # print instructions
    print(f"WELCOME TO POTIONS CLASS! Recommended reading Potions 101:")
    print(tabulate(potions_table, tablefmt="double_grid"))
    print(f"You can play as your favourite character - or as yourself!")

    # get number of players
    while True:
        try:
            nr_players = int(input("How many players (max 8)? "))
            if nr_players <= 8:
                break
        except ValueError:
            pass

    # get player names and instantiate them
    players = list(range(nr_players))
    for i in range(nr_players):
        name = input("Name: ").strip().capitalize()
        for student in known:
            if student.name == name:
                players[i] = student
                break
        else:
            players[i] = Student(name)
        print(
            f"Congratulations, you are in {players[i].house}! Your patronus is {p.a(players[i].patronus)}."
        )

    # start main game: pick potions randomly and prompt each player to list ingredients, then add / deduct house points according to correctness
    print(f"Let's brew potions!")
    rounds = min(4, 9 - nr_players)
    potion_picker = list(range(0, len(potions)))
    for i in range(rounds):
        index = random.choice(potion_picker)
        potion_picker.remove(index)
        potion = potions[index]
        print(f"List ingredients for {potion} (separate by comma+space)")
        for player in players:
            ingredients = input(f"{player.name}: ").lower().split(", ")
            print(
                potion_checker(
                    get_hourglass(player), ingredients, potion_ingredients[index]
                )
            )

    # spell competition
    for player in players:
        spell = input(f"Cast your spell, {player.name}: ").strip().lower()
        cast_spell(get_hourglass(player), spell)

    # display winner of the Housecup
    winner = housepoint_winner()[0][0]
    print(f"{winner} won the Housecup! Congratulations, {winner}s!")


# order houses according to points
def housepoint_winner():
    leaderboard = [
        ("Gryffindor", Gryffindor.points),
        ("Ravenclaw", Ravenclaw.points),
        ("Hufflepuff", Hufflepuff.points),
        ("Slytherin", Slytherin.points),
    ]
    leaderboard.sort(key=itemgetter(1), reverse=True)
    return leaderboard


# check potion ingredients for correctness and order, assign housepoints
def potion_checker(house, ingredients, potions_dict):
    if ingredients == potions_dict:
        house.add(20)
        return "Well done, you earned 20 points for your house"
    elif set(ingredients) == set(potions_dict):
        house.add(10)
        return "Wrong order, you earned 10 points for your house"
    elif set(ingredients).issubset(set(potions_dict)) and ingredients != []:
        house.add(5)
        return "Missing ingredients, you earned 5 points for your house"
    else:
        house.deduct(10)
        return "Explosion: you lost 10 points"


# check spells, assign housepoints accordingly
def cast_spell(house, spell):
    if spell in {"expecto patronum"}:
        house.add(30)
    elif spell in {"obliviate", "expelliarmus", "riddikulus", "accio"}:
        house.add(20)
    elif spell in {"alohomora", "petrificus totalus"}:
        house.add(15)
    elif spell in {"lumos", "wingardium leviosa", "reparo"}:
        house.add(10)
    elif spell in {"crucio", "imperio", "avada kedavra"}:
        house.deduct(50)
    return


# determine the right hourglass for a given student
def get_hourglass(student):
    if student.house == "Gryffindor":
        return Gryffindor
    elif student.house == "Ravenclaw":
        return Ravenclaw
    elif student.house == "Hufflepuff":
        return Hufflepuff
    elif student.house == "Slytherin":
        return Slytherin


if __name__ == "__main__":
    main()
