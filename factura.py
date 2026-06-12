import xml.etree.ElementTree as ET


class Factura:
    def __init__(self, archivo_xml="Prueba.xml"):
        self.tree = ET.parse(archivo_xml)
        self.root = self.tree.getroot()
        self.nombre = None
        self.numero = None
        self.correo = None
        self.telefono = None
        self.provincia = None
        self.canton = None
        self.distrito = None
        self.otras_senas = None
        self.detalle_servicio = []

    def obtener_encabezado(self):
        receptor = self.root.find(".//{*}Receptor") #.// sirve para buscar todo en específicamente ese elemento

        if receptor is None:
            return

        self.nombre = receptor.findtext(".//{*}Nombre")
        self.numero = receptor.findtext(".//{*}Numero")
        self.correo = receptor.findtext(".//{*}CorreoElectronico")
        self.telefono = receptor.findtext(".//{*}NumTelefono")
        self.provincia = receptor.findtext(".//{*}Provincia")
        self.canton = receptor.findtext(".//{*}Canton")
        self.distrito = receptor.findtext(".//{*}Distrito")
        self.otras_senas = receptor.findtext(".//{*}OtrasSenas")

    def obtener_detalle_servicio(self):
        self.detalle_servicio = []

        for prod in self.root.findall(".//{*}LineaDetalle"):


            linea = type("LineaDetalle", (), {})()

            linea.codigo = prod.findtext(".//{*}Codigo")
            linea.cantidad = prod.findtext(".//{*}Cantidad")
            linea.unidad_medida = prod.findtext(".//{*}UnidadMedida")
            linea.detalle = prod.findtext(".//{*}Detalle")
            linea.precio_unitario = prod.findtext(".//{*}PrecioUnitario")
            linea.monto_total = prod.findtext(".//{*}MontoTotal")

            self.detalle_servicio.append(linea)

    def mostrar_informacion(self):

        self.obtener_encabezado()
        self.obtener_detalle_servicio()


        print("----- ENCABEZADO -----")
        print("Nombre:", self.nombre)
        print("Numero:", self.numero)
        print("Correo:", self.correo)
        print("Telefono:", self.telefono)
        print("Provincia:", self.provincia)
        print("Canton:", self.canton)
        print("Distrito:", self.distrito)
        print("Otras Señas:", self.otras_senas)

        print("\n----- DETALLE -----")
        for linea in self.detalle_servicio:
            print("Codigo:", linea.codigo)
            print("Cantidad:", linea.cantidad)
            print("Unidad:", linea.unidad_medida)
            print("Detalle:", linea.detalle)
            print("Precio:", linea.precio_unitario)
            print("Total:", linea.monto_total)
            print("-------------------")

if __name__ == "__main__":
    factura = Factura()
    factura.mostrar_informacion()
    