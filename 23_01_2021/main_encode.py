from encode_decode import b_encode, b_decode

if __name__ == '__main__':
    string_to_encode = input('Expression: ')
    print(b_encode(string_to_encode))
    print(b_decode(b_encode(string_to_encode)))