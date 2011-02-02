#!/usr/bin/python2.6
'''
This document takes a message, encrypts it, makes a base64 representation
Then takes the base64 representation, decodes it, decrypts it, and returns the original message
'''
#imports for Crypto
import base64
from serve_pages import default_page
#imports for HTTP
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
import cgi
import cgitb

#crypto imports
from CryptoUtils import encrypt,decrypt,makehash

class HttpHandler(CGIHTTPRequestHandler):

	def do_GET(self):
		try:
			print "GET received",self.path
			#if self.path.endswith(".html"):
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(default_page('encrypt','This is the input','','This is the output','',''))
			return
		except:
			self.send_error(404,'Where the hell you \'goin?')

	def do_POST(self):
		global rootnode
		try:
			print "POST received"
			form = cgi.FieldStorage(fp=self.rfile,
						headers=self.headers,
						environ={'REQUEST_METHOD':'POST',
							'CONTENT_TYPE':self.headers['Content-type']})
			action = 'encrypt'
			hashstring = ''
			inputString = ''
			secretString = ''
			tohashString = ''
			outputString = ''
			if "secret" in form:
				inputString = form['input'].value
				secretString = form['secret'].value
				inputString = cgi.escape(inputString,True)
				secretString = cgi.escape(secretString,True)
				if form['type'].value == 'encrypt':
					outputString = encrypt("AES",secretString,inputString)
					#keep the default behavior/action
				elif form['type'].value == 'decrypt':
					outputString = decrypt(secretString,inputString)
					#remain on decrypt
					action = 'decrypt'
			if "string" in form:
				tohashString = form['string'].value
				tohashString = cgi.escape(tohashString,True)
				hashstring = makehash(tohashString)		
			self.send_response(301)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(default_page(action,inputString,secretString,outputString,tohashString,hashstring))
			return
		except:
			pass


def main():
	try:
		#cgitb.enable()
		server = HTTPServer(('',8080),HttpHandler)
		print "Started server..."
		server.serve_forever()
	except KeyboardInterrupt:
		print "Interrupted - server shutdown"

if __name__=="__main__":
	main()
