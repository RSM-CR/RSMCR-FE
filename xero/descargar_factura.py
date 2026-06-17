# Este es un módulo temporal para tener el código para descargar facturas
# La idea es mover este código a otro lado para formar una implementación
# completa de la clase Fuente
from xero.auth import obtener_cliente
from httpx import Client

def descargar_factura(id_factura: str):
    xero = obtener_cliente()
    factura = xero.request("GET", f"https://api.xero.com/api.xro/2.0/Invoices/{id_factura}")
    return factura.json()

if __name__ == "__main__":
    id_factura = input("Introduce el ID de la factura\n> ")
    print(descargar_factura(id_factura))