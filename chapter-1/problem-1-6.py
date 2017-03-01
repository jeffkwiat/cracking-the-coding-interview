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

    def test_rotate(self):
        image0 = [[1]]
        image1 = [[1, 2],
                  [3, 4]]
        image2 = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

        self.assertEqual(ImageAlgorithm.rotate(image0), image0)
        self.assertEqual(ImageAlgorithm.rotate(image1), [[3, 1], [4, 2]])
        self.assertEqual(ImageAlgorithm.rotate(image2), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_rotate_in_place(self):
        image0 = [[1]]
        image1 = [[1, 2],
                  [3, 4]]
        image2 = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

        self.assertEqual(ImageAlgorithm.rotate_in_place(image0), image0)
        self.assertEqual(ImageAlgorithm.rotate_in_place(image1), [[3, 1], [4, 2]])
        self.assertEqual(ImageAlgorithm.rotate_in_place(image2), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

if __name__ == '__main__':
    unittest.main()