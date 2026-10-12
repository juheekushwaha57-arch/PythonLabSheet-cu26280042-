# 25. Count word frequency in a paragraph using a dictionary

paragraph = input("Enter a paragraph: ").lower()
words = paragraph.split()

frequency = {}

for word in words:
    word = word.strip(".,!?;:\"'()[]{}")
    if word:
        frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:", frequency)

