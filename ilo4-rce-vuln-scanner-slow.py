#!/usr/bin/env python3

##################################
# Written by: sk1dish
# Date: 8/15/2019
##################################

import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getVersion(ip):
    url = "https://%s/json/login_session" % (str(ip))
    r = requests.get(url, timeout=1, verify=False)
    if (r.json()['version'] <= '2.53' and ('moniker' not in r.json() or r.json()['moniker']['PRODGEN'] == 'iLO 4')):
        ver = (r.json()['version'])
        print(("%s,%s") % (ip, ver))
    else:
        pass

if __name__ == '__main__':
    import argparse
    import sys
    parser = argparse.ArgumentParser(description="Crawl list of IP's or hostnames looking for HP iLO 4 vulnerable versions.")
    parser.add_argument('-ip', help="Specify IP's to check (multiple IP's/hostnames surrounded by double quotes with a space between them)")
    parser.add_argument('-iL', help="Path to file containing one IP/hostname per line to crawl")
    
    args = parser.parse_args()

    if args.ip is None and args.iL is None:
        print(("An argument is required. Run %s -h for help.") % (__file__))
        sys.exit()

    if args.ip:
        if args.ip is None:
            print("Specify IP's to check (multiple IP's/hostnames surrounded by double quotes with a space between them)")
            sys.exit()
        for ip in args.ip.split( ):
            try:
                getVersion(ip)
            except:
                pass

    if args.iL:
        if args.iL is None:
            print("Path to file containing one IP/hostname per line to crawl")
            sys.exit()
        with open(args.iL) as f:
            for ip in f.read().splitlines():
                try:
                    getVersion(ip)
                except:
                    pass

