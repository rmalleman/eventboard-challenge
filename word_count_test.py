import unittest
from word_count import word_count, count_words_in_a_file


class WordCountUnitTest(unittest.TestCase):

    def test_string(self):
        TEST_STRING = "the quick brown fox jumps over the lazy dog"
        TEST_STRING_ALTERED_CASE = "The QUick brOwn fox JUMPS over the Lazy Dog."
        EXPECTED_DICT = {
            'the': 2,
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'over': 1,
            'lazy': 1,
            'dog': 1
        }

        self.assertEqual(word_count(TEST_STRING), EXPECTED_DICT)
        self.assertEqual(word_count(TEST_STRING_ALTERED_CASE), EXPECTED_DICT)

    def test_file(self):
        FILE = './test_data/the-raven.txt'
        EXPECTED_DICT = {'poe': 1, 'dreadry': 1, 'upon': 1, 'weary': 1, 'allen': 1, 'while': 1, 'the': 1,
                         'pondered': 1, 'weak': 1, 'and': 1, 'raven': 1, 'i': 1, 'midnight': 1, 'once': 1, 'a': 1,
                         'edgar': 1}
        self.assertEqual(count_words_in_a_file(FILE), EXPECTED_DICT)

if __name__ == '__main__':
    unittest.main()