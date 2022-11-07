content = ""
with open('DOB.txt', 'r+') as f:
    for line in f:
        content += line
    print(content)
