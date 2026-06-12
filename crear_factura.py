from factura import Factura

def crear_factura_GTI(archivo_xml="Prueba.xml") -> Factura:
    factura = Factura()

    receptor = factura.root.find(".//{*}Receptor") #.// sirve para buscar todo en específicamente ese elemento

    if receptor is None:
        return

    factura.nombre = receptor.findtext(".//{*}Nombre")
    factura.numero = receptor.findtext(".//{*}Numero")
    factura.correo = receptor.findtext(".//{*}CorreoElectronico")
    factura.telefono = receptor.findtext(".//{*}NumTelefono")
    factura.provincia = receptor.findtext(".//{*}Provincia")
    factura.canton = receptor.findtext(".//{*}Canton")
    factura.distrito = receptor.findtext(".//{*}Distrito")
    factura.otras_senas = receptor.findtext(".//{*}OtrasSenas")

    return factura

def crear_factura_Xero():
    # Aqui va todo lo que se ocupa para crear la factura de Xero
    pass