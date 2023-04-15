import unittest
import main


class TestStringMethods(unittest.TestCase):

    def test_null(self):
        self.assertEqual(main.addition(''), 1)

    def test_one_number(self):
        self.assertEqual(main.addition('14'), 14)

    def test_two_numbers(self):
        self.assertEqual(main.addition('8, 3'), 11 + 1)





# if name == 'main':
#     unittest.main()
