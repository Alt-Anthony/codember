with open("message_02.txt") as lista:
    leer = lista.read()

""""#" Incrementa el valor numérico en 1.
"@" Decrementa el valor numérico en 1.
"*" Multiplica el valor numérico por sí mismo.
"&" Imprime el valor numérico actual."""

count =" ";
intcount=0;
for i in leer:
    if i == '#':
        intcount=intcount+1
    elif i=='@':
        intcount=intcount-1
    elif i=='*':
        intcount=intcount*intcount
    elif i =='&':
        count = count+str(intcount)
print(f"submit"+count)