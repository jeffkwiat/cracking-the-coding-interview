import unittest


'''
Write a method to replace all spaces in a string with ‘%20’

'''

class StringAlgorithm(object):
    def __init__(self):
        pass

    @staticmethod
    def replace(input, replace, replace_with):
        # 1.  loop through string and look for spaces
        # 2.  loop through string again and replace spaces,
        # growing the return string by the length of replace_with

        result = []
        for letter in input:
            if letter == ' ':
                result.append('%20')
            else:
                result.append(letter)
        return ''.join(result)


    @staticmethod
    def replace_using_std(input, replace, replace_with):
        return input.replace(replace, replace_with)

class TestStringAlgorithm(unittest.TestCase):
    def setUp(self):
        pass

    def test_replace(self):
        self.assertEquals(StringAlgorithm.replace('a b', ' ', '%20'), 'a%20b')
        self.assertEquals(StringAlgorithm.replace('a b ', ' ', '%20'), 'a%20b%20')
        self.assertEquals(StringAlgorithm.replace('   ', ' ', '%20'), '%20%20%20')

    def test_replace_using_std(self):
        self.assertEquals(StringAlgorithm.replace_using_std('a b', ' ', '%20'), 'a%20b')

if __name__ == '__main__':
    unittest.main()