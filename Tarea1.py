#Tarea 2do Parcial
#Josue Morales
#Todos los archivos deben de estar en la misma carpeta
#hay un ejemplo ya creado "ResultadosTareaEjemplo.txt", este archivo ya esta listo para uno nuevo "ResultadosTarea.txt"
#tarda aproximadamente de una hora con diez minutos

import re
import time

a = time.time()

print("Comenzando...")

gen = open("RF00059_vs_UTR_Todas_sp_unicas","r")
bus = open("UTR_Todas_sp_unicas_linea.txt","r")
res = open("ResultadosTarea.txt","w")

lista3 = []

for line in gen:
    lista = re.compile(r'\d{2}\.\d{1}\b *\d\.\d\b *\w{3}\-\S*\|\w{3}\|\S*')
    lista2 = re.findall(lista, line)
    if lista2 != []:
        lista3.append(lista2)
    
print("Primer paso de tres, listo!")

lista4 = [num for elem in lista3 for num in elem]

lista5 = []
for x in range(int(len(lista4))):
    if float(lista4[x][0:4])>=35.8:
        lista5.append(lista4[x][12:])

lista5=list(set(lista5))

doc = []
for line in bus:
    doc.append(line)
    
print("Segundo paso de tres, listo!")

res.write("IDs con Genoma\n")
count=1
for x in lista5:
    for y in range(int(len(doc))):
        if x in doc[y]:
            res.write("{}. ".format(count)+x+","+doc[y+1])
            count+=1
            break

res.close()
bus.close()
gen.close()

print("Tercero y ultimo, listo!")

b = time.time()
horas=int((b-a)//3600)
minutos= int(((b-a)%3600)//60)
seg = int((b-a)%60)

print("Tiempo transcurrido: "+str(horas)+ " hora(s), " + str(minutos)+ " minuto(s) y " + str(seg)+ " segundo(s).")

#ExpresionesR
#\d{2}\.\d{1}\b *\d\.\d{1,}\b *\D{1,}\d{1,}\S{1,}
#\w{3}\-\w*\|\w{3}\|\S*
#\w{3}\-\S*\|\w{3}\|\S*
#\d{2}\.\d{1}\b *\d\.\d\b *\w{3}\-\S*\|\w{3}\|\S*
