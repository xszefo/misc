#!/usr/bin/env python
import re

def get_ip (input):
    #return(re.findall(r'((?:(?:(?:25[0-5])|(?:2[0-4][0-9])|(?:[01]?[0-9][0-9]?)).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))', input))
     return(re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', input))



def main():
    test = "My ip: 192.168.255.255, not my ip: 192.168.0.1"

    print get_ip(test)

if __name__ == '__main__':
    main()








