from gti_implementation.gti import gti
import asyncio

class main():
    async def exec(self):
        return await gti().upload_facture()

if __name__ == "__main__":
    asyncio.run(main().exec())