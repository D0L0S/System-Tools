#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import requesocks
import stem.process
from stem.util import term

SOCKS_PORT = 5090

session = requesocks.session()
session.proxies = {
    'http': 'socks5://127.0.0.1:5090',
    'https': 'socks5://127.0.0.1:5090'
}

def connection():
	r = requests.get("https://www.atagar.com/echo.php")
	resp = r.content
	return resp

def query(url):
	r = session.get(url, verify=False)
	resp = r.content
	return resp

def print_bootstrap_lines(line):
	if "Bootstrapped " in line:
		print(term.format("     "+line, term.Color.BLUE))

def startTor():
	print(term.format(" [+] Starting Tor Connection", term.Attr.BOLD))
	global tor_process
	tor_process = stem.process.launch_tor_with_config(
		config = {
			'SocksPort': str(SOCKS_PORT),
			'ExitNodes': '{ru}',
		},
		init_msg_handler = print_bootstrap_lines,
	)

def stopTor():
	tor_process.kill() 
	
def main():
  try:
		startTor()
		print(term.format(" [+] Checking Endpoint...", term.Attr.BOLD))
		ExternalIP = connection()
		TORIP = query("https://www.atagar.com/echo.php")
		if ExternalIP == TORIP: 
		  print(term.format(" [!] FAILED TO CONNECT TO TOR", term.Color.RED))
		  exit(1)
		else: print(term.format(" [+] Successfully Connected to TOR", term.Attr.BOLD))
		## ADD STEPS HERE
		stopTor()  # stops tor
		
	except Exception as e:
		print "ERROR: {error}".format(error=e)
		stopTor()  # stops tor
		
if __name__=="__main__":
	main()
