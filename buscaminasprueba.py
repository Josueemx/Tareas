import re


#la lista (c) es un tablero creado del codigo de luisra, solo que para no batallar con dos variables lo hice una sola lista, osea de esto c[x][y] paso a esto c[x]
#la lista (esp) es una lista llena de espacios que rellena el template 
a = [['*', '', '', '', '', '', '*', '', ''], ['', '', '', '', '', '*', '*', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '*', '', '', '', '', '', ''], ['', '', '', '', '', '', '*', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '*', '*', '', '', ''], ['*', '', '', '', '', '', '', '', '*'], ['', '', '', '', '', '', '', '', '']]
b = [[True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True]]
#c = [1, '*', 1, 0, 1, 3, '*', 2, 0, 1, 1, 1, 0, 1, '*', '*', 2, 0, 0, 1, 1, 1, 1, 2, 2, 1, 0, 0, 1, '*', 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, '*', 1, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 1, 1, 0, 1, '*', '*', 1, 1, 1, '*', 1, 0, 1, 2, 2, 1, 1, '*', 1, 1, 0, 0, 0, 0, 0, 1, 1]
#c = [0, 0, 0, 0, 1, 3, '*', 2, 0, 0, 0, 0, 0, 1, '*', '*', 2, 0, 0, 1, 1, 1, 1, 2, 2, 1, 0, 0, 1, '*', 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, '*', 1, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 1, 1, 0, 1, '*', '*', 1, 1, 1, '*', 1, 0, 1, 2, 2, 1, 1, '*', 1, 1, 0, 0, 0, 0, 0, 1, 1]
c = [1, 1, 2, '*', 2, '*', 2, 1, 2, 2, 2, 2, 2, '*', '*', 1, 1, '*', 2, '*', 2, '*', 1, 0, 1, '*', 1, '*', 2, 1, 2, 1, 3, '*', 4, '*', '*', 3, '*', 5, 3, 2, 1, 1, 2, 1, 2, 1, 1, 0, 1, 1, 2, 2, 1, 1, 1, 1, 3, '*', '*', 3, 2, 3, '*', 4, '*', 3, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, '*', 1, 0, 2, '*', 2, 2, '*', 3, 1, 0, 1, 1, 3, '*', '*', 2, 1, 1, 0, 2, '*', 2, 0, 1, 1, 2, 2, 1, 2, '*', 3, 2, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, '*', 1, 0, 2, '*', 2, 0, 1, '*', 2, '*', 1, 1, 2, '*', 1, 0, 1, '*', '*', 2, '*', '*', 2, 2, '*', 2, 1, 0, 1, 2, 3, 2, 2, 1, '*', 2, 1, 1, 2, 2, 1, 0, 1, 2, 3, 3, 3, 2, 2, '*', 2, 2, 2, 2, 1, 1, '*', '*', 2, 1, 1, 2, 1, 2, '*', 2, 1, 0, 0, 1, 3, '*', 3, 1, 2, 1, 2, 2, '*', '*', 1, 1, 2, 2, 2, '*', 1, 2, '*', 2, 2, '*', 1, 1, 2, 3, '*', '*', 3, '*', 1, 1, 3, '*', 4, 2, 1, 0, 1, 1, 2, 1, 1, '*', 2, 1, 1, 1, 2, 2, '*', '*', 3, 3, 3, 2, 1, 1, '*', '*', 3, 1, 0, 0, 1, '*', 1, 0, 2, 2, 2, 0, 1, 1, 2, '*', 4, 4, 3, 2, '*', 2, 2, 3, 4, 4, '*', 2, 1, 1, 1, 1, 1, 0, 1, '*', 2, 1, 1, '*', 2, 1, 2, '*', '*', 2, 1, 2, '*', '*', 3, '*', 2, 2, '*', 1, 0, 0, 0, 0, 1, 2, '*', 2, 2, 2, 1, 0, 2, 3, 4, 3, 3, 4, 4, 4, '*', 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 3, 2, 3, '*', 1, 0, 1, 2, '*', 2, '*', '*', '*', '*', 2, 2, 2, 2, '*', 2, 1, 1, 1, 1, 1, '*', 2, '*', 2, 1, 1, 0, 1, '*', 2, 2, 2, 4, '*', 3, 1, 2, '*', 3, 1, 3, '*', 3, 2, '*', 1, 1, 2, 1, 1, 0, 0, 0, 2, 2, 2, 1, 1, 2, 1, 1, 0, 2, '*', 2, 0, 2, '*', 3, '*', 2, 1, 0, 0, 1, 1, 1, 0, 0, 1, '*', 2, 3, '*', 3, 1, 1, 0, 1, 1, 1, 0, 1, 1, 2, 1, 1, 0, 0, 0, 2, '*', 2, 0, 0, 2, 3, 5, '*', '*', 3, '*', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, '*', 2, 0, 0, 2, '*', '*', '*', 4, 3, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, '*', 1, 1, 1, 1, 0, 0, 2, '*', 4, 3, '*', 2, 2, '*', 3, 2, 1, 0, 0, 0, 1, 2, 3, '*', '*', 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, '*', 3, 3, '*', '*', 2, 1, 1, 0, 2, '*', '*', 4, 3, '*', 1, 1, 2, 2, 1, 0, 0, 0, 0, 0, 2, 2, 3, '*', 4, 3, 2, '*', 1, 0, 3, '*', 6, '*', 2, 2, 2, 2, '*', '*', 1, 0, 0, 0, 0, 1, 2, '*', 2, 2, '*', 3, 3, 2, 2, 1, 3, '*', 4, '*', 2, 1, '*', 3, 3, 2, 2, 1, 1, 0, 0, 1, '*', 2, 1, 1, 2, '*', '*', 1, 1, '*', 3, 2, 2, 1, 1, 2, 4, '*', 3, 1, 1, '*', 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, '*', 1, 0, 0, 0, '*', 3, '*', '*', 1, 1, 2, '*', 2, '*', 1, 1, '*', 2, '*', 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
#win = [0, 0, 0, 0, 1, 3, "F", 2, 0, 0, 0, 0, 0, 1, "F", "F", 2, 0, 0, 1, 1, 1, 1, 2, 2, 1, 0, 0, 1, "F", 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, "F", 1, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 1, 1, 0, 1, "F", "F", 1, 1, 1, "F", 1, 0, 1, 2, 2, 1, 1, "F", 1, 1, 0, 0, 0, 0, 0, 1, 1]
win = [1, 1, 2, 'F', 2, 'F', 2, 1, 2, 2, 2, 2, 2, 'F', 'F', 1, 1, 'F', 2, 'F', 2, 'F', 1, 0, 1, 'F', 1, 'F', 2, 1, 2, 1, 3, 'F', 4, 'F', 'F', 3, 'F', 5, 3, 2, 1, 1, 2, 1, 2, 1, 1, 0, 1, 1, 2, 2, 1, 1, 1, 1, 3, 'F', 'F', 3, 2, 3, 'F', 4, 'F', 3, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 'F', 1, 0, 2, 'F', 2, 2, 'F', 3, 1, 0, 1, 1, 3, 'F', 'F', 2, 1, 1, 0, 2, 'F', 2, 0, 1, 1, 2, 2, 1, 2, 'F', 3, 2, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 'F', 1, 0, 2, 'F', 2, 0, 1, 'F', 2, 'F', 1, 1, 2, 'F', 1, 0, 1, 'F', 'F', 2, 'F', 'F', 2, 2, 'F', 2, 1, 0, 1, 2, 3, 2, 2, 1, 'F', 2, 1, 1, 2, 2, 1, 0, 1, 2, 3, 3, 3, 2, 2, 'F', 2, 2, 2, 2, 1, 1, 'F', 'F', 2, 1, 1, 2, 1, 2, 'F', 2, 1, 0, 0, 1, 3, 'F', 3, 1, 2, 1, 2, 2, 'F', 'F', 1, 1, 2, 2, 2, 'F', 1, 2, 'F', 2, 2, 'F', 1, 1, 2, 3, 'F', 'F', 3, 'F', 1, 1, 3, 'F', 4, 2, 1, 0, 1, 1, 2, 1, 1, 'F', 2, 1, 1, 1, 2, 2, 'F', 'F', 3, 3, 3, 2, 1, 1, 'F', 'F', 3, 1, 0, 0, 1, 'F', 1, 0, 2, 2, 2, 0, 1, 1, 2, 'F', 4, 4, 3, 2, 'F', 2, 2, 3, 4, 4, 'F', 2, 1, 1, 1, 1, 1, 0, 1, 'F', 2, 1, 1, 'F', 2, 1, 2, 'F', 'F', 2, 1, 2, 'F', 'F', 3, 'F', 2, 2, 'F', 1, 0, 0, 0, 0, 1, 2, 'F', 2, 2, 2, 1, 0, 2, 3, 4, 3, 3, 4, 4, 4, 'F', 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 3, 2, 3, 'F', 1, 0, 1, 2, 'F', 2, 'F', 'F', 'F', 'F', 2, 2, 2, 2, 'F', 2, 1, 1, 1, 1, 1, 'F', 2, 'F', 2, 1, 1, 0, 1, 'F', 2, 2, 2, 4, 'F', 3, 1, 2, 'F', 3, 1, 3, 'F', 3, 2, 'F', 1, 1, 2, 1, 1, 0, 0, 0, 2, 2, 2, 1, 1, 2, 1, 1, 0, 2, 'F', 2, 0, 2, 'F', 3, 'F', 2, 1, 0, 0, 1, 1, 1, 0, 0, 1, 'F', 2, 3, 'F', 3, 1, 1, 0, 1, 1, 1, 0, 1, 1, 2, 1, 1, 0, 0, 0, 2, 'F', 2, 0, 0, 2, 3, 5, 'F', 'F', 3, 'F', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 'F', 2, 0, 0, 2, 'F', 'F', 'F', 4, 3, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 'F', 1, 1, 1, 1, 0, 0, 2, 'F', 4, 3, 'F', 2, 2, 'F', 3, 2, 1, 0, 0, 0, 1, 2, 3, 'F', 'F', 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 'F', 3, 3, 'F', 'F', 2, 1, 1, 0, 2, 'F', 'F', 4, 3, 'F', 1, 1, 2, 2, 1, 0, 0, 0, 0, 0, 2, 2, 3, 'F', 4, 3, 2, 'F', 1, 0, 3, 'F', 6, 'F', 2, 2, 2, 2, 'F', 'F', 1, 0, 0, 0, 0, 1, 2, 'F', 2, 2, 'F', 3, 3, 2, 2, 1, 3, 'F', 4, 'F', 2, 1, 'F', 3, 3, 2, 2, 1, 1, 0, 0, 1, 'F', 2, 1, 1, 2, 'F', 'F', 1, 1, 'F', 3, 2, 2, 1, 1, 2, 4, 'F', 3, 1, 1, 'F', 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 'F', 1, 0, 0, 0, 'F', 3, 'F', 'F', 1, 1, 2, 'F', 2, 'F', 1, 1, 'F', 2, 'F', 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
#esp = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
##########################
########Falta ESP##########
#########################
d2={0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}


#este es un codigo de luisra para crear templates
def imprimir(tablero,tabbol):
        lenght=int(len(tablero)**.5)
        num = int(len(tablero))
        arriba="     "
        for x in range(lenght):
                arriba=arriba+d2[x] +"   "
        arriba="\n"+arriba+"\n" 
        vimp=""
        z = 0
        for x in range(lenght):
                for y in range(lenght):
                        if y ==0 and x<9:
                                vimp= vimp+str(x+1)+"  |"
                        if y ==0 and x>8:
                                vimp= vimp+str(x+1)+" |"
                        if tabbol[x][y]:
                                vimp=vimp+ " {{0[{}]}} ".format(z) +"|"
                                z+=1
                        if tabbol[x][y]==False:
                                vimp=vimp+ "["+(str(tablero[x][y]))+"]" +"|"
                vimp=vimp+"\n"
                
        arriba=arriba+vimp             
        return (print(arriba))
#imprimir(c,b)


newtemp ="     A   B   C   D   E   F   G   H   I   \n1  | {0[0]} | {0[1]} | {0[2]} | {0[3]} | {0[4]} | {0[5]} | {0[6]} | {0[7]} | {0[8]} |\n2  | {0[9]} | {0[10]} | {0[11]} | {0[12]} | {0[13]} | {0[14]} | {0[15]} | {0[16]} | {0[17]} |\n3  | {0[18]} | {0[19]} | {0[20]} | {0[21]} | {0[22]} | {0[23]} | {0[24]} | {0[25]} | {0[26]} |\n4  | {0[27]} | {0[28]} | {0[29]} | {0[30]} | {0[31]} | {0[32]} | {0[33]} | {0[34]} | {0[35]} |\n5  | {0[36]} | {0[37]} | {0[38]} | {0[39]} | {0[40]} | {0[41]} | {0[42]} | {0[43]} | {0[44]} |\n6  | {0[45]} | {0[46]} | {0[47]} | {0[48]} | {0[49]} | {0[50]} | {0[51]} | {0[52]} | {0[53]} |\n7  | {0[54]} | {0[55]} | {0[56]} | {0[57]} | {0[58]} | {0[59]} | {0[60]} | {0[61]} | {0[62]} |\n8  | {0[63]} | {0[64]} | {0[65]} | {0[66]} | {0[67]} | {0[68]} | {0[69]} | {0[70]} | {0[71]} |\n9  | {0[72]} | {0[73]} | {0[74]} | {0[75]} | {0[76]} | {0[77]} | {0[78]} | {0[79]} | {0[80]} |"


#aqui esta el template con ambos formatos (c y esp), imprimanlos para que vean como queda
print(newtemp.format(c))
print("----------------------------------------------")
print(newtemp.format(esp))
print("---------------------despues----------------------")
#temp ="     A   B   C   D   E   F   G   H   I   \n1  | {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |\n2  | {9} | {10} | {11} | {12} | {13} | {14} | {15} | {16} | {17} |\n3  | {18} | {19} | {20} | {21} | {22} | {23} | {24} | {25} | {26} |\n4  | {27} | {28} | {29} | {30} | {31} | {32} | {33} | {34} | {35} |\n5  | {36} | {37} | {38} | {39} | {40} | {41} | {42} | {43} | {44} |\n6  | {45} | {46} | {47} | {48} | {49} | {50} | {51} | {52} | {53} |\n7  | {54} | {55} | {56} | {57} | {58} | {59} | {60} | {61} | {62} |\n8  | {63} | {64} | {65} | {66} | {67} | {68} | {69} | {70} | {71} |\n9  | {72} | {73} | {74} | {75} | {76} | {77} | {78} | {79} | {80} |"


#aqui esta la funcion
#tiene 4 argumentos: casilla, este es un numero que seleciona el elemento de inside (lista c, el segundo argumento) y showing (lista esp, el tercer argumento)
# y por ultimo esta el template (el cuarto argumento)
#en pocas palabras, lo que hace esta funcion es que cambia los elementos de inside a showing de acuerdo a su posicion (cuando son llamados)
#si funciona cuando se escoge una mina o un numero pero cuando se escoje un cero hace un loop y todavia no se por que


def ceros(casilla, inside, showing, temp):
       lineas = int(len(inside)**.5)
       columnas = int(len(inside)**.5)
       casilla = str(casilla)
       if "F" in casilla:
           x = int(casilla[0:len(casilla)-1])
           if showing[x] in (0,1,2,3,4,5,6,7):
                   return
           else:
                   if showing[x] == "F":
                       showing[x] = " "
                       return(showing)
                   else:
                       showing[x] = "F"
                       return(showing)
       else:
           x = int(casilla)
           if showing[x]==inside[x]:
                   return
           else: 
                   if inside[x] == "*":
                           if showing[x] == "F":
                                   return(showing)
                           else:
                                   showing[x]=inside[x]
                                   return(showing)
                   elif inside[x] in (1,2,3,4,5,6,7):
                           if showing[x] == "F":
                                   return(showing)
                           else:
                                   showing[x]=inside[x]
                                   return(showing)
                   else:
                           if showing[x] == "F":
                                   return(showing)
                           else:
                                   showing[x]=inside[x]
                                   if x == 0:
                                           if inside[x+1] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1,inside,showing,temp)
                                           if inside[x+1+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1+columnas,inside,showing,temp)
                                           if inside[x+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+columnas,inside,showing,temp)
                                   elif x == columnas-1:
                                           if inside[x-1] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1,inside,showing,temp)
                                           if inside[x-1+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1+columnas,inside,showing,temp)
                                           if inside[x+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+columnas,inside,showing,temp)
                                   elif x == (lineas-1)*columnas:
                                           if inside[x-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-columnas,inside,showing,temp)
                                           if inside[x+1-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1-columnas,inside,showing,temp)
                                           if inside[x+1] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1,inside,showing,temp)
                                   elif x == (lineas*columnas)-1:
                                           if inside[x-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-columnas,inside,showing,temp)
                                           if inside[x-1-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1-columnas,inside,showing,temp)
                                           if inside[x-1] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1,inside,showing,temp)
                                   elif x > (lineas-1)*columnas and x < (lineas*columnas)-1 :
                                           if inside[x-1] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1,inside,showing,temp)
                                           if inside[x+1] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1,inside,showing,temp)
                                           if inside[x-1-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1-columnas,inside,showing,temp)
                                           if inside[x-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-columnas,inside,showing,temp)
                                           if inside[x+1-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1-columnas,inside,showing,temp)
                                   elif (x+1) % columnas == 0:
                                           if inside[x+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+columnas,inside,showing,temp)
                                           if inside[x-1+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1+columnas,inside,showing,temp)
                                           if inside[x-1] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1,inside,showing,temp)
                                           if inside[x-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-columnas,inside,showing,temp)
                                           if inside[x-1-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1-columnas,inside,showing,temp)
                                   elif x % columnas == 0:
                                           if inside[x+1+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1+columnas,inside,showing,temp)
                                           if inside[x+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+columnas,inside,showing,temp)
                                           if inside[x+1] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1,inside,showing,temp)
                                           if inside[x+1-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1-columnas,inside,showing,temp)
                                           if inside[x-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-columnas,inside,showing,temp)
                                   elif x > 0 and x < columnas-1:
                                           if inside[x+1+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1+columnas,inside,showing,temp)
                                           if inside[x+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+columnas,inside,showing,temp)
                                           if inside[x-1+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1+columnas,inside,showing,temp)
                                           if inside[x+1] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1,inside,showing,temp)
                                           if inside[x-1] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1,inside,showing,temp)
                                   else:
                                           if inside[x+1+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1+columnas,inside,showing,temp)
                                           if inside[x+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+columnas,inside,showing,temp)
                                           if inside[x-1+columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1+columnas,inside,showing,temp)
                                           if inside[x+1] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1,inside,showing,temp)
                                           if inside[x-1] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1,inside,showing,temp)
                                           if inside[x+1-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x+1-columnas,inside,showing,temp)
                                           if inside[x-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-columnas,inside,showing,temp)
                                           if inside[x-1-columnas] in (0,1,2,3,4,5,6,7):
                                                   ceros(x-1-columnas,inside,showing,temp)
           return(showing) 



