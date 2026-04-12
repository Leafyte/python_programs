def count_words(sentence):
    words = sentence.split()
    return len(words)

text = input("Enter a sentence: ")
result = count_words(text)

print("Number of words:", result)