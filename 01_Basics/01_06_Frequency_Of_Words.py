
my_sentence = "a a a b c d e a a b d"

word_count = {}

for word in my_sentence.split():
    if (word in word_count):
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)