from fb import fizzbuzz
import unittest


class Fizzbuzz_test(unittest.TestCase):
    def test_business_as_usual(self):
        self.assertEqual(fizzbuzz(4), 4)
        self.assertEqual(fizzbuzz(82), 84)
        self.assertEqual(fizzbuzz(88), 88)

    def test_fizz(self):
        self.assertEqual(fizzbuzz(33), 'fizz')
        self.assertEqual(fizzbuzz(66), 'fizz')
        self.assertEqual(fizzbuzz(99), 'fizz')

    def test_buzz(self):
        self.assertEqual(fizzbuzz(25), 'buzz')
        self.assertEqual(fizzbuzz(50), 'buzz')
        self.assertEqual(fizzbuzz(75), 'buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(30), 'fizzbuzz')
        self.assertEqual(fizzbuzz(60), 'fizzbuzz')
        self.assertEqual(fizzbuzz(90), 'fizzbuzz')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
