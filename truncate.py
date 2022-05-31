lst = []

for i in range(10):
    lst.append("written {}".format(i))

with open('textfiles/text.txt', 'r+') as textfile:
    textfile.truncate(0)

for line in lst:
    with open('textfiles/text.txt', 'a') as textfile:
            textfile.write("this is line " + line + "\n")

