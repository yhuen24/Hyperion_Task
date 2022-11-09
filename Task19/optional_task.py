# this file handler reads number of characters and words
with open('input.txt', 'r+') as f:
    data = f.read()  # reads the whole file
    words = data.split()  # split the file word by word
    word_count = len(words)  # length of words
    character_count = len(data)  # length of data would be the same as the number of characters including spaces
    print(f"The file has {character_count} number of characters")
    print(f"The file has {word_count} number of words")

# this file handler reads number of lines
with open('input.txt', 'r+') as f2:
    lines = f2.readlines()
    line_count = len(lines)
    print(f"The file has {line_count} number of lines")