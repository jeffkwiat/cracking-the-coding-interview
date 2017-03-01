import unittest

from collections import Counter


class StringAlgorithm(object):
    '''
    Write a method to decide if two strings are anagrams or not.

    '''

    def __init__(self):
        pass

    @staticmethod
    def are_strings_anagrams(input1, input2):
        if input1 == input2:
            return True

        dict1 = Counter(input1)
        dict2 = Counter(input2)

        return dict1 == dict2


class TestStringAlgorithm(unittest.TestCase):
    def setUp(self):
        pass

    def test_are_strings_anagrams(self):
        self.assertTrue(StringAlgorithm.are_strings_anagrams('bbaa', 'abba'))
        self.assertTrue(StringAlgorithm.are_strings_anagrams('baab', 'abba'))
        self.assertTrue(StringAlgorithm.are_strings_anagrams('a', 'a'))
        self.assertTrue(StringAlgorithm.are_strings_anagrams('', ''))

    def test_are_strings_not_anagrams(self):
        self.assertFalse(StringAlgorithm.are_strings_anagrams('abcba', 'bbabc'))

if __name__ == '__main__':
    unittest.main()


