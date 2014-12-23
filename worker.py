class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker('bob', 5000)
sue = Worker('Sue smith', 6000)

sue.lastName()
sue.giveRaise(.10)
sue.pay
