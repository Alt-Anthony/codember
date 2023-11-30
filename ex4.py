with open("files_quarantine.txt") as lista:
    leer = lista.read()

newList = leer.split("\n")
totalmalas = 0
totalbuenas = 0
lsit = []
for i in range(0,len(newList)):
    elemento = newList[i].split("-")
    codigo = elemento[0]
    checksum = elemento[1]
    for j in range(0,len(codigo)):
        if codigo.count(codigo[j])>1:
            new = codigo.replace(codigo[j],"")
    print(f"-{codigo}-{checksum} {i}")
    if 
