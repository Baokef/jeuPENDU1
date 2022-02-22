
# print(content)
x = 0


def print_pendu(x):
    f = open("pendu.txt", "r")

    content = f.read()
    return content


print(print_pendu(110))
