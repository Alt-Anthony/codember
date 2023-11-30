with open("database_attacked.txt") as lista:
    leer = lista.read()


newList = leer.split("\n")
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
contraseña = ""
for i in range(0, len(newList)):
    list = newList[i].split(",")
    id = list[0]
    username = list[1]
    email = list[2]
    age = list[3]
    location = list[4]
    a = True
    b = False
    for j in id:
        if j not in letras:
            a=False
            break
    if email.count("@")==1 and email[0] !="@" and email[-1]=="m" and email.count(".")==1:
        b = True
    if not(id!="" and a==True):
        contraseña = contraseña+username[0]
        print(newList[i])
    elif not(email!="" and b==True):
        print(newList[i])
        contraseña = contraseña+username[0]



print(contraseña)

