#######################################################################
#Encapsulation Exercise 2
#######################################################################
class Artist:
    def __init__(self, name, medium, style, famous_artwork):
        self.__name = name
        self.__medium = medium
        self.__style = style
        self.__famous_artwork = famous_artwork
# Initialize an object of the Artist class
my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')
# Attempt to print the attributes directly (will result in an error)
try:
    print(my_artist.name)
except AttributeError as e:
    print("Error Message:", e)
try:
    print(my_artist.medium)
except AttributeError as e:
    print("Error Message:", e)
try:
    print(my_artist.style)
except AttributeError as e:
    print("Error Message:", e)
try:
    print(my_artist.famous_artwork)
except AttributeError as e:
    print("Error Message:", e)
    
# Access the private attributes using name mangling
print(my_artist._Artist__name)
print(my_artist._Artist__medium)
print(my_artist._Artist__style)
print(my_artist._Artist__famous_artwork)