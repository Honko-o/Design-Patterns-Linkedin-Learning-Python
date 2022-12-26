from IBank import IBank
from BankFactory import BankFactory

bankFactory: BankFactory = BankFactory()

cardNumber = input('Enter Your Card Number:')
bankCode = cardNumber[0:6]

bank: IBank = bankFactory.GetBank(bankCode)

print(bank.Withdraw())