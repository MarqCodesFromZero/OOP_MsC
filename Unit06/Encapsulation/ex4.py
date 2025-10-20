#######################################################################
#Encapsulation Exercise 4
#######################################################################

class Dancer:
    def __init__(self, name, nationality, style):
        self._name = name
        self._nationality = nationality
        self._style = style

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        self._style = value

# Initialize an object of the Dancer class
my_dancer = Dancer("Savion Glover", "American", "tap")

# Access attributes using getters
print(my_dancer.name)
print(my_dancer.nationality)
print(my_dancer.style)

# Update attributes using setters
my_dancer.name = 'Anna Pavlova'
my_dancer.nationality = 'Russian'
my_dancer.style = 'ballet'

# Access updated attributes using getters
print(my_dancer.name)
print(my_dancer.nationality)
print(my_dancer.style)