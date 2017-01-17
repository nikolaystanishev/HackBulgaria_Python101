import unittest
from task import *


class TestDecorator(unittest.TestCase):
    def setUp(self):
        self.name = "S"

    def test_say_hello(self):
        self.assertEqual(say_hello(self.name),
                         "Hello, I am {}".format(self.name))
        with self.assertRaises(TypeError):
            say_hello(1)

    def test_deposit(self):
        self.assertTrue(deposit("ska", 9822))
        with self.assertRaises(TypeError):
            deposit(121, 9822)

    def test_get_low(self):
        self.assertEqual(get_low(), "Igv igv igv nqy")

    def test_somthing_heavy(self):
        self.assertEqual(something_heavy(), "I am done!")


if __name__ == "__main__":
    unittest.main()
