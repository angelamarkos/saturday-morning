import argparse

parser_parent = argparse.ArgumentParser(prog='MyLS', usage='%(prog)s [options]', epilog='End of help',
                                 description='Custom ls implementation. ...', add_help=False)


parser_parent.add_argument('path', type=str)
parser_parent.add_argument('-l','--list_1', type=int)


parser_1 = argparse.ArgumentParser(usage='%(prog)s [options_1]', parents=[parser_parent], prefix_chars='+/-')
parser_1.add_argument('+list', '--l', type=int)

args_1 = parser_1.parse_args(['path/to/file_1'])
# print(args_1.__dict__)
# print(args_1.l)

parser_2 = argparse.ArgumentParser(usage='%(prog)s [options_2]', parents=[parser_parent])
parser_2.add_argument('-a', type=int)
args_2 = parser_2.parse_args(['path/to/file_2', '-a 72', '-l 1'])
# print(args_2.__dict__)
# print(args.path_1)


# ---------------------------------------------

parser = argparse.ArgumentParser(description='Argument manipulation')


parser.add_argument('first_num', type=float)
parser.add_argument('second_num', type=float)

parser.add_argument('-m', '--mult', nargs='*', type=int)
parser.add_argument('-mm', '--mmult', nargs='+', type=int, action='append')
parser.add_argument('-f', '--d', action='append_const', const=1, dest='combine')
parser.add_argument('-c', '--c', action='append_const', const=2, dest='combine')
parser.add_argument("--foo", action="extend", nargs="+", type=str)
parser.parse_args(["--foo", "f1", "--foo", "f2", "f3", "f4"])
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-v', '--verbose', action='store_const', const=1, dest='verb')
group.add_argument('-l', '--list', nargs='?', type=int, action='append')

args = parser.parse_args(['1', '3', '-v', '-l'])
print(args.__dict__)

if args.verb == 1:
    print(f'Result is {args.first_num + args.second_num}')
elif args.verb == 2:
    print(f'Sum of {args.first_num} and {args.second_num} is {args.first_num + args.second_num}')
else:
    print(args.first_num + args.second_num)

