diccionario= dict()
for i in range(3):
    a = str(1+i)
    diccionario["pista "+ a] = "hola "+str(i)

for i in diccionario.items():
    print (i)
