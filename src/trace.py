import os
import sys

def option():
    print('Choose 1 if you are using Mac, 2 for Window, or 3 to exit')
    input_1 = input('Enter input: ')
    while(input_1!=3):
        if input_1 == 1:
            traceroute()
        elif input_1 == 2:
            tracert()
        else:
            print('Enter wrong input')
            print('-'*60)
            input_1 = input('Enter input again: ')

#Command for Window user
def tracert():
    print('#'*60)
    route_to_test = raw_input('Enter a route: ')
    print('-'*60)
    os.system('tracert {}'.format(route_to_test))
    print('-'*60)
    sys.exit(1)

#Command for Mac user
def traceroute():
    print('#'*60)
    route_to_test = raw_input('Enter a route: ')
    print('-'*60)
    os.system('traceroute {}'.format(route_to_test))
    print('-'*60)
    sys.exit(1)


