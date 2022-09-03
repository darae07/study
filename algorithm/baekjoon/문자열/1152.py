sentence = input()
words = list(filter(lambda x: len(x) > 0, sentence.split()))
print(len(words))
