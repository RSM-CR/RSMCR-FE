import xml.etree.ElementTree as ET

class Factura:
    def __init__(self):
        self.nombre = None
        self.numero = None
        self.correo = None
        self.telefono = None
        self.provincia = None
        self.canton = None
        self.distrito = None
        self.otras_senas = None
        self.codgigo = None
        self.cantidad = None
        self.unidad_medida = None
        self.detalle = None
        self.precio_unitario = None
        self.monto_total = None
        #falta el impuesto
        self.cosas = []

class datos:
    @staticmethod
    def obtener_datos(archivo_xml = "Prueba.xml")-> Factura:
        factura = Factura()
        tree = ET.parse(archivo_xml)
        root = tree.getroot()

        info = []
        receptor = root.find(".//{*}Receptor") #.// sirve para buscar todo en específicamente ese elemento
        if receptor is not None:
            factura.nombre = receptor.findtext(".//{*}Nombre")
            factura.numero = receptor.findtext(".//{*}Numero")
            factura.correo = receptor.findtext(".//{*}CorreoElectronico")
            factura.telefono = receptor.findtext(".//{*}NumTelefono")
            factura.provincia = receptor.findtext(".//{*}Provincia")
            factura.canton = receptor.findtext(".//{*}Canton")
            factura.distrito = receptor.findtext(".//{*}Distrito")
            factura.otras_senas = receptor.findtext(".//{*}OtrasSenas")

        for linea in root.findall(".//{*}LineaDetalle"):
            info.append({
                "nombre": factura.nombre,
                "numero": factura.numero,
                "correo": factura.correo,
                "telefono": factura.telefono,
                "provincia": factura.provincia,
                "canton": factura.canton,
                "distrito": factura.distrito,
                "otras_senas": factura.otras_senas,
                "codigo": linea.findtext(".//{*}Codigo"),
                "cantidad": linea.findtext(".//{*}Cantidad"),
                "unidad_medida": linea.findtext(".//{*}UnidadMedida"),
                "detalle": linea.findtext(".//{*}Detalle"),
                "precio_unitario": linea.findtext(".//{*}PrecioUnitario"),
                "monto_total": linea.findtext(".//{*}MontoTotal")
                #falta el impuesto
            })
        factura.cosas = info
        return factura