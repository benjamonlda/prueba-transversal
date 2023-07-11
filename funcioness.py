

import numpy
lista_nombre = []
lista_apellido = []
lista_ruts = []
lista_filas = []
lista_columnas = []
lista_entradas = []
lista_ganacias = []
cancha = numpy.zeros((10,10),int)
platium = 120000
gold = 80000
silver = 50000

def validar_opcion ():
    while True:
        try:
            opcion = int(input("ingrese opcion:"))
            if opcion in (1,2,3,4,5):
                return opcion
            else:
                print("error tu opcion debe tener un numero del 1 al 5")
        except:
            print("error debe tener un numero entero")

def validar_nom ():
      while True:
        nom = input("ingrese su nombre:")
        if len(nom.strip()) >= 3:
            return nom
        else:
            print("ingresar un nombre que tenga 3 letras")
  

def validar_rut ():
    while True:
       try:
           rut = int(input("ingrese un rut sin digito verificador:"))
           if rut >= 1000000 and rut <=30000000:
            return rut
           else:
            print("debe ingresar un rut entre 7 y 8 digito ")
       except:
          print("debe ingresar un numero entero")

def validar_apellido ():
    while True:
        apellido = input("ingrese su apellido:")
        if len(apellido.strip()) >= 3 and apellido.isalpha:
            return apellido
        else:
           print("ingresar un apellido que tenga 3 letras")
  

def ver_menu ():
    print(""" BIENVENIDO AL CONCIERTO MAS INCREBLE DEL MUNDO
    1.COMPRAR ENTRADAS
    2.MOSTRAR UBICACIONES DISPONIBLES
    3.VER ASISTENTE
    4.MOSTRAR GANACIAS
    5.salir
    """)

def validar_compra_de_entradas():
     while True:
        try:
            entradas = int(input("ingrese opcion:"))
            if entradas in (1,2,3):
                return entradas
            else:
                print("error tu opcion debe tener un numero del 1 al 3")
        except:
            print("error debe tener un numero entero")




def comprar_entradas():
 while True:
    nom =validar_nom()
    apellido = validar_apellido()
    rut = validar_rut()
    entradas = validar_compra_de_entradas
    print(precios())
    print(cancha)
    filas = filas()
    columnas = columnas()
    if cancha [filas-1][columnas-1] == 0:
     cancha [filas-1][columnas-1] == 1

    if filas == 1 and 2:
        print ("usted adquerido la entrada platium que tiene un valor de ",platium,)
    elif filas == 3 and 4:
        ("usted adquerido la entrada platium que tiene un valor de ",gold,)
    if filas == 5 and 6:
       ("usted adquerido la entrada platium que tiene un valor de ",silver,)
    else:
       lista_filas in 0
       print ("no esta disponible")

    total= entradas*filas
    print("su total seria",total,)

    nom = lista_nombre.append(nom)
    apellido = lista_apellido.append(apellido)
    rut = lista_ruts.append(rut)
    columnas = lista_columnas.append(columnas)
    filas = lista_filas.append(filas)
    entradas = lista_entradas.append(entradas)
    
    

def ver_asistentes ():
    print("asistentes")
    print(lista_nombre)


def salir ():
  print ("vuelva pronto")
  print ("nombre",lista_nombre,)
  print ("apellido",lista_apellido,)
  print("fecha 11/07/2023")
  
def ver_cancha ():
    for x in range (10):
     print (f"fila {x+1}",end=" ")
     print (cancha[x])
    for y in range(10):
     print (f"columna {x+1}",end=" ")
     print (cancha[y])
    print(cancha[x][y],end= " ")
    print("columas 1 2 3 4 5 6 7 8 9 10")
    print("fila 1 2 3 4 5 6 7 8 9 10")
    
def precios ():
    print("""""
    Platinum = 120.000 
    gold = 80.000 
    silver = 50.000 
    """)

def filas ():
    while True:
       try:
           fila = int(input("ingrese una fila 1-10:"))
           if fila in(1,2,3,4,5,6,7,8,9,10):
            if filas == 1 and 2:
                print ("usted adquerido la entrada platium que tiene un valor de ",platium,)
            elif filas == 3 and 4:
                 ("usted adquerido la entrada platium que tiene un valor de ",gold,)
            elif filas == 5 and 6:
              ("usted adquerido la entrada platium que tiene un valor de ",silver,)
            else:
                lista_filas in 0
                print ("no esta disponible")
            return fila   
       except:
             print("debe ingresar un numero entero")

def columnas ():
    while True:
       try:
           columnas = int(input("ingrese una columnas 1-10:"))
           if columnas in(1,2,3,4,5,6,7,8,9,10):
             return columnas
           else: 
               print(" ERROR!!! DEBE ESTAR ENTRE 1-10")
       except:
             print("debe ingresar un numero entero")

def ganacias():
  print(lista_ganacias)
  