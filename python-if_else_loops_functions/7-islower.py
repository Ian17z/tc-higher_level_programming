#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) < 123:
        return True
    else:
        return False
if islower('a') == True:
    print('{} is {}'.format('a', 'lower'))
else:
    print('{} is {}'.format('a', 'upper'))