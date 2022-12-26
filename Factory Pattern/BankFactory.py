from IBankFactory import IBankFactory
from IBank import IBank
from BankA import BankA
from BankB import BankB

class BankFactory(IBankFactory):
    def GetBank(self, bankCode: str) -> IBank:
        if (bankCode == '123456'):
            return BankA()
        elif (bankCode == '111111'):
            return BankB()
        else:
            return None