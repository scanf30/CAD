#! /usr/bin/python3
import openpyxl
import datetime


class fileMAngage(openpyxl.Workbook):
    def __init__(self):
        super(fileMAngage, self).__init__()
        self.initFile()

    def initFile(self):
        self.workspace = self.active
        self.workspace.title = 'demo'
        self.cont = 1

    def saveFile(self):
        self.save(filename =  str(datetime.date.today()) + '.xlsx')

    def addCount(self, peso):
        now = datetime.datetime.now()
        self.workspace['A'+str(self.cont)] = now.strftime("%H:%M:%S")
        self.workspace['B'+str(self.cont)] = peso
        self.cont = self.cont + 1

    def closeFile(self):
        self.saveFile()