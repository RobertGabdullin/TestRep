import unittest
import pytest
from unittest.mock import patch, call

from app.hangman import *

class HangmanTestCase(unittest.TestCase):

    def test_get_random_word(self):
        word = get_random_word()
        self.assertTrue(word in WORDS)

    @patch('builtins.input', side_effect=['\n'])
    @patch('builtins.print')
    def test_splash_screen(self, mock_print, mock_input):
        splash_screen()
        mock_print.assert_called()
        mock_input.assert_called_once_with("Press enter to continue...")

    @patch('builtins.input', side_effect=['t', 'a', 'b', 'c', 'd', 'r', 'y', 'u', 'n'])
    @patch('builtins.print')
    def test_hangman_game(self, mock_print, mock_input):
        with patch('app.hangman.get_random_word', return_value='test'):
            hangman()
        self.assertEqual(mock_print.call_count, 47)
        mock_input.assert_called_with("Play again? (y/n): ")

    @patch('builtins.input', side_effect=['t', 'a', 'b', 'c', 'd', 'r', 'y', 'u', 'n'])
    @patch('builtins.print')
    def test_hangman_game_play_again(self, mock_print, mock_input):
        with patch('app.hangman.get_random_word', return_value='test'):
            hangman()
        self.assertEqual(mock_input.call_count, 9)

    @patch('builtins.input', side_effect=['\n', 't', 'e', 'e', 'qwe', 's', 't', 'n'])
    @patch('builtins.print')
    def test_win(self, mock_print, mock_input):
        with patch('app.hangman.get_random_word', return_value='test'):
            hangman()
        mock_print.assert_any_call("You win!")
        mock_print.assert_any_call("You have already guessed that letter.")
        mock_print.assert_any_call("Invalid guess. Please enter a single letter.")
        

    @patch("builtins.input", side_effect=[KeyboardInterrupt])
    @patch("builtins.print")
    def test_interrupt(self, mock_print, mock_input):
        with pytest.raises(SystemExit):
            hangman()
        self.assertEqual(mock_print.call_count, 6)
	
if __name__ == '__main__':
    unittest.main()
