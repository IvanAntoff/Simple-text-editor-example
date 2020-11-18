# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:27:56 2020

@author: Antoff Ivan
"""
from PyQt5.QtWidgets import QFileDialog
from interfazQT_ui import *
from manejoDeArchivos import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #self.pushButton.setText("Presióname")
        # Conectamos los eventos con sus acciones
        self.botonLeer.clicked.connect(self.leer)
        self.botonEscribir.clicked.connect(self.actualizar)
        self.botonRestablecer.clicked.connect(self.restablecer)
    

    def leer(self):
        nombreArchivo, ext = validarExt(self.textoRutaDelArchivo.text())
        ext = ext.lower()
        if ext == ".json":
            self.textoArchivo.setPlainText(leerArchivoJson(self.textoRutaDelArchivo.text()))
            self.textoArchivoModificable.setPlainText(leerArchivoJson(self.textoRutaDelArchivo.text()))
        elif (ext == ".dat"):
            self.textoArchivo.setPlainText(leerArchivoDeDatos(self.textoRutaDelArchivo.text()))
            self.textoArchivoModificable.setPlainText(leerArchivoDeDatos(self.textoRutaDelArchivo.text()))
        else:
            self.textoArchivo.setPlainText(leerArchivoDeTexto(self.textoRutaDelArchivo.text()))
            self.textoArchivoModificable.setPlainText(leerArchivoDeTexto(self.textoRutaDelArchivo.text()))
        

    def actualizar(self):
        escribirArchivoDeTexto(self.textoRutaDelArchivo.text(),self.textoArchivoModificable.toPlainText())
        self.textoArchivo.setPlainText(leerArchivoDeTexto(self.textoRutaDelArchivo.text()))


    def restablecer(self):
        self.textoArchivoModificable.setPlainText(self.textoArchivo.toPlainText())


    def searchFolderClicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if fileName:
            self.textoRutaDelArchivo.setText(fileName)
            
    
    
if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
    