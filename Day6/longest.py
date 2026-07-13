def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

sentence = input("Enter a sentence: ")

result = longest_word(sentence)

print("Longest word:", result)
