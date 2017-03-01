'''
Implement an algorithm to determine if a string has all unique characters. What if you
can not use additional data structures?
'''

import unittest

class StringAlgorithm(object):
    def __init__(self):
        pass

    def are_string_characters_unique(self, input):
        return len(set(input)) == len(input)

    def are_string_characters_unique_inline(self, input):

        # for each letter in the input string
        for index_x, ch_x in enumerate(input):
            # for every other letter in the input string
            for index_y, ch_y in enumerate(input):
                if index_x != index_y:
                    if ch_x == ch_y:
                        return False
        return True

class TestStringAlgorithm(unittest.TestCase):
    def setUp(self):
        self.algorithm = StringAlgorithm()

    def test_characters_are_unique(self):
        self.assertTrue(self.algorithm.are_string_characters_unique(''))
        self.assertTrue(self.algorithm.are_string_characters_unique('a'))
        self.assertTrue(self.algorithm.are_string_characters_unique('ab'))
        self.assertTrue(self.algorithm.are_string_characters_unique('abcdefghijklmn'))

    def test_characters_are_not_unique(self):
        self.assertFalse(self.algorithm.are_string_characters_unique('abcc'))
        self.assertFalse(self.algorithm.are_string_characters_unique('aaaabbc'))

    def test_characters_are_unique_inline(self):
        self.assertTrue(self.algorithm.are_string_characters_unique_inline(''))
        self.assertTrue(self.algorithm.are_string_characters_unique_inline('a'))
        self.assertTrue(self.algorithm.are_string_characters_unique_inline('ab'))
        self.assertTrue(self.algorithm.are_string_characters_unique_inline('abcdefghijklmn'))

    def test_characters_are_not_unique_inline(self):
        self.assertFalse(self.algorithm.are_string_characters_unique_inline('abcc'))
        self.assertFalse(self.algorithm.are_string_characters_unique_inline('aaaabbc'))

if __name__ == '__main__':
    unittest.main()


