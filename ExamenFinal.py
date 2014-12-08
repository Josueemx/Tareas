######################################################
###NOTAS IMPORTANTES##################################
#LOS ARCHIVOS DEBEN DE ESTAR EN LA MISMA CARPETA######
#SI GUSTA, PUEDE ABRIRLO DESDE LA CONSOLA DE COMANDOS#
######################################################

print("ingrese mts^2 de aspas:")
mts=int(input("mts^2: "))
valor = float(mts*float(2.7))
print("el precio de su cantidad de mts^2 es: $"+str(round(valor),))


import re
print("Creando documento")
print("espere...")
clima = open("clima.csv","r")
rango = open("generacion.csv","r")
res = open("ResultadosExamenFinal.csv","w")

lista3 = []

for line in clima:
    lista = re.compile(r'\d*\-\d*\-\d*,\d*\,\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*')
    lista2 = re.findall(lista, line)
    if lista2 != []:
        lista3.append(lista2)

lista4=[]
lista5 =[]
for x in range(len(lista3)):
    str(lista3[x][0])
    lista4 = lista3[x][0].split(",")
    lista5.append(lista4)

lista6 =0
for x in range(len(lista5)):
    lista6 = int((int(lista5[x][17])/3.6))
    lista5[x][17] = lista6

for x in range(len(lista5)):
    if int(lista5[x][17]) >= 23:
        lista5[x][17] = 7452.3
    elif int(lista5[x][17]) == 1:
        lista5[x][17] = 0.6
    elif int(lista5[x][17]) == 2:
        lista5[x][17] = 4.9
    elif int(lista5[x][17]) == 3:
        lista5[x][17] = 16.5
    elif int(lista5[x][17]) == 4:
        lista5[x][17] = 39.2
    elif int(lista5[x][17]) == 5:
        lista5[x][17] = 76.5
    elif int(lista5[x][17]) == 6:
        lista5[x][17] = 132.3
    elif int(lista5[x][17]) == 7:
        lista5[x][17] = 210.1
    elif int(lista5[x][17]) == 8:
        lista5[x][17] = 313.6
    elif int(lista5[x][17]) == 9:
        lista5[x][17] = 446.5
    elif int(lista5[x][17]) == 10:
        lista5[x][17] = 612.5
    elif int(lista5[x][17]) == 11:
        lista5[x][17] = 815.2
    elif int(lista5[x][17]) == 12:
        lista5[x][17] = 1058.4
    elif int(lista5[x][17]) == 13:
        lista5[x][17] = 1345.7
    elif int(lista5[x][17]) == 14:
        lista5[x][17] = 1680.7
    elif int(lista5[x][17]) == 15:
        lista5[x][17] = 2067.2
    elif int(lista5[x][17]) == 16:
        lista5[x][17] = 2508.8
    elif int(lista5[x][17]) == 17:
        lista5[x][17] = 3009.2
    elif int(lista5[x][17]) == 18:
        lista5[x][17] = 3572.1
    elif int(lista5[x][17]) == 19:
        lista5[x][17] = 4201.1
    elif int(lista5[x][17]) == 20:
        lista5[x][17] = 4900
    elif int(lista5[x][17]) == 21:
        lista5[x][17] = 5672.4
    elif int(lista5[x][17]) == 22:
        lista5[x][17] = 6521.9
    else:
        ()

y = 0
valor = 0
for x in range(len(lista5)):
    y = round((float(lista5[x][17])*(0.0027)),4)
    lista5[x][17] = y
    valor+= y
    

res.write("fecha, cantidad generada\n")
for x in range(len(lista5)):
    res.write(str(lista5[x][0])+","+str(lista5[x][17])+"\n")


res.close()
rango.close()
clima.close()

print("listo!")

print("valor ahorrado durante al año: $"+str(round(valor,2)))

end = input("")
