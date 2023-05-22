# POTIONS
#### Video Demo:  https://youtu.be/kO5myqmAlHE
#### Description:

## Harry Potter Potion Making Game
### **project.py**

#### Background
This is a Harry Potter inspired game where players compete for the Housecup in the Interhouse Championship between the four Hogwarts houses (Gryffindor, Ravenclaw, Hufflepuff and Slytherin). Just like in the original books and movies, players earn points for their house by performing well in class and lose points for bad behaviour. At the end of the game, the house with the most points is awarded the Housecup.

#### **class Wizard**
This project uses object-oriented programming to implement key features. Instances of this class have a *name* and a *patronus* attribute. The *patronus* argument is optional and *wizards* are assigned a new *patronus* if omitted.

#### **class Student(Wizard)**
The *Student* class inherits from *Wizard* and has the additional attribute *house*. The *house* is optional and will be picked if not given.

#### **class Hat**
The *Hat* is called in the *Student* class to assign (at random) one of the four houses to *students* that do not have one yet. This is similar to the Sorting Hat in Harry Potter that takes on the role of sorting new students into houses.

#### **class Patronus**
Similarly, this class randomly assigns a *patronus* to *wizards* with unknown patronus.

#### **class Hourglass**
This class keeps track of a house's points, just like the big hourglasses in the books. Points can be added and deducted but cannot go below zero.

#### **housepoint_winner()**
This function checks the current state of the four *hourglasses* and returns a sorted list of tuples (house name and points), with the house with the highest number of points coming first.

#### **potion_checker(house, ingredients, potions_dict)**
This function checks if a given list of *ingredients* corresponds to the correct list of potion ingredients *potions_dict*. If it does not, it goes on to check if the ingredients match in a different order or if the items are correct but there are ingredients missing. The relevant *house* points are updated accordingly. If there are wrong ingredients or no ingredients at all, points are deducted from the *house*. The function returns a message informing the player of the result.

#### **cast_spell(house, spell)**
In a similar fashion, *cast_spell* takes as arguments a *spell* and the player's *house* hourglass. Depending on the difficulty of the spell, different numbers of points are added to the *house*. If the *spell* is an Unforgivable Curse, points are deducted instead. To keep things less predictable when playing repeatedly, the player is not informed about how many points were earned.

#### **get_hourglass(student)**
This function checks a *student*'s house and returns the respective *hourglass* to facilitate point tracking.

#### **main()**
In *main*, original characters with their respective houses and patronuses are imported from a CSV file using the *DictReader* and instantiated as *students*. Potion names and ingredients are also imported and stored in the lists *potions* and *potion_ingredients*. They are also put into a *table* to be formatted with *tabulate* and printed for the players to see. After receiving basic instructions, the user is asked for the number of players and then the names of those players. If a name belongs to one of the original characters, that instance of *student* is used. Otherwise, a new *student* is created. The *students* are stored in a list. For each round of the game (maximum of four rounds, decreases with number of players), a random (and non-repeating) potion is picked, then each player in turn is prompted for the ingredients, to be checked by *potion_checker*. After the last round, each player can cast a spell of their choosing, points are awarded accordingly by *cast_spell*. At last, *housepoint_winner* is called and the winner of the Housecup announced to the players. \
Code was styled with *Black*.

### **test_project.py**
Unit tests for *housepoint_winner*, *potion_checker*, *cast_spell* and *get_hourglass*. The relevant instances of *hourglass* were imported to facilitate state modelling. \
Code was styled with *Black*.

### **potions.csv**
CSV file with potions and their corresponding ingredients, in order.

### **students.csv**
CSV file of original characters and their respective house and patronus.