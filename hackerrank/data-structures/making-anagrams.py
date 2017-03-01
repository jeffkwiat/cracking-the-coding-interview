import unittest

from collections import Counter

class NumberNeeded(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def number_needed(self, a, b):
        a_dict = Counter(self.a)
        b_dict = Counter(self.b)
        needed = 0

        for letter in a_dict:
            if letter not in b_dict or (a_dict[letter] != b_dict[letter]):
                needed += 1

        for letter in b_dict:
            if letter not in a_dict or (a_dict[letter] != b_dict[letter]):
                needed += 1

        return needed

# a = input().strip()
# b = input().strip()

# print(number_needed(a, b))

unittest.main()

class TestNumberNeeded(object):
    def setUp(self, a, b):
        self.a = a
        self.b = b

    def test_number_needed(self):
        assertEqual()
