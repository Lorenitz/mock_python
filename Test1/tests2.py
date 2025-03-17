import unittest
from unittest.mock import patch

from main2 import len_joke

class TestJoke(unittest.TestCase):

    # This decorator replaces the function get_joke() (inside main2.py) with a mock object during the tests.
    @patch('main2.get_joke')
    # This is the mock version of get_joke(), automatically passed as an argument to the test function
    def test_len_joke(self, mock_get_joke):
        # this tells the mock function mock_get_joke() to always return 'one' when called, instead of executing its real logic.
        mock_get_joke.return_value = 'one'
        # calls len_joke(), which (in the real main2.py), likelly calls get_joke() to fetch a joke 
        self.assertEqual(len_joke(), 3)


if __name__ == '__main__':
    unittest.main()        