# This is a ping command file
import os
import sys
#os.system('cls')
def ping():
    print('#'*60)
    ip = raw_input('Enter IP to check: ')
    print('-'*60)
    os.system('ping {}'.format(ip))
    print('-'*60)
    sys.exit(1)

