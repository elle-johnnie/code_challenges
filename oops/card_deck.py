import random

ROYAL_CARDS = {
    1: 'Ace',
    11: 'Jack',
    12: 'Queen',
    13: 'King'
}

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def reveal(self):
        _value = self.value
        if self.value in ROYAL_CARDS:
            _value = ROYAL_CARDS[self.value]

        return f"{_value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']
        values = [ num for num in range(1, 14) ]
        for s in suits:
            for val in values:
                self.cards.append(Card(s, val))

    def show(self):
        for card in self.cards:
            _value = card.value
            if card.value in ROYAL_CARDS:
                _value = ROYAL_CARDS[card.value]

            print(f"{_value} of {card.suit}")

    def shuffle(self):
        random.shuffle(self.cards)


    def draw(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        # draw 7 cards and add to hand
        print(f"{self.name} is drawing 7 cards.")
        for i in range(1, 8):
            self.hand.append(deck.draw())

    def show_hand(self):
        if not self.hand:
            return f"No cards left in {self.name}'s hand."
        print(f"{self.name}'s hand contains: ")
        for card in list(self.hand):
            _value = card.value
            if card.value in ROYAL_CARDS:
                _value = ROYAL_CARDS[card.value]

            print(f"{_value} of {card.suit}")

    def play_card(self):
        played = self.hand.pop().reveal()
        print(f"{self.name} has played the: {played}")


if __name__ == '__main__':
    d = Deck()
    d.shuffle()
    d.show()
    p1 = Player('lj')
    print(f"Welcome {p1.name}")
    p1.draw(d)
    p1.show_hand()
    p1.play_card()
    p1.show_hand()
    p1.play_card()
    p1.show_hand()