def WinLooseContinue(showing):              
        if "*" in showing:
                return(print(newtemp.format(showing)+"\n\n            Has Muerto\n"))
#se tiene que ingresar el argumento
        elif showing == win:
                return(print(newtemp.format(showing)+"\n\n            Ganaste!!!!\n"))
        else:
                return(print(newtemp.format(showing)))
#casilla = str(input("casilla: "))
def evaluate(valor):
        if valor == None:
                z = esp
                '''
                #por que da error?????????
                print("\n")
                x = str(input("Casilla ya escojida, escoja otra, por favor: "))
                y = ceros(x,c, esp,newtemp)
                z = evaluate(y)
                mostrar = WinLooseContinue(z)
                '''
                mostrar = WinLooseContinue(z)
                print("esoje otra casilla")
                return(mostrar)
        else:
                mostrar = WinLooseContinue(valor)
                return(mostrar)


showing = ceros("0F",c,esp,newtemp)
print(showing)
evaluate(showing)

#WinLooseContinue(showing)

###########
#no se debe de poder abrir si hay un numero debajo de donde se quiere poner la "F" 
###########

#creo que temp en los argumentos ya no sirve

#regular expression profe - de numeros y F
#pagina - http://regex101.com/#python
#cosa - ^\s*(\d{1,2})\s*(\w*)
#ejemplo - 52F


#Traductor de tipo lista[x][y] a lista[x]
vec = [[1,2,3], [4,5,6], [7,8,9]]
var = [num for elem in vec for num in elem]
#print(var)
