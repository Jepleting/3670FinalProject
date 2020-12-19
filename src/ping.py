# This is a ping command file
import os
import sys
#os.system('cls')
def ping(ip):
    print('-'*60)
    try:
        if os.system('ping {}'.format(ip)) != 0: # if it is not != 0 then something is wrong and raise Exception
            raise Exception('IP does not exist')
    except:
        print('Command does not work')
    print('-'*60)
    sys.exit(1)

ping()
