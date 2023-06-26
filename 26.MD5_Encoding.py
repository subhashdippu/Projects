import hashlib
 
input_word = input('Enter the word: ')
cipher_text = hashlib.md5(input_word.encode())
print('The MD5 for your input:', cipher_text.hexdigest())