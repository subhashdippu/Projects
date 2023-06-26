import base64
 
plain_text = 'programming'
cipher_text = base64.b64encode(plain_text.encode())
 
print(cipher_text.decode())