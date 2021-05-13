class customerAmt:
    def __init__(self, custName, amt):
        self.custName = custName
        self.amt = amt
    def update(self):
        if self.amt < 0:
            print (f"The customer {self.custName} does not owe any money")
        elif self.amt > 0:
            print (f"The customer {self.custName} owe {self.amt}, please send email to customer {self.custName}")
class Accounting_System:
    def __init__(self):
        self.customers = set()

    def register(self, customerName):
        self.customers.add(customerName)
#        print (self.customers)

    def unregister(self, customerName):
        self.customers.remove(customerName)
    def notify(self):
        for i in self.customers:
            i.update()

def main():
    Krishan = customerAmt("krishan", 10)
    Renu = customerAmt("Renu", 20)
    Bhavya = customerAmt("Bhavya", -10)
    Jeenu = customerAmt("Jeenu", -10)
    test = customerAmt("test", 10)

    accountingSystem = Accounting_System()
    accountingSystem.register(Krishan)
    accountingSystem.register(Renu)
    accountingSystem.register(Bhavya)
    accountingSystem.register(Jeenu)
    accountingSystem.register(test)
    accountingSystem.notify()
    print (f"The customer Test has closed his account")
    print("+++++++++++++++++++++++++++++++Reprinting ++++++++++++++++++++++++++++++++++++")
    accountingSystem.unregister(test)
    accountingSystem.notify()



if __name__ == "__main__":
    main()


