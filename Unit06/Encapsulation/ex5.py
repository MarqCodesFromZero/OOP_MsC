#######################################################################
#Encapsulation Exercise 5
#######################################################################

class Cyclist:
    def __init__(self, name, nationality, nickname):
        self._name = name
        self._nationality = nationality
        self._nickname = nickname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, new_nationality):
        self._nationality = new_nationality

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, new_nickname):
        self._nickname = new_nickname

# Initialize an object of the Cyclist class
my_cyclist = Cyclist("Greg LeMond", "American", "Le Montstre")

# Display initial values
print(my_cyclist.name)
print(my_cyclist.nationality)
print(my_cyclist.nickname)

# Update attributes using setters
my_cyclist.name = "Eddy Merckx"
my_cyclist.nationality = "Belgian"
my_cyclist.nickname = "The Cannibal"

# Display updated values
print(my_cyclist.name)
print(my_cyclist.nationality)
print(my_cyclist.nickname)