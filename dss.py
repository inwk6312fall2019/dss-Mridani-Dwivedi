import string
fin=open('name.txt')
line=fin.readline()
letter=''
for line in fin:
    word=line.strip()
    for char in line:
        if ((char in string.punctuation) or (char in string.whitespace)):
            pass
        else:
            letter += char.lower()
print(letter)