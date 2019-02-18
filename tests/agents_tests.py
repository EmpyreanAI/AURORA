import unittest

class TestBaseAgent(unittest.TestCase):

    def test_hello2(self):
        self.assertEqual("hello3", "hello")


class TestRandomAgent(unittest.TestCase):

    def test_hello2(self):
        self.assertEqual("hello3", "hello")


if __name__ == '__main__':
    unittest.main()
