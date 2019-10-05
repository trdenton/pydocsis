#!/usr/bin/python

from docsis import Docsis
if __name__ == "__main__":
    d = Docsis('cusadmin','yourpasswordhere')
    print "Logging in..."
    r1= d.login()
    print "Lets configure wifi"
    print d.configure_wifi(False,False)
    
