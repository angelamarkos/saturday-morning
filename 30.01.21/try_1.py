import unittest

def my_func():
    return 'Test string'

def func_1(a, b):
    return a/b

class Book:
    def __init__(self, title, author, published_date, page_count):
        self.title = title
        self.author = author
        self.published_date = published_date
        self.page_count = page_count

    def to_string(self):
        return f'{self.title}-{self.author}'


# if __name__ == '__main__':
#     my_test = MyTest()
#     my_test.test_func_1()
#     # assert func_1(1, 1) == 1, 'Should be 1'
#     # assert func_1(0, 1) == 0, 'Should be 0'
#     # try:
#     #     func_1(1, 0)
#     # except Exception as e:
#     #     assert str(e) == 'division by zero', 'should be division by zero'
