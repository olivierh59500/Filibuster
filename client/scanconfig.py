#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

""" Useful information
initializes client scanner for further configuration
	checks if port range is a file or string
	builds port list used to scan from
	gets current date
	checks for randomness of port scanning
	check protocol being scanned (tcp / udp / both)
	check for scan type(currently: connect)
	checks for TLS wrapped communication
	calls socket creation function
		displays any diagnostics information as processes happen
"""

import random
import time
import os
import numpy as np
import __builtin__
from diagforall import socktesting
from diagforall import diagclientheader
from diagforall import csconf
from diagforall import ctsc
from diagforall import cusc
from pcolors import printfunction
from helper import helper
from tcpsock import tcpsocks
from udpsock import udpsocks
from bothsock import bothsocks
class initscanner():

	def __init__(self):
		pass
	def scanengine(self):
		if 1 == 1 :
			""" start stack build timer """
			__builtin__.stack_timer = time.time()
			__builtin__.stack = [] # stored port numbers here when generated from user specifications"
			__builtin__.passlist = []
			__builtin__.faillist = []
			# get the date information from local system
			""" maybe future addition, if NTP test passes use NTP server in EDU for data information """
			d = os.popen("date")
			dft = d.readline()
			__builtin__.ldate = str(dft.strip('\n')[4:7])+"-"+str(dft.strip('\n')[8:10])+"-"+str(dft.strip('\n')[24:29])
			__builtin__.u = 0

			""" check if the portrange configuration variable is a file or a range """
			if os.path.isfile(portr):
				with open(portr) as prange:
					for sport in prange:
						nstrip = sport.strip()
						stack.append(nstrip)
						try:
							stack.remove('\n')
						except Exception as stackrfail: # add in diagnostics handling for this error if one is caught
							print "stack remove failed: " + str(stackrfail)
							pass
						try:
							stack.remove('')
						except Exception as stackrfail: # add in diagnostics handling for this error if one is caught
							print "stack remove failed: " + str(stackrfail)
							pass
			else:
				if not os.path.isfile(portr):
					portrange = portr
					__builtin__.portranges = str(portrange).split("-")
					__builtin__.lowport = int(portranges[0])
					__builtin__.highport = int(portranges[1])
					__builtin__.base_port = int(lowport)
					__builtin__.end_port = int(highport)
					if str(diag).lower() in ["true","yes"]:
						try:
							from diagforall import portrng
							portrng().prange()
						except Exception as prangefail:
							print("\t"+bf+"ATTENTION "+be+bw+"[?] Client preperation for portrange "+bf+"FAILED"+be +" to:" + str(prangefail))
					__builtin__.s = int(lowport)
					__builtin__.t = int(highport)

					# iterate over port start and finish range
			for x in range(s,t):
				stack.append(x)
			stack.append(highport)
			if str(randomness).lower() in ["true","yes"]:
				#ls = random.choice(stack)
				random.shuffle(stack)
			else:
				pass
			__builtin__.total_stack = len(stack)
			print(bh+"\n\t[-] Starting "+be+str(scantype)+be+bh+" scanning process against server IP: "+be+ipaddr+be)
			while int(u) != total_stack:
				__builtin__.state = ""
				__builtin__.run_timer = time.time()
				if stack[0]:
					__builtin__.ls = stack[0]
					if sleepy == "random":
						__builtin__.rest = int(random.choice(np.arange(1,int(nappy),int(rester))))
					else:
						__builtin__.rest = rester
					__builtin__.u = int(u) + 1
					__builtin__.thread_count = int(u)
					__builtin__.cfb = str(flipbit)
					# configure connect scanner
					if  str(scantype).lower() == "connect":
						if (str(mytls)) == (str("no")):
							cfb = str(flipbit).lower()
							# initalize socket creation
							if cfb == "tcp":
								try:
									ctsc().clienttcpsockconf()
									socktesting().sockdiag()
									tcpsocks().connectsocket()
								except Exception as tcpconnectsocketfail:
									print("\t"+bf+"ATTENTION "+be+bw+"[?] Client failed to connect to TCP sockets "+ \
									      bf+"FAILED"+be+bw+" due to "+be+str(tcpconnectsocketfail))
									pass
								time.sleep(float(rest))
								stack.remove(ls)

							if cfb == "udp":
								try:
									cusc().clientudpsockconf()
									socktesting().sockdiag()
									udpsocks().connectsocket()
								except Exception as udpsockfail:
									print("\t"+bf+"ATTENTION "+be+bw+"[?] Client failed to connect to UDP sockets "+bf+"FAILED"+be+bw+" due to "+be+str(udpsockfail))
									pass
								time.sleep(float(rest))
								stack.remove(ls)

							# initalize socket creation

							if cfb == "both":
								try:
									cusc().clientudpsockconf()
									ctsc().clienttcpsockconf()
									socktesting().sockdiag()
									bothsocks().connectsocket()
								except Exception as tcpsockfail:
									print("\t"+bf+"ATTENTION "+be+bw+"[?] Client failed to connect to TCP/UDP sockets "+bf+"FAILED"+be+bw+" due to "+be+str(tcpsockfail))
								time.sleep(float(rest))
								stack.remove(ls)