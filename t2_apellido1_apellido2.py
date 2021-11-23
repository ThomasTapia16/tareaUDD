import operator

archivo = open('1920-2020_final.csv','r')


def leer_guaguas(archivo):

    tupla = [] #esta lista luego será la tupla final
    lista_de_listas = [] #aca van todos los nombres
    contador = 0
    for x in archivo:
        if contador == 0:
            nombre_datos = x.strip().split(";") #cuando recorramos el primer elemento del csv lo capturamos
        else:
            a = x.strip().split(";")#creamos una lista 'a' que iremos agregando a 'lista_de_listas' donde
            #cada lista 'a' contiene los datos de cada guagua (lista de listas)
            lista_de_listas.append(a)
        contador +=1
    tupla.append(nombre_datos) #agregamos en el indice cero la lista con los nombres de los datos 
    tupla.append(lista_de_listas)#agregamos la lista de listas con los nombres
    tupla = tuple(tupla)# la lista tupla finalmente es una tupla ([],[[],[],...])
    return tupla
    
def guaguas_top_2020(archivo):
    dicc = {}
    lista_total = []
    
    for x in archivo:
        dato = x.strip().split(";") #dato generará una lista con los datos de cada guagua
        if dato[1] != 'nombre':
            dicc[dato[1]] = 0
            lista_total.append(dato[1]) #si el elemento indice 1 de cada lista no es 'nombre' entraran como clave de un diccionario
    for x in range(len(lista_total)):
        dicc[lista_total[x]] +=1
    lista_principal = []
    for clave,valor in dicc.items():
        l = []
        l.append(valor)
        l.append(clave)
        lista_principal.append(l)
    lista_principal.sort()
    lista_principal.reverse()
    
    
    return lista_principal[0:10]

def guaguas_por_año(archivo):  
    dicc = {}
    lista_total = []
    
    for x in archivo:
        dato = x.strip().split(";") #dato generará una lista con los datos de cada guagua
        if dato[0] != 'anio':
            dicc[dato[0]] = 0
            lista_total.append(dato[0]) #si el elemento indice 1 de cada lista no es 'nombre' entraran como clave de un diccionario
    for x in range(len(lista_total)):
        dicc[lista_total[x]] +=1
    return dicc

def guaguas_sexo_anio(año,archivo):
    femenino = 0
    masculino = 0
    
    for x in archivo:
        dato = x.strip().split(";")
        if dato[0] == año:
            if dato[2] == 'F':
                femenino += 1
            elif dato[2] == 'M':
                masculino += 1
    
    tupla = (femenino,masculino)
    return tupla

def guaguas_sex_dicc(archivo):
    dicc = {}
    for x in archivo:
        
        dato = x.strip().split(";")
        if dato[0] != 'anio':
            dicc[dato[0]] = ()
    for x in dicc:
        dicc[x] = guaguas_sexo_anio(dicc[x],archivo)
    print(dicc)

#print(leer_guaguas(archivo))
#print(guaguas_top_2020(archivo))
#print(guaguas_por_año(archivo))
#print(guaguas_sexo_anio('2020',archivo))
print(guaguas_sex_dicc(archivo))