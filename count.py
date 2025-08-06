
text = input("Enter a sentence: ")
words = text.split()
word_count = {}
for word in set(words):
    count = 0
    for w in words:
        if word == w:
            count += 1
    word_count[word] = count

print(word_count)
