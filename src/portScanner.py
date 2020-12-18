import sys 
import socket 
from datetime import datetime 

def portScanner(IP):
        # translate hostname to IPv4 
        ip = socket.gethostbyname(IP) 

        #prints status block of target and when the scan starts
        print("-" * 50) 
        print("Scanning: " + ip) 
        print("Scanning started at:" + str(datetime.now()).split('.')[0]) 
        print("-" * 50) 

        try: 
                # scan ports between 1 to 65,535
                openPorts = []
                for port in range(1,65535):

                        # create socket
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        socket.setdefaulttimeout(1) 
                        
                        # s.connect_ex() returns 0 if port is open 
                        c = s.connect_ex((ip,port))
                        if c == 0: 
                                print("Port",port,"is open")
                                openPorts.append(port)
                        s.close()

                print(" List of Open Ports:",openPorts)
                        
        except KeyboardInterrupt: 
                        print("\n Scan Stopped.") 
                        sys.exit() 
        except socket.gaierror: 
                        print("\n Hostname could not Be Resolved.") 
                        sys.exit() 
        except socket.error: 
                        print("\ Server could not be reached.") 
                        sys.exit()

#test code
IPadd = input("Please enter IP address: ")
portScanner(IPadd)
