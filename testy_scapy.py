#!/usr/bin/env python

from scapy.all import *

packet = IP(dst="178.216.201.47")/ICMP()
#packet = IP(src="1.1.1.1", dst="193.187.68.16")/ICMP()

#reply = sr1(packet)

#if "193.187.68.16" in reply.src:
#    print ls(reply)
#    reply.show()

#adres = ['192', '168','0', '1']
#print ".".join(adres)

#print packet.src
#print packet.dst
#print packet.ttl
ans,uns = sr(packet)

#print ans.summary()
#print "*" * 100
#print uns.summary()
