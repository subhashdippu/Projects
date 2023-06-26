text = "John is good developer. John is a writer John"
words = text.split(' ')
counter = 0
for word in words:
    if word == "John":
        counter += 1
print(counter)