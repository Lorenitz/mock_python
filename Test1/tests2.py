import unittest
from unittest.mock import patch, MagicMock

from main2 import len_joke, get_joke

class TestJoke(unittest.TestCase):

    # This decorator replaces the function get_joke() (inside main2.py) with a mock object during the tests.
    @patch('main2.get_joke')
    # This is the mock version of get_joke(), automatically passed as an argument to the test function
    def test_len_joke(self, mock_get_joke):
        # this tells the mock function mock_get_joke() to always return 'one' when called, instead of executing its real logic.
        mock_get_joke.return_value = 'one'
        # calls len_joke(), which (in the real main2.py), likelly calls get_joke() to fetch a joke.
        # since get_joke() is mocked to return 'one', len_joke() operates on 'one'
        # the tests expects len_joke() to return 3, which suggests len_joke() is computing len('one'), which is indeed 3.
        self.assertEqual(len_joke(), 3)

    @patch('main2.requests')
    def test_get_joke(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value':
        {'joke': 'hello world'}}

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), 'hell o world')

if __name__ == '__main__':
    unittest.main()        