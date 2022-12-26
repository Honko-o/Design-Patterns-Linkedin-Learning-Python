from abc import ABC
from IBank import IBank

class IBankFactory(ABC):
    def GetBank(self, bankCode: str) -> IBank:
        pass