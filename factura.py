import xml.etree.ElementTree as ET

class Factura:
    def __init__(self):
        self.nombre: str | None = None
        self.numero: str | None = None
        self.correo: str | None = None
        self.telefono: str | None = None
        self.provincia: str | None = None
        self.canton: str | None = None
        self.distrito: str | None = None
        self.otras_senas: str | None = None
        self.codigo: str | None = None
        self.cantidad: str | None = None
        self.unidad_medida: str | None = None
        self.detalle: str | None = None
        self.precio_unitario: str | None = None
        self.monto_total: str | None = None
        #falta el impuesto
        self.cosas = list[LineasDetalle]()

class LineasDetalle:
    def __init__(self):
        self.codigo: str | None = None
        self.cantidad: str | None = None
        self.unidad_medida: str | None = None
        self.detalle: str | None = None
        self.precio_unitario: str | None = None
        self.monto_total: str | None = None
        #falta el impuesto

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


        for linea_xml in root.findall(".//{*}LineaDetalle"):
            linea_obj = LineasDetalle()
            linea_obj.codigo = linea_xml.findtext(".//{*}Codigo")
            linea_obj.cantidad = linea_xml.findtext(".//{*}Cantidad")
            linea_obj.unidad_medida = linea_xml.findtext(".//{*}UnidadMedida")
            linea_obj.detalle = linea_xml.findtext(".//{*}Detalle")
            linea_obj.precio_unitario = linea_xml.findtext(".//{*}PrecioUnitario")
            linea_obj.monto_total = linea_xml.findtext(".//{*}MontoTotal")

            factura.cosas.append(linea_obj)
        return factura
