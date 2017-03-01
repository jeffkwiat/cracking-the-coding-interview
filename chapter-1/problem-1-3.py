'''
Implement an algorithm to determine if a string has all unique characters. What if you
can not use additional data structures?
'''

import unittest

class StringAlgorithm(object):
    def __init__(self):
        pass

    def remove_duplicates(self, input):
        result = ''
        if not input:
            return input
        if len(input) < 2:
            return input
        import pdb; pdb.set_trace()
        for i in range(1, len(input)):
            for j in range(0, i):
                if input[i] == input[j]:
                    break
                result += input[j]

        return result





class TestStringAlgorithm(unittest.TestCase):
    def setUp(self):
        self.algorithm = StringAlgorithm()

    def test_remove_duplicates(self):
        # self.assertEquals(StringAlgorithm().remove_duplicates(''), '')
        # self.assertEquals(StringAlgorithm().remove_duplicates('a'), 'a')
        # self.assertEquals(StringAlgorithm().remove_duplicates('ab'), 'ab')
        # self.assertEquals(StringAlgorithm().remove_duplicates('aab'), 'ab')
        self.assertEquals(StringAlgorithm().remove_duplicates('aabbc'), 'abc')

if __name__ == '__main__':
    unittest.main()


