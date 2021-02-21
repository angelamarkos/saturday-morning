import logging
logging.basicConfig(level=logging.INFO, filename='logs_1.log',
                    format='%(asctime)s -- %(levelname)s -- %(name)s -- %(message)s.')

logger = logging.getLogger('test1')
formatting = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s.')
file_handler = logging.FileHandler('log_2.log')
file_handler.setFormatter(formatting)
logger.addHandler(file_handler)
logger.setLevel(logging.ERROR)
def my_func(a, b, c):

    try:
        value = a * b / c
        logger.error(f'Result is {value}!')
        return value
    except ZeroDivisionError as e:
        logger.exception(f'DivisionError')

my_func(1, 2, 0)

'''DEBUG-10
INFO-20
WARNING-30
ERROR-40
CRITICAL-50'''