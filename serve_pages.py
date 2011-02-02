#!/usr/bin/python2.6
'''
This class implements the server handler pages
'''

def default_page(checked,input_text,secret,output_text,checksummed_val,checksum):
	encryptChecked = 'checked'
	decryptChecked = ''
	if checked == 'decrypt':
		encryptChecked = ''
		decryptChecked = 'checked'		
	page = "<html>\n<head>\
<title>Secret Book</title></head>\
<body>\
<form action=\"server.py\" method=\"post\">\
Put the FB text here</br>\
<input type=\"radio\" name=\"type\" value=\"encrypt\" "+encryptChecked+"/> Encryption\
<input type=\"radio\" name=\"type\" value=\"decrypt\" "+decryptChecked+"/> Decryption\
</br>\
<textarea name=\"input\" type=\"text\" rows=\"4\" cols=\"40\">"+input_text+"</textarea>\
</br>\
<input type=\"text\" name=\"secret\" value=\""+secret+"\"/><input type=\"submit\" value=\"Submit\" />\
</br>Enjoy! :) </br>\
<textarea name=\"output\" type=\"text\" rows=\"4\" cols=\"40\">"+output_text+"</textarea>\
</br>Cryptographic checksum, for groups</br>\
<input type=\"text\" name=\"string\" value=\""+checksummed_val+"\"/><input type=\"submit\" value=\"Submit\" />\
</br><input type=\"text\" name=\"chksum\" size=\"53\" value=\""+checksum+"\"/>\
</br>Cipherpunks unite!\
<form>\
</body>\
</html>"
	return page

