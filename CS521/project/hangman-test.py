import unittest
from game import Hangman


class TestHangman(unittest.TestCase):
    def test_correctGuess(self):
        word = ["w"]
        game = Hangman(word)
        game.correctGuess("w")
        self.assertTrue(game.correct[0] in game.chosenWord(), True)

    def test_wrongGuess(self):
        word = ["w"]
        game = Hangman(word)
        game.wrongGuess("o")
        self.assertFalse(game.wrong[0] in game.chosenWord(), False)


if __name__ == '__main__':
    unittest.main()
