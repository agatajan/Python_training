#definicja pojedynczej karty
class Card():

    FIGURES = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    COLORS = ["hearts", "clubs", "diamonds", "spades"]

    def __init__(self, figure, color):
        self.__figure = figure
        self.__color = color

    #metoda do przedstawienia karty(przedstawienia obiektu)
    def __str__(self):
        return f"{self.__figure} of {self.__color}"

#klasa przechowujaca talie kart/kontener na karty/kontenerem na karty bedzie nasza lista
#zeby stworzyc talkie karte nalezy przemnozyc kolory razy figury
class CardDeck():

    def __init__(self):
        self.__deck = []
        for figure in Card.FIGURES:
            for color in Card.COLORS:
                self.__deck.append(Card(figure, color))

    def cards_count(self):
        return len(self.__deck)

    def __str__(self):
        return self.show_all_the_cards()

#self.__deck ---> pusta talia kart, do ktorej mozemy dodawac kolejne elementy

    def show_all_the_cards(self):
        string_to_return = ""
        for card in self.__deck:
            string_to_return += str(card) + "\n"

        # string_to_return += str(self.__deck[0]) + "\n"
        # string_to_return += str(self.__deck[1]) + "\n"
        # string_to_return += str(self.__deck[2]) + "\n"

        return string_to_return


deck_of_cards = CardDeck()
print(deck_of_cards.cards_count())

print(deck_of_cards)

