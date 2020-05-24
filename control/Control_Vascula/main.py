#! /usr/bin/python3
# Importamos el modulo para la creación del archivo de excel
from fileManage import fileMAngage

if __name__ == "__main__":
    file = fileMAngage()
    kilos = 1
    # rutina para poder realizar las entradas necesarias
    while (kilos > 0):
        # Esperamos en terminal la entrada del dato 
        # lo convertimos en float para ingresar las decimales
        kilos = float(input("kilos pesados  "))
        # validamso la entrada
        if (kilos > 0):
            # se agrega al workspace el dato de los kilos
            file.addCount(kilos)
        # si kilos es 0 significa que ya no habrá 
        # más entradas por lo que cerramso el workspace
        # y exportamos el archivo
        else:
            print ("File created")
            file.closeFile()