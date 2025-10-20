#######################################################################
#Exercise 17.2
#######################################################################

'''
This exercise is a cautionary tale about one of the most common, and 
difficult to find, errors in Python. Write a definition for a class named 
Kangaroo with the following methods:

1. An __init__ method that initializes an attribute named pouch_contents to 
an empty list.

2. A method named put_in_pouch that takes an object of any type and adds it 
to pouch_contents.

3. A __str__ method that returns a string representation of the Kangaroo 
object and the contents of the pouch.

Test your code by creating two Kangaroo objects, assigning them to variables 
named kanga and roo, and then adding roo to the contents of kanga’s pouch.
View BadKangaroo.py. It contains a solution to the previous problem with 
one big, nasty bug. Find and fix the bug.
'''

class Kangaroo:
    """A Kangaroo is a marsupial."""

    def __init__(self, name, contents=None):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        if contents is None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representation of this Kangaroo."""
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)

# Printing roo to verify the contents
print(roo)
