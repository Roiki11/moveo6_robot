#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For http://bitforestinfo.blogspot.com
# This Script is Written By
#__author__='''

######################################################
                By S.S.B Group
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''

# import modules
import socket
import struct
import binascii
import os
import pye

# print author details on terminal
print pye.__author__

# if operating system is windows
if os.name == "nt":
    s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
    k = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
    s.bind(("",11000))
    k.bind(("",11002))
    s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    s.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

# if operating system is linux
else:
    s=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

# create loop
while True:

    # Capture packets from network
    pkt=s.recvfrom(65565)

    # extract packets with the help of pye.unpack class
    unpack=pye.unpack()

    print "\n\n===&gt;&gt; [+] ------------ Ethernet Header----- [+]"

    # print data on terminal
    for i in unpack.eth_header(pkt[0][0:14]).iteritems():
        a,b=i
        print "{} : {} | ".format(a,b),
    print "\n===&gt;&gt; [+] ------------ IP Header ------------[+]"
    for i in unpack.ip_header(pkt[0][14:34]).iteritems():
        a,b=i
        print "{} : {} | ".format(a,b),
    print "\n===&gt;&gt; [+] ------------ Tcp Header ----------- [+]"
    for  i in unpack.tcp_header(pkt[0][34:54]).iteritems():
        a,b=i
        print "{} : {} | ".format(a,b),
