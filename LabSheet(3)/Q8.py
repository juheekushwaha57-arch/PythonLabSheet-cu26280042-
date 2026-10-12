# 8. Convert a string into title case without using built-in functions

string = input("Enter a string: ")

result = ""
new_word = True

for char in string:
    if char == " ":
        result += char
        new_word = True
    else:
        if new_word:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
            new_word = False
        else:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char

print("Title case:", result)
