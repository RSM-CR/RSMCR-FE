from gti.gti import gti
import asyncio

class main():
    async def exec(self):
        with open("gti\\Prueba.xml", "r") as f:
            xml_facture = f.read()
        return {
            await gti().subir_factura(xml_facture)
            }

if __name__ == "__main__":
    asyncio.run(main().exec())