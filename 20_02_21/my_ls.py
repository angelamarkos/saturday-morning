import sys
import os

if __name__ == '__main__':
    args = sys.argv[1:]
    path = None
    tags = []
    for arg in args:
        if arg.startswith('-'):
            tags.append(arg)
        elif not path:
            path = path
        else:
            raise Exception('Needs only one path.')

    if not path:
        path = '.'


    _, file_list, folder_list = next(os.walk(path))
    if not tags:
        print(file_list + folder_list)
    print(file_list[0])
    print(os.umask(os.stat(f'{path}/{file_list[0]}').st_mode))


