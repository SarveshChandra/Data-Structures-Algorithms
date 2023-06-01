# ATM

**Requirements**

1. Card reader: to read the users’ ATM cards.
2. Keypad: to enter information into the ATM e.g. PIN. cards.
3. Screen: to display messages to the users.
4. Cash dispenser: for dispensing cash.
5. Deposit slot: For users to deposit cash or checks.
6. Printer: for printing receipts.
7. Communication/Network Infrastructure: it is assumed that the
ATM has a communication infrastructure to communicate with the
bank upon any transaction or activity.

Given the requirements, here's an outline of the classes and their responsibilities.

1. `ATM`: This is the main class that represents the ATM machine. It contains instances of the `CardReader`, `Keypad`, `Screen`, `CashDispenser`, `DepositSlot`, and `Printer` classes. It also maintains the current `Account` in context and handles the high level operations and user flow.

2. `CardReader`: This class is responsible for interacting with the user's ATM card. It can read the account number from the card.

3. `Keypad`: This class allows the user to input information such as PIN, amount to withdraw, deposit, etc.

4. `Screen`: This class displays information to the user, such as their account balance, menu options, and prompts for user input.

5. `CashDispenser`: This class controls the cash dispenser component of the ATM, which dispenses cash to the user during a withdrawal. It must track the amount of cash it has available to dispense.

6. `DepositSlot`: This class represents the deposit slot for accepting deposits from the user. It can accept cash or checks.

7. `Printer`: This class is responsible for printing receipts that detail the transaction.

8. `NetworkInterface`: This class allows the ATM to communicate with the bank to verify the user's PIN, check account balances, handle deposits and withdrawals, etc. 

9. `Bank`: This class handles the bank's side of the operations, including managing accounts and verifying transactions.

10. `Account`: This class represents a user's bank account. It stores details such as the account number, the account balance, and the account holder's name.

Here is the skeleton code for these classes:

```python
class ATM:
    def __init__(self):
        self.cardReader = CardReader()
        self.keypad = Keypad()
        self.screen = Screen()
        self.cashDispenser = CashDispenser()
        self.depositSlot = DepositSlot()
        self.printer = Printer()
        self.networkInterface = NetworkInterface()

    def insertCard(self):
        pass

    def enterPin(self):
        pass

    def selectTransaction(self):
        pass

    def performTransaction(self):
        pass

    def ejectCard(self):
        pass

class CardReader:
    def readCard(self):
        pass

class Keypad:
    def getInput(self):
        pass

class Screen:
    def displayMessage(self, message):
        pass

class CashDispenser:
    def dispenseCash(self, amount):
        pass

    def hasSufficientCash(self, amount):
        pass

class DepositSlot:
    def acceptDeposit(self):
        pass

class Printer:
    def printReceipt(self, transaction):
        pass

class NetworkInterface:
    def authenticateUser(self, accountNumber, pin):
        pass

    def getAccountDetails(self, accountNumber):
        pass

    def updateAccountBalance(self, accountNumber, amount):
        pass

class Bank:
    def __init__(self):
        self.accounts = []

    def addAccount(self, account):
        pass

    def getAccount(self, accountNumber):
        pass

class Account:
    def __init__(self, accountNumber, pin, initialBalance):
        self.accountNumber = accountNumber
        self.pin = pin
        self.balance = initialBalance

    def debit(self, amount):
        pass

    def credit(self, amount):
        pass
```

In the provided python code, every class has been defined with a constructor and its operations (methods). The details of these operations, however, are omitted with a `pass` statement.