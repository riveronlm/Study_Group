

class Computer():
    ssd = 50
    ram = 32

    def _init_(self, ssd, ram):
        self.ssd = ssd
        self.ram = ram

    def divBy_2(self):
        return(self.ram/2)

    def displaySSD(self):
        return(self.ssd % 2)


Mymac = Computer()


print(Mymac.displaySSD())
print(Mymac.divBy_2())
