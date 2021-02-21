def validate(decode_string):
    n = len(decode_string)
    if not n % 8 == 0:
        raise Exception('Length shoul be devided by 8')
    char_set = set(decode_string)
    if not char_set < {0, 1}:
        raise Exception('Should contains only 1 or 0')

print('xxxx')
print(__name__)
if __name__ == '__main__':
    pass