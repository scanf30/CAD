#! /usr/bin/python3
# libreria para generar el excel
import openpyxl
# libreria para obtener la fecha y hora del sistema
import datetime


class fileMAngage(openpyxl.Workbook):
    # Inicialización de la clase
    def __init__(self):
        super(fileMAngage, self).__init__()
        # Creación del workspace para guardar los datos en formato Colunmas y filas
        self.initFile()

    def initFile(self):
        # Se crea el workspace en el que se va a trabajar
        self.workspace = self.active
        # Nombramos la hoja de excel
        self.workspace.title = 'demo'
        # iniciamos el contador de filas
        # para conocel la fila actual en
        # la que los datos serán guardados
        self.cont = 1

    # Función que exporta el workspace en un archivo excel 2010
    def saveFile(self):
        self.save(filename =  str(datetime.date.today()) + '.xlsx')

    # Función para agregar un nuevo dato al workspace
    # Recive como parametro el dato del peso
    def addCount(self, peso):
        # obtenemos la hora acutal del sistema
        now = datetime.datetime.now()
        # Se guarda la hora actual del sistama en 
        # la primera columna en el renglon actual
        # en formato Hora: Minutos: Segundos
        self.workspace['A'+str(self.cont)] = now.strftime("%H:%M:%S")
        # Guardamos el dato que recibimos como parametro 
        self.workspace['B'+str(self.cont)] = peso
        # Pasamos a la fila sigueinte
        self.cont = self.cont + 1

    # Función para cerrar que manda a llamar al exportador 
    # Creado para una mejor sintaxis
    # TODO igual y esta de más
    def closeFile(self):
        self.saveFile()