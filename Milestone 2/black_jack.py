import random


class Deck(object):
    cards = dict.fromkeys([str(x) for x in range(2, 10+1)]+['J', 'Q', 'K', 'A'], 0)

    def getCards(self, numCards):
        x = 0
        newCards = []
        while x < numCards:
            card = random.choice(list(self.cards.keys()))
            if self.cards[card] >= 4:
                continue
            else:
                newCards.append(card)
                self.cards[card] += 1
                x += 1

        return newCards

    def reset(self):
        self.cards = dict.fromkeys(self.cards.keys(), 0)


class Player(object):

    def __init__(self):
        self.cards = []
        self.money = 500

    def addMoney(self, amount):
        self.money += amount

    def takeAwayMoney(self, amount):
        self.money -= amount

    def addCards(self, newCards):
        self.cards.extend(newCards)

    def resetCards(self):
        self.cards = []


class Dealer(object):

    def __init__(self):
        self.cards = []

    def resetCards(self):
        self.cards = []

    def checkCards(self, playerCards):
        playerCardsTotal = self.totalCards(playerCards)
        dealerCardsTotal = self.totalCards(self.cards)

        if playerCardsTotal > 21:
            return "Bust"
        elif playerCardsTotal < dealerCardsTotal:
            return "Lose"
        elif playerCardsTotal == dealerCardsTotal:
            return "Draw"
        elif playerCardsTotal > dealerCardsTotal:
            return "Win"

    def addCards(self, cards):
        self.cards.extend(cards)

    @staticmethod
    def aceDecision(total):
        if total + 11 > 21:
            return 1
        else:
            return 11

    def totalCards(self, cards):
        total = 0
        ace = False

        for card in cards:
            if card.isdigit():
                total += int(card)
            elif card != 'A':
                total += 10
            else:
                ace = True

        if ace:
            total += self.aceDecision(total)

        return total


class Display(object):

    @staticmethod
    def getStringInput(prompt, validStrings):
        while True:
            response = input(prompt)
            if response in validStrings:
                return response
            else:
                continue

    @staticmethod
    def getBet(money):
        while True:
            bet = None
            try:
                bet = int(input("Please enter a betting amount, you currently have ${0}: ".format(money)))
            except ValueError:
                print("Please enter a number")
            else:
                if bet <= 0:
                    print("You can't bet a negative amount, try again")
                    continue
                elif bet > money:
                    print("You can't bet more than you have!")
                    continue
                else:
                    return bet

    @staticmethod
    def showCards(whosCards, cards):
        print("{} has a ".format(whosCards), end='')
        for card in cards:
            print(card, end=' ')
        print()

    @staticmethod
    def showText(prompt):
        print(prompt)

def reset():
    player.resetCards()
    d.resetCards()
    deck.reset()
    player.addCards(
        deck.getCards(2)
    )
    bet = 0

deck = Deck()
d = Dealer()
player = Player()

play = True
bet = 0

reset()
while play:
    if bet == 0:
        bet = Display.getBet(player.money)
        Display.showText("You bet {0} and currently have ${1}".format(bet, player.money))

    Display.showCards("Player", player.cards)
    if d.totalCards(player.cards) < 21 and "hit" == \
            Display.getStringInput("Would you like to hold or hit? (hold/hit)", ["hold", "hit"]):
            player.addCards(
                deck.getCards(1)
            )
    else:
        while d.totalCards(d.cards) < 17:
            d.addCards(deck.getCards(1))
        Display.showCards("Dealer", d.cards)
        if 'y' == Display.getStringInput("You {0}. Play again? (y/n)".format(d.checkCards(player.cards)), ['y', 'n']):
            reset()
            player.addMoney(2*bet)
            bet = 0
            play = True
        else:
            player.takeAwayMoney(bet)
            play = False


