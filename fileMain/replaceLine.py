
def maniLine(line):
    with open('testfiles/text.txt', 'r') as f:
        data = f.readlines()
        data[line] = 'Changed by maniLine function\n'

    with open('testfiles/text.txt', 'w') as f:
        f.writelines(data)



maniLine(3)
