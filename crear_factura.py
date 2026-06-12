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

    for prod in factura.root.findall(".//{*}LineaDetalle"):

        linea = type("LineaDetalle", (), {})()

        linea.codigo = prod.findtext(".//{*}Codigo")
        linea.cantidad = prod.findtext(".//{*}Cantidad")
        linea.unidad_medida = prod.findtext(".//{*}UnidadMedida")
        linea.detalle = prod.findtext(".//{*}Detalle")
        linea.precio_unitario = prod.findtext(".//{*}PrecioUnitario")
        linea.monto_total = prod.findtext(".//{*}MontoTotal")
        #falta el impuesto

        factura.cosas.append(linea)

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
        for linea in factura.cosas:
            print("Codigo:", linea.codigo)
            print("Cantidad:", linea.cantidad)
            print("Unidad:", linea.unidad_medida)
            print("Detalle:", linea.detalle)
            print("Precio:", linea.precio_unitario)
            print("Total:", linea.monto_total)
            print("-------------------")

    return factura
    
    
def crear_factura_Xero(archivo_xml="pruebachat.xml") -> Factura:
    factura1 = Factura()
    
    cliente = factura1.root.find(".//{*}Contact")
    if cliente is None:
        return
    factura1.nombre = cliente.findtext(".//{*}Name")
    factura1.correo = cliente.findtext(".//{*}EmailAddress")
    factura1.estado = cliente.findtext(".//{*}Status")
    factura1.moneda = cliente.findtext(".//{*}CurrencyCode")
    for prod in factura1.root.findall(".//{*}LineItem"):
        library = type("LineaItem", (), {})()
        library.descripcion = prod.findtext(".//{*}Description")
        library.cantidad = prod.findtext(".//{*}Quantity")
        library.precio_unitario = prod.findtext(".//{*}UnitAmount")
        library.codecuenta = prod.findtext(".//{*}AccountCode")
        library.monto_total = prod.findtext(".//{*}LineAmount")
        factura1.cosas.append(library)
        print("----- ENCABEZADO -----")
        print("Nombre:", factura1.nombre)
        print("Correo:", factura1.correo)
        print("Estado:", factura1.estado)
        print("Moneda:", factura1.moneda)
        print("\n----- DETALLE -----")
        for linea in factura1.cosas:
            print("Descripcion:", linea.descripcion)
            print("Cantidad:", linea.cantidad)
            print("Precio Unitario:", linea.precio_unitario)
            print("Codigo Cuenta:", linea.codecuenta)
            print("Monto Total:", linea.monto_total)
            print("-------------------")

    return factura1