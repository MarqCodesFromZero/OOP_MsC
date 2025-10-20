"""Polymorphism Exercise 3"""

class Characters:

    def __init__(self, phrases):
        # Initialize Characters with a list of phrases
        self.phrases = phrases

    def total_characters(self):
        # Calculate and return the total number of characters in all phrases
        return sum(len(phrase) for phrase in self.phrases)

    # Overload the < operator
    def __lt__(self, other):
        return self.total_characters() < other.total_characters()

    # Overload the > operator
    def __gt__(self, other):
        return self.total_characters() > other.total_characters()

    # Overload the == operator
    def __eq__(self, other):
        return self.total_characters() == other.total_characters()

# Test code
if __name__ == "__main__":
    # Sample phrases for testing
    sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
    sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

    # Create instances of Characters
    c1 = Characters(sample_phrases1)
    c2 = Characters(sample_phrases2)

    # Testing comparisons
    print(c1 > c2)  # Output: True
    print(c1 < c2)  # Output: False
    print(c1 == c1)  # Output: True