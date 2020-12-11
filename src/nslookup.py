import os
import sys

def nslookup():
    print('#'*70)
    Host_name = raw_input('Enter the host name: ')
    print('-'*70)
    os.system('nslookup {}'.format(Host_name)) 
    print('-'*70)
    sys.exit(1)

