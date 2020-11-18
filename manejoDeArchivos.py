def validarRuta (ruta_del_archivo):
    return ruta_del_archivo.replace("\"","/")

def crearArchivo (ruta_del_archivo):
    open(ruta_del_archivo,"x")


def asignarArchivo (ruta_del_archivo,modo):
    try:
        return open(ruta_del_archivo,modo)
    except FileNotFoundError:
        crearArchivo (ruta_del_archivo)
        asignarArchivoDeTexto (ruta_del_archivo)

def leerArchivoDeTexto (ruta_del_archivo):
    archivo = asignarArchivo(ruta_del_archivo,"rt")
    return(archivo.read())
    cerrarArchivo(archivo)

def leerArchivoDeDatos (ruta_del_archivo):
    archivo = asignarArchivo(ruta_del_archivo,"rb")
    return(archivo.read())
    cerrarArchivo(archivo)


def escribirArchivoDeTexto (ruta_del_archivo,texto):
    archivo = asignarArchivo(ruta_del_archivo, "w")
    archivo.write(texto)
    cerrarArchivo(archivo)


def cerrarArchivo(archivo):
    archivo.close()