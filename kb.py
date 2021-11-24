
archivo = '1920-2020_final.csv'

def brian_vs_kevin_bsb(archivo):
    csv = open(archivo,'r')
    dicc = {}
    brian = 0
    kevin = 0
    
    for x in csv:
        
        datos = x.strip().split(';')
        
        if datos[0] != 'anio' and int(datos[0]) >= 1996:
            dicc[datos[0]] = [0,0]
            if 'Brian' in datos[1]:
                dicc[datos[0]][0] += 1
            elif 'Kevin' in datos[1]:
                dicc[datos[0]][1] += 1
            print(dicc)
        
    
   


brian_vs_kevin_bsb(archivo)