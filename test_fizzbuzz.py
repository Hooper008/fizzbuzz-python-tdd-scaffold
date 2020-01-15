import unittest
import fizzbuzz

class testfizzbuzzz(unittest.TestCase):

    def test(self):
        self.assertEqual(fizzbuzz.FizzBuzz(1).process(),'1')
        self.assertEqual(fizzbuzz.FizzBuzz(3).process(),'Fizz')
        self.assertEqual(fizzbuzz.FizzBuzz(5).process(),'Buzz')
        self.assertEqual(fizzbuzz.FizzBuzz(15).process(),'FizzBuzz')

    if __name__ == "__main__":
        unittest.main()