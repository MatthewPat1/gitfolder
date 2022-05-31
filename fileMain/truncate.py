lst = []

for i in range(10):
    lst.append("written {}".format(i))

with open('testfiles/text.txt', 'r+') as f:
    f.truncate(0)

for line in lst:
    with open('testfiles/text.txt', 'a') as f:
            f.write("this is line " + line + "\n")

