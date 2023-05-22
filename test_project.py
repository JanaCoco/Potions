import pytest
from project import (
    housepoint_winner,
    potion_checker,
    cast_spell,
    get_hourglass,
    Hourglass,
    Student,
    Gryffindor,
    Ravenclaw,
    Hufflepuff,
    Slytherin,
)
import inflect
import csv
from operator import itemgetter


def test_housepoint_winner():
    Gryffindor.points = 220
    Ravenclaw.points = 40
    Hufflepuff.points = 0
    Slytherin.points = 80
    assert housepoint_winner() == [
        ("Gryffindor", 220),
        ("Slytherin", 80),
        ("Ravenclaw", 40),
        ("Hufflepuff", 0),
    ]
    Gryffindor.points = 0
    assert housepoint_winner()[0][0] == "Slytherin"
    Ravenclaw.points = 80
    assert housepoint_winner()[0][0] == "Ravenclaw"


def test_potion_checker():
    house = Hourglass(50)
    ingredients = ["a", "b", "c"]
    potions_dict = ["a", "b", "c"]
    assert (
        potion_checker(house, ingredients, potions_dict)
        == "Well done, you earned 20 points for your house"
    )
    assert house.points == 70
    ingredients = ["a", "c", "b"]
    assert (
        potion_checker(house, ingredients, potions_dict)
        == "Wrong order, you earned 10 points for your house"
    )
    assert house.points == 80
    ingredients = ["a", "b"]
    assert (
        potion_checker(house, ingredients, potions_dict)
        == "Missing ingredients, you earned 5 points for your house"
    )
    assert house.points == 85
    ingredients = ["a", "c"]
    assert (
        potion_checker(house, ingredients, potions_dict)
        == "Missing ingredients, you earned 5 points for your house"
    )
    assert house.points == 90
    ingredients = ["c", "b"]
    assert (
        potion_checker(house, ingredients, potions_dict)
        == "Missing ingredients, you earned 5 points for your house"
    )
    assert house.points == 95
    ingredients = ["d", "e", "f"]
    assert (
        potion_checker(house, ingredients, potions_dict)
        == "Explosion: you lost 10 points"
    )
    assert house.points == 85
    ingredients = []
    assert (
        potion_checker(house, ingredients, potions_dict)
        == "Explosion: you lost 10 points"
    )
    assert house.points == 75


def test_cast_spell():
    house = Hourglass()
    cast_spell(house, "expecto patronum")
    assert house.points == 30
    cast_spell(house, "avada kedavra")
    assert house.points == 0
    cast_spell(house, "wingardium leviosa")
    assert house.points == 10
    cast_spell(house, "alohomora")
    assert house.points == 25
    cast_spell(house, "accio")
    assert house.points == 45
    cast_spell(house, "hokus pokus")
    assert house.points == 45
    cast_spell(house, 5)
    assert house.points == 45
    cast_spell(house, "")
    assert house.points == 45


def test_get_hourglass():
    A = Student("A", "stag", "Gryffindor")
    B = Student("B", "boar", "Ravenclaw")
    C = Student("C", "unicorn", "Hufflepuff")
    D = Student("D", "dog", "Slytherin")
    assert get_hourglass(A) == Gryffindor
    assert get_hourglass(B) == Ravenclaw
    assert get_hourglass(C) == Hufflepuff
    assert get_hourglass(D) == Slytherin
