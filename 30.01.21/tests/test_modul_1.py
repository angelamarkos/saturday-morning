import unittest
from try_1 import func_1
from try_1 import my_func
from try_1 import Book


class MyTest(unittest.TestCase):
    def test_cust(self):
        self.assertEqual(func_1(1, 1), 1, 'Should be 1')
        self.assertEqual(func_1(0, 1), 0, 'Should be 0')
        self.assertRaises(ZeroDivisionError, func_1, 1, 0)
        with self.assertRaises(ZeroDivisionError):
            func_1(1, 0)

class TestBook(unittest.TestCase):
    def setUp(self) -> None:
        self.book_1 = Book('Raven', 'Edgar Alan Poe', published_date='Jan 01 1900', page_count=80)
        self.book_2 = Book('Title_1', 'Author_1', published_date='Jan 01 1900', page_count=80)

    def test_book(self):
        self.assertEqual(self.book_1.to_string(), 'Raven-Edgar Alan Poe', 'Wrong string formatting')
        self.assertEqual(self.book_2.to_string(), 'Title_1-Author_1', 'Wrong string formatting')

    def tearDown(self) -> None:
        del self.book_1
        del self.book_2




    def test_my_func(self):
        self.assertEqual(my_func(), 'Test string')