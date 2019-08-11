import matplotlib.pyplot as mpplot
import matplotlib.image as mpimg
import os
from DAY_11.cards import CardDeck, Card
deck_of_cards = CardDeck()
deck_of_cards.shuffle()
# print(deck_of_cards.get_card())
cards_to_deal = 5
figure, axes = mpplot.subplots(nrows=1, ncols=cards_to_deal)
for ax in axes.ravel():
   ax.get_xaxis().set_visible(False)
   ax.get_yaxis().set_visible(False)
   img =  mpimg.imread(str(os.path.join(os.getcwd(), "cards", deck_of_cards.get_card().image_name)))
   ax.imshow(img)
figure.show()
figure.waitforbuttonpress()