with open("message_01.txt") as lista:
    leer = lista.read()

print(type(leer))

listconverted = leer.split()
newlist = [];
count = []

for i in listconverted:
    if i not in count:
        count.append(i)

for i in count:
    newlist.append(listconverted.count(i))
print(newlist)
"newlist = listconverted.count(listconverted[3])"
"print(newlist)"

