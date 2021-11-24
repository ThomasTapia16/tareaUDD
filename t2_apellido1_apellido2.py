
#no se abre directamente el archivo ya que mi pc presentaba problemas tecnicos...



archivo = '1920-2020_final.csv'


def leer_guaguas(archivo):
    csv = open(archivo,'r')
    tupla = [] #esta lista luego será la tupla final
    lista_de_listas = [] #aca van todos los nombres
    contador = 0
    for x in csv:
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
    csv.close()
    return tupla
    
def guaguas_top_2020(archivo):
    csv = open(archivo,'r')
    dicc = {}
    lista_total = []
    
    for x in csv:
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
    
    csv.close()
    return lista_principal[0:10]

def guaguas_por_año(archivo):  
    csv = open(archivo,'r')
    dicc = {}
    lista_total = []
    
    for x in csv:
        dato = x.strip().split(";") #dato generará una lista con los datos de cada guagua
        if dato[0] != 'anio':
            dicc[dato[0]] = 0
            lista_total.append(dato[0]) #si el elemento indice 1 de cada lista no es 'nombre' entraran como clave de un diccionario
    for x in range(len(lista_total)):
        dicc[lista_total[x]] +=1
    csv.close()
    return dicc

def guaguas_sexo_anio(año,archivo):
    csv = open(archivo,'r')
    femenino = 0
    masculino = 0
    
    for x in csv:
        dato = x.strip().split(";")
        if dato[0] == año:
            if dato[2] == 'F':
                femenino += 1
            elif dato[2] == 'M':
                masculino += 1
    
    tupla = (femenino,masculino)
    csv.close()
    return tupla

def guaguas_sex_dicc(archivo):
    csv = open(archivo,'r')
    dicc = {}
    for x in csv:
        
        dato = x.strip().split(";")
        if dato[0] != 'anio':
            dicc[dato[0]] = ()
    
    for x in dicc:
        
        dicc[x] = guaguas_sexo_anio(x,archivo)
    csv.close()
    return dicc
def guaguas_escribir_archivo(archivo):
    nuevo = open("1920-2020_resumen.csv",'w')
    csv = open(archivo,'r')
    nuevo.write('anio;f;m\n')
    dicc = guaguas_sex_dicc(archivo)
    for x in dicc:
        nuevo.write(x+';'+str(dicc[x][0])+';'+str(dicc[x][1])+'\n')
    csv.close()

def efecto_romane(nombre,archivo):

    csv = open(archivo,'r')
    lista = []
    lista.append(nombre)
    nombre_repetido = 0
    for x in csv:
        dato = x.strip().split(";")
        if dato[1] == nombre and (dato[0] == '2000' or dato[0] == '1999'):
            nombre_repetido += 1
    lista.append(nombre_repetido)
    return lista

def brian_vs_kevin_bsb(archivo):
    csv = open(archivo,'r')
    dicc = {}
    brian = 0
    kevin = 0
    principal = []
    for x in csv:
        datos = x.strip().split(';')
        if datos[0] != 'anio' and int(datos[0]) >= 1996:
            dicc[datos[0]] = []
            if 'Brian' in datos[1]:
                print("si")
                brian += 1
        dicc[datos[0]] = brian
        
    print(dicc)
    csv.close()
    
# print(leer_guaguas(archivo))
# print(guaguas_top_2020(archivo))
# print(guaguas_por_año(archivo))
# print(guaguas_sexo_anio('2020',archivo))
# print(guaguas_sex_dicc(archivo))
#guaguas_escribir_archivo(archivo)
#print(efecto_romane('Yovanka',archivo))
brian_vs_kevin_bsb(archivo)
