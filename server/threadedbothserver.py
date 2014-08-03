#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

import os
import re
import threading
import SocketServer
import socket
from contamination import contaminlog
import __builtin__
import base64 as b64

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(65535).strip()
		if self.data:
			try:
				self.line = self.data

				matchObj = re.match('GET /this/should/never/be/real_anywhere/Filterbuster.html(.*)', self.line)
				if matchObj:
					print self.line
					self.reply1 = " - HTTP Allowed over port: "
					try:
						self.request.sendto(str(self.reply1), self.client_address)
					except Exception as e:
						print e
			except Exception as notxor:
				pass
			try:
				from itertools import cycle, izip
				key = 'filterbuster'
				self.line = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(self.data, cycle(key)))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = ": Filterbuster - " + self.line
					self.data = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(self.data, cycle(key)))
					self.request.send(self.data)
			except Exception as notxor:
				pass
			try:
				self.line = str(self.data).decode('rot13')
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = str(" : Filterbuster - "+str(self.line)).encode('rot13')
					self.request.send(self.data)
			except Exception as notro13:
				pass
			try:
				self.line = str(b64.b85decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be+ " " +self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b64.b85encode(" : Filterbuster - " + str(self.line))
					self.request.send(self.data)
			except Exception as notbase85:
				pass
			try:
				self.line = str(b64.b64decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " +self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b64.b64encode(" : Filterbuster - " + str(self.line))
					self.request.send(self.data)
			except Exception as notbase64:
				pass
			try:
				self.line = str(b64.b32decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b64.b85encode(" : Filterbuster - " + str(self.line))
					self.request.send(self.data)
			except Exception as notbase64:
				pass
			try:
				self.line = str(b64.b16decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b64.b85encode(" : Filterbuster - " + str(self.line))
					self.request.send(self.data)
			except Exception as notbase16:
				pass
			try:
				self.line = self.data
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.request.send(" : Filterbuster - " + self.data)
			except Exception as notplaintxt:
				pass
		else:
			contaminlog().jcom_keeper(self.client_address[0], str("tcp").upper(), self.client_address[1], self.data)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass


class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.data = self.request[0].strip()
		socket = self.request[1]
		if self.data:
			try:
				self.line = self.data

				matchObj = re.match('GET /this/should/never/be/real_anywhere/Filterbuster.html(.*)', self.line)
				if matchObj:
					print self.line
					self.reply1 = " - HTTP Allowed over port: "
					try:
						self.request.sendto(str(self.reply1), self.client_address)
					except Exception as e:
						print e
			except Exception as notxor:
				pass
			try:
				from itertools import cycle, izip
				key = 'filterbuster'
				self.line = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(self.data, cycle(key)))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = " : Filterbuster - " +self.line
					self.data = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(self.data, cycle(key)))
					socket.sendto(str(self.data[0::]), self.client_address)
			except Exception as notxor:
				pass
			try:
				self.line = str(self.data).decode('rot13')
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = str(" : Filterbuster - " + str(self.line)).encode('rot13')
					socket.sendto(str(self.data[0::]), self.client_address)
			except Exception as notro13:
				pass
			try:  # this actualy may not work - fix it
				self.line = str(b64.b85decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b64.b85encode(" : Filterbuster - " + str(self.line))
					socket.sendto(str(self.data[0::]), self.client_address)
			except Exception as notbase85:
				pass
			try:
				self.line = str(b64.b64decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b64.b64encode(" : Filterbuster - " + str(self.line))
					socket.sendto(str(self.data[0::]), self.client_address)
			except Exception as notbase64:
				pass
			try:
				self.line = str(b64.b32decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b32.b85encode(" : Filterbuster - " + str(self.line))
					socket.sendto(str(self.data[0::]), self.client_address)
			except Exception as notbase64:
				pass
			try:
				self.line = str(b64.b16decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b16.b85encode(" : Filterbuster - " + str(self.line))
					socket.sendto(str(self.data[0::]), self.client_address)
			except Exception as notbase16:
				pass
			try:
				self.line = self.data
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					socket.sendto(str(" : Filterbuster - " + self.data[0::]), self.client_address)
			except Exception as notplaintxt:
				pass

		else:
			contaminlog().jcom_keeper(self.client_address[0], str("udp").upper(), self.client_address[1], self.data)



class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
	pass


class bothserver(object):
	def __init__(self):
		pass

	def mybothserver(self):
		usocketserver = ThreadedUDPServer(('', int(serverport)), ThreadedUDPRequestHandler)
		usocketserver_thread = threading.Thread(target=usocketserver.serve_forever)
		usocketserver_thread.setDaemon(False)
		tsocketserver = ThreadedTCPServer(('', int(serverport)), ThreadedTCPRequestHandler)
		tsocketserver_thread = threading.Thread(target=tsocketserver.serve_forever)
		tsocketserver_thread.setDaemon(False)
		os.popen("iptables -t nat -F")
		os.popen("iptables -t nat -I PREROUTING -p tcp --dport 1:65534 -j REDIRECT --to-ports "+str(serverport))
		os.popen("iptables -t nat -I OUTPUT -p tcp -d 127.0.0.1 --dport 1:65534 -j REDIRECT --to-port "+ str(serverport))
		os.popen("iptables -t nat -I PREROUTING -p tcp --dport 65535 -j REDIRECT --to-ports 22")
		os.popen("iptables -t nat -I OUTPUT -p tcp -d 127.0.0.1 --dport 65535 -j REDIRECT --to-port 22")
		os.popen("iptables -t nat -I PREROUTING -p udp --dport 1:65535 -j REDIRECT --to-ports " + str(serverport))
		os.popen("iptables -t nat -I OUTPUT -p udp -d 127.0.0.1 --dport 1:65535 -j REDIRECT --to-port " + str(serverport))
		for sserver in [tsocketserver_thread, usocketserver_thread]:
			sserver.start()