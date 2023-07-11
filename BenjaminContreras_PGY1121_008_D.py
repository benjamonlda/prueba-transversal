import os
import time
import msvcrt
import funcioness as fn



fn.ver_menu()
opcion = fn.validar_opcion()
if opcion==1:
   fn.comprar_entradas()
elif opcion==2:
   fn.ver_cancha
elif opcion==3:
   fn.ver_asistentes()
elif opcion ==4:
   fn.ganacias()
else: 
    fn.salir()
        
