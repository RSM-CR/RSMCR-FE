from abc import ABC, abstractmethod

class destination (ABC):
	def __init__(self):
		pass
	
	@abstractmethod
	async def upload_facture():
		pass