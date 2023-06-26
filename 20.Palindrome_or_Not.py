word = input('Enter the word to check: ')
if word == word[::-1]:
    print('The word is Palindrome')
else:
    print('The word is not Palindrome')