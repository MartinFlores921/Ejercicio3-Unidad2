
import csv
from ClaseRegistro import Registro
from ClaseMenu import Menu
"""def test():
    m = Registro(8, 7.1, 9.9)
    m.getvalores()"""
if __name__ == '__main__':
    #test()
    lista= [] #creo la matriz bidimensional por decirlo asi
    m= 30 # "m" hace referencia a mes
    h= 24 # "h" hace referencia a hora
    archivo = open("VariablesDelMes.csv")
    reader = csv.reader(archivo, delimiter=";")
    next(reader)
    for i in range(m):        
        lista.append([Registro(0,0,0)]*24)
    for fila in reader:
        dia= int(fila[0])
        hora = int(fila[1])
        instancia= Registro(float(fila[2]), int(fila[3]), int(fila[4]))
        lista[int(fila[0])-1] [int(fila[1])-1] = instancia
    archivo.close()
    print("Ingrese la Opcion")
    print("1: Mostrar para Cada Variable el dia y hora de menor y mayor \n")
    print("2: Indicar la temperatura promedio mensual por cada hora")
    print("3: Listar los valores de las tres variables \n")
    op = int(input("4: Salir \n"))
    menudeopciones = Menu(op,lista)
    menudeopciones.menu()
    
    
    