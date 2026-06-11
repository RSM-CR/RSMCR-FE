from abc import ABC, abstractmethod
from fastapi import Request

class destination (ABC):
	def __init__(self):
		pass
	
	@abstractmethod
	async def get_document(req: Request):
		pass

	@abstractmethod
	async def upload_facture(body: get_document):
		pass