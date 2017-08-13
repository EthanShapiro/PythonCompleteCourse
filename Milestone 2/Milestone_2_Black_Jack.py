import random

class Player(object):

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.money = 500
        self.cards = []

    def win(self):
        self.wins += 1

    def lose(self):
        self.losses += 1

    def addCards(self, cards):
        self.cards.extend(cards)

    def getCards(self):
        return self.cards

class Deck(object):
    _deckNumStart = 1
    _deckNumEnd = 13
    cards = dict.fromkeys([str(x) for x in range(_deckNumStart, _deckNumEnd + 1)], 0)

    def getCards(self, numCards):
        x = 0
        c = []
        while x < numCards:
            card = random.randint(self._deckNumStart, self._deckNumEnd)
            if self.cards[str(card)] < 4:
                self.cards[str(card)] += 1
                c.append(card)
                x += 1
            else:
                continue

        return c


class Dealer(object):
    deck = Deck()

    def __init__(self):
        self.cards = []

    def dealCards(self, numCards):
        return self.deck.getCards(numCards)

    def addCards(self):
        self.cards.extend(self.dealCards(2))

p = Player()
d = Dealer()

play = True
while play:
    print(sorted(d.dealCards(52)))
    break