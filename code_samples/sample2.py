import sys, argparse
import re
from collections import defaultdict

class LiveHack:


        def __init__(self, filename):
            self.usernames = defaultdict(int) #defaultdict will make sure that value is 0
            self.d = {}
            self.ip_addresses = defaultdict(int)
            self.ip_port = dict()
            #------------------------------------
            f = open(filename)
            content = f.readlines()
            #------------------------------------
            for line in content:
                match_user = re.search('user\s(.*)from', line)
                # Group 1 : IP, Group 2: Port
                match_ip = re.search('((?:\d{1,3}\.){3}\d{1,3})\sport\s(\d+)', line)

                if match_user:
                    self.usernames[match_user.group(1)] += 1
                    self.d[match_user.group(1)] = hash(match_user.group(1))
                if match_ip:
                    self.ip_addresses[match_ip.group(1)] += 1
                    if match_ip.group(1) in self.ip_port:
                       self.ip_port[match_ip.group(1)].append(match_ip.group(2))
                    else:
                        self.ip_port[match_ip.group(1)] = [match_ip.group(2)]

            #------------------------------------

        def getAddresses(self):
            return self.ip_addresses
        def getUsernames(self):
            return self.usernames
        def getHash(self):
            return self.d

        def getAllAddressesByPort(self, start, end):
            temp = []
            for k, v in self.ip_port.items():
                for x in range(start, end + 1):
                    if str(x) in v:
                        temp.append({k:x})
            return temp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-filename", help="Filename relative")
    args = parser.parse_args()
    # python File.py -filename test.txt
    filename = args.filename
    if not filename:
        filename = 'livehack.txt'
    # should print test.txt
    print "Reading file: ", filename
    hack = LiveHack(filename)

    print "---------------------------"
    print "Printing out how many times an user is listed: "
    for k, v in hack.getUsernames().items():
        print "User:", k, " Count:", v
    print "---------------------------"
    print "Printing out hash value of usernames: "
    for k,v in hack.getHash().items():
        print "User:", k, " Hash:", v
    print "---------------------------"
    print "Printing out how many times an ip is listed: "
    for k, v in hack.getAddresses().items():
        print "IP:", k, " Count:", v
    print "---------------------------"
    print "Result of search: "
    for k in hack.getAllAddressesByPort(10650, 10651):
        print "IP", k

if __name__ == "__main__":
    main()