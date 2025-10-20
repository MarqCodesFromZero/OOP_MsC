import random

class Card:
    """Represents a standard playing card."""

    suit_names=["Diamonds","Hearts","Spades","Clubs"]
    rank_names=[None, "Ace", "2", "3", "4", "5", "6","7","8","9","10","Jack","Queen","King","Ace"]


    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        rank_name=self.rank_names[self.rank]
        suit_name=self.suit_names[self.suit]
        return f"{rank_name} of {suit_name}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __ne__(self, other):
        return not self.__eq__(other)

    def turn_into_tuple(self):
        return self.suit ,self.rank

    def __lt__(self, other):
        return self.turn_into_tuple() < other.turn_into_tuple()

    def __gt__(self, other):
        return self.turn_into_tuple() > other.turn_into_tuple()

    def __le__(self, other):
        return self.turn_into_tuple() <= other.turn_into_tuple()

    def __ge__(self, other):
        return self.turn_into_tuple() >= other.turn_into_tuple()


class Deck:

    def __init__(self, cards):
        self.cards = cards

    @staticmethod
    def make_cards():
        cards=[]
        for suit in range(4):
            for rank in range(2,15):
                card=Card(suit, rank)
                cards.append(card)
        return cards

    def __str__(self):
        deck_string = []
        for card in self.cards:
            deck_string.append(str(card))
        return '\n'.join(deck_string)

    def take_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort_cards(self):
        self.cards.sort()

    def move_cards(self, other, num):
        for i in range(num):
            card = self.take_card()
            other.add_card(card)


class Hand(Deck):
    """Represents a standard playing hand.
    It acts like a mini deck that's assigned to a player
    """

    def __init__(self, player=""):

        self.player = player
        self.cards = []

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return f'Cards: {res}'


    # Polymorphism!!!
    def move_cards(self, other, num):
        for i in range(num):
            card = self.take_card()
            other.add_card(card)

class BridgeHand(Hand):
    """Represents a standard playing bridge."""
    high_card_point_count={
        "Ace": 4,
        "King":3,
        "Queen":2,
        "Jack":1,
    }

    def card_rank_score(self,rank):
        rank_name=Card.rank_names[rank]
        score= self.high_card_point_count.get(rank_name,0)
        return rank_name, score

    def points_in_hand(self):
        count = 0
        for card in self.cards:
            rank_name = Card.rank_names[card.rank]
            count += BridgeHand.high_card_point_count.get(rank_name, 0)
        return count

    def winning_hand(self, other):
        if self.points_in_hand()>other.points_in_hand():
            print(f"{self.player} wins")
        else:
            print(f"{other.player} wins")

    @staticmethod
    def winning_among(*hands):
        """Return the hand(s) with the highest points."""
        # Handle empty call
        if not hands:
            return []

        # Find the maximum points amongst all player hands
        max_points = 0
        for hand in hands:
            points = hand.points_in_hand()
            if points > max_points:
                max_points = points

        # Collect all hands that match max_points
        winners = []
        for hand in hands:
            if hand.points_in_hand() == max_points:
                winners.append(hand.player)

        return winners







cards=Deck.make_cards()
deck=Deck(cards)
print(len(deck.cards))

queen=Card(1,12)

queen2=Card(1,12)

six=Card(1,6)


small_deck = Deck([queen, six])

print(small_deck)


################### ADD, REMOVE, SHUFFLE and SORT cards from a deck ##################
deck.shuffle()
card1=deck.take_card()
print(card1)

print(len(deck.cards))

deck.add_card(card1)
print(len(deck.cards))




################### Hands for players ######################
deck.shuffle()
p1_hand=Hand("Player 1")
print(p1_hand.player)

deck.sort_cards()
deck.move_cards(p1_hand, 52)

print(p1_hand)

p1_hand.shuffle()
p1_hand.move_cards(deck, 52)

print(p1_hand)

####bridgehand###

bridge_hand1=BridgeHand("P1")
deck.shuffle()
deck.move_cards(bridge_hand1, 5)
print(f"\n{bridge_hand1.player}")
print(bridge_hand1)

print(bridge_hand1.points_in_hand(), "points in hand")


bridge_hand2=BridgeHand("P2")
deck.move_cards(bridge_hand2, 5)
print(f"\n{bridge_hand2.player}")
print(bridge_hand2)

print(bridge_hand2.points_in_hand(), "points in hand")



bridge_hand1.winning_hand(bridge_hand2)

bridge_hand3=BridgeHand("P3")
deck.shuffle()
deck.move_cards(bridge_hand3, 5)
print(f"\n{bridge_hand3.player}")
print(bridge_hand3)

print(bridge_hand3.points_in_hand(), "points in hand")

print(BridgeHand.winning_among(bridge_hand1,bridge_hand2,bridge_hand3))