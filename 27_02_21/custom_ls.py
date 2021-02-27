import os
import stat
import pwd
import grp
import argparse
import datetime

parser = argparse.ArgumentParser(description='Custom implementation of ls command')

parser.add_argument('paths', default=['.'], nargs='*', help='path of direcory')
parser.add_argument('-la', action='store_true', help='optional info')

args = parser.parse_args()

len_paths = len(args.paths)

for path in args.paths:
    if len_paths > 1:
        print(path)
    _, files, folders = next(os.walk(path))
    list_file_name = files + folders
    if not args.la:
        print(*list_file_name, sep='  ')
    else:
        rows = []
        for file_name in list_file_name:
            row = []
            stat_result = os.stat(file_name)
            ownership = stat.filemode(stat_result.st_mode)
            row.append(ownership)
            row.append(stat_result.st_nlink)
            row.append(stat_result.st_nlink)
            row.append(pwd.getpwuid(stat_result.st_uid).pw_name)
            row.append(grp.getgrgid(stat_result.st_gid).gr_name)
            row.append(stat_result.st_size)
            date_of_modified = datetime.datetime.fromtimestamp(stat_result.st_mtime)
            row.append(date_of_modified.strftime('%b %d %H:%M'))
            row.append(file_name)
            rows.append(row)
        formatting = '{: >2} ' * len(rows[0]) if rows else '{}'
        for row in rows:
            print(formatting.format(*row))
