#!/usr/bin/python3
import sys
if __name__  == "__main__":
    argv = input().split()
    if len(argv) == 1:
        print('1 argument:\n1: {}'.format(argv[0]))
    elif len(argv) > 1:
        print('{} arguments: '.format(len(argv)))
        for i in range(len(argv)):
            print('{}: {}'.format(i + 1, argv[i]))
    else:
        print('0 arguments.')
