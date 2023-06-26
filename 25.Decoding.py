import base64
 
cipher_text = 'cHJvZ3JhbW1pbmc='
plain_text = base64.b64decode(cipher_text)
 
print(plain_text.decode())