#!/usr/bin/python

from argparse import ArgumentParser
from docsis import Docsis

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('p',metavar="password",type=str,help="Password for modem")
    parser.add_argument('-u',metavar="username",type=str,default="cusadmin",help="Admin username for modem [default cusadmin]")
    parser.add_argument('-i',metavar="ip address",type=str,default="192.168.100.254",help="IP address for modem [default 192.168.100.254]")
   
    args = parser.parse_args()

    d = Docsis(args.u,args.p,args.i)
    print "Logging in..."
    r1= d.login()
    print "Restarting modem"
    print d.restart()
    
