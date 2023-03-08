import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def test_check_for_ace(self):
        ace_card = Card("Ace", 1)
        game = CardGame()
        self.assertEqual(True, game.check_for_ace(ace_card))

    def test_highest_card(self):
        card1 = Card("Spade", 10)
        card2 = Card("Heart", 5)
        game = CardGame()
        self.assertEqual(card1, game.highest_card(card1, card2))

    def test_cards_total(self):
        cards = []
        card1 = Card("Jack", 10)
        card2 = Card("King", 10)
        card3 = Card("Ace", 1)
        cards.append(card1)
        cards.append(card2)
        cards.append(card3)
        game = CardGame()
    

