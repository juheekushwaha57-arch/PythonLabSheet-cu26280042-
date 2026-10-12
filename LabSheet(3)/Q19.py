# 19. Find the most repeated word in a string

text = input("Enter a string: ").lower()
words = text.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

if words:
    most_repeated = max(frequency, key=frequency.get)
    print("Most repeated word:", most_repeated)
    print("Frequency:", frequency[most_repeated])
else:
    print("No words found")

