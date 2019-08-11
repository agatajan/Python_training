import random
import matplotlib.pyplot as mpplot
import matplotlib.image as mpimg
import os

class Card():
    FIGURES = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", \
               "jack", "queen", "king"]
    COLORS = ["hearts", "clubs", "diamonds", "spades"]

    def __init__(self, figure, color):
        self.__figure = figure
        self.__color = color

    def __str__(self):
        return f"{self.__figure} of {self.__color}"

    @property
    def image_name(self):
        return f"{self.__figure}_of_{self.__color}.svg.png"


class CardDeck():

    def __init__(self):
        self.__deck = []
        self.__current_card_index = 0
        for figure in Card.FIGURES:
            for color in Card.COLORS:
                self.__deck.append(Card(figure, color))



    def shuffle(self):
    #     shuffle cards
        self.__current_card_index = 0
        random.shuffle(self.__deck)

    def give_card(self):
        card_to_return = self.__deck[self.__current_card_index]
        self.__current_card_index += 1

        return card_to_return

    def cards_count(self):
        return len(self.__deck)

    def __str__(self):
        return self.show_all_the_cards()


    def show_all_the_cards(self):
        string_to_return = ""

        for card in self.__deck:
            string_to_return += str(card) + "\n"

        return  string_to_return
        # solution using list comprehension
        # return "\n".join([str(x) for x in self.__deck])

# deck_of_cards = CardDeck()
# deck_of_cards.shuffle()
# print(deck_of_cards.show_all_the_cards())
#
# number_of_cards = 5
# card_hand = []
#
# for i in range(5):
#     card_hand.append(deck_of_cards.give_card())
#
# for card in card_hand:
#     print(card)



deck_of_cards = CardDeck()
deck_of_cards.shuffle()
# print(deck_of_cards.get_card())
cards_to_deal = 5
figure, axes = mpplot.subplots(nrows=1, ncols=cards_to_deal)
for ax in axes.ravel():
   ax.get_xaxis().set_visible(False)
   ax.get_yaxis().set_visible(False)
   img =  mpimg.imread(str(os.path.join(os.getcwd(), "cards", deck_of_cards.give_card().image_name)))
   ax.imshow(img)
figure.show()
figure.waitforbuttonpress()





