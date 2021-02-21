import time

def execution_time(f):
    def wrap_f(*args, **kwargs):
        print("starting timer")
        start_time = time.time()
        value = f(*args, **kwargs)
        end_time = time.time()
        print("Execution Time: {}".format(end_time-start_time))
        return value
    return wrap_f

def class_execution_time(cls):
    class NewCls:
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)


        def __getattribute__(self, item):

            try:
                attr = super().__getattribute__(item)
            except Exception as e:
                attr = self.instance.__getattribute__(item)
            else:
                return attr

            if callable(attr):
                print(attr.__name__)
                return attr
            x = execution_time(attr)
            return x

    return NewCls

@class_execution_time
class Calc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add_a_b(self):
        return self.a + self.b

    def sub_b_c(self):
        return self.b - self.c

    def div_a_c(self):
        return self.a / self.c

    @staticmethod
    def printing():
        return 'test'


calc = Calc(1, 2, 4)
print(calc.printing())
