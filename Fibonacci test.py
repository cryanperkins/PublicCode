__author__ = 'student'

import unittest
import Fibonacci


class MyTestCase(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(Fibonacci.fib(10), [1,1,2,3,5,8])


if __name__ == '__main__':
    unittest.main()
