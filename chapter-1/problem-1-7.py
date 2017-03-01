import unittest


class ImageAlgorithm(object):
    """
    Given an image represented by an NxN matrix, where each pixel in the image is 4
    bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

    """

    def __init__(self):
        pass

    @staticmethod
    def rotate(image):
        """
        Rotate the matrix 90 degrees
        :return:
        """
        return [list(row) for row in zip(*image[::-1])]


    @staticmethod
    def rotate_in_place(image):
        """
        Rotate the matrix 90 degrees, but do it in place.
        :return:
        """
        results = []
        for col_index in range(len(image)):
            result = []
            for row_index in range(len(image) - 1, 0, -1):
               result.append(image[row_index][col_index])
        results.append(result)

        return results


class TestImageAlgorithm(unittest.TestCase):
    def setUp(self):
        pass

    def test_rotate_in_place(self):
        pass

if __name__ == '__main__':
    unittest.main()