import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_1 = Card("club",1)
        self.card_2 = Card("heart",11)
        self.game_1 = CardGame()

    def test_check_for_ace_true(self):
        is_ace = self.game_1.check_for_ace(self.card_1)
        self.assertEqual(is_ace,True)

    def test_check_for_ace_false(self):
        is_ace = self.game_1.check_for_ace(self.card_2)
        self.assertEqual(is_ace,False)

    def test_highest_card(self):
        result = self.game_1.highest_card(self.card_1,self.card_2)
        self.assertEqual(result,self.card_2)

    def test_cards_total(self):
        cards = []
        cards.append(self.card_1)
        cards.append(self.card_2)
        result = self.game_1.cards_total(cards)
        self.assertEqual(result,"You have a total of 12") 