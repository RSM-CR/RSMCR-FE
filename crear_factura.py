from factura import Factura
from factura import FacturaXero
import xml.etree.ElementTree as ET

def crear_factura_GTI(archivo_xml="Prueba.xml") -> Factura:
    factura = FacturaGTI()

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

    for prod in factura.root.findall(".//{*}LineaDetalle"):

        linea = type("LineaDetalle", (), {})()

        linea.codigo = prod.findtext(".//{*}Codigo")
        linea.cantidad = prod.findtext(".//{*}Cantidad")
        linea.unidad_medida = prod.findtext(".//{*}UnidadMedida")
        linea.detalle = prod.findtext(".//{*}Detalle")
        linea.precio_unitario = prod.findtext(".//{*}PrecioUnitario")
        linea.monto_total = prod.findtext(".//{*}MontoTotal")
        #falta el impuesto

        factura.detalle_servicio.append(linea)

        print("----- ENCABEZADO -----")
        print("Nombre:", factura.nombre)
        print("Numero:", factura.numero)
        print("Correo:", factura.correo)
        print("Telefono:", factura.telefono)
        print("Provincia:", factura.provincia)
        print("Canton:", factura.canton)
        print("Distrito:", factura.distrito)
        print("Otras Señas:", factura.otras_senas)

        print("\n----- DETALLE -----")
        for linea in factura.root.findall(".//{*}LineaDetalle"):
            print("Codigo:", linea.codigo)
            print("Cantidad:", linea.cantidad)
            print("Unidad:", linea.unidad_medida)
            print("Detalle:", linea.detalle)
            print("Precio:", linea.precio_unitario)
            print("Total:", linea.monto_total)
            print("-------------------")

    return factura
    
    
def crear_factura_Xero(archivo_xml="pruebachat.xml") -> Factura:
    factura = Factura()

    receptor = factura.root.find(".//{*}Contact") #.// sirve para buscar todo en específicamente ese elemento
    if receptor is None:
        return
    
    pass