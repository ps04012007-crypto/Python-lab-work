# Q5: Count frequency of words and characters

text = input("Enter a text string: ")

# Convert text to lowercase
text = text.lower()

# Count characters
character_frequency = {}

for ch in text:
    if ch != " ":
        if ch in character_frequency:
            character_frequency[ch] += 1
        else:
            character_frequency[ch] = 1

# Count words
words = text.split()
word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("\nCharacter Frequency:")
for ch in character_frequency:
    print(ch, ":", character_frequency[ch])

print("\nWord Frequency:")
for word in word_frequency:
    print(word, ":", word_frequency[word])
