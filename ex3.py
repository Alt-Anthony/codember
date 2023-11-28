with open("encryption_policies.txt") as lista:
    leer = lista.read()
abc=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numeros=["1","2","3","4","5","6","7","8","9","0"]
total =0
totalbuenas =0
listconverted = leer.split("\n")
for i in range(0,len(listconverted)):
    a= listconverted[i].split(" ")
    for j in range(0,len(a)):
        count = a[0].split("-")
        numerador = a[1].split(":")
        codigo = a[2]
    min = int(count[0])
    max = int(count[1])
    letra = numerador[0]
    valor = codigo.count(letra)
    if min<=valor<=max:
        totalbuenas = totalbuenas+1
    else:
        total =total+1
    if total ==13:
        print(f"sudo {codigo}")
    elif total ==42:
        print(f"submit {codigo}")

print(f"total buenas: {totalbuenas}")