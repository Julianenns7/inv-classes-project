class Laboratory:

    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost

    def formatLabInfo(self):
        return f"{self.lab_name}_{self.cost}"

    def addLabToFile(self):
        f = open('laboratories.txt', 'a')
        f.write(self.formatLabInfo())
        f.close()

    def enterLaboratoryInfo(self):
        lab_name = input("Enter Laboratory facility:")
        cost = input("Enter Laboratory cost:")
        Laboratory(lab_name, cost)

    def readLaboratoriesFile(self):
        f = open('laboratories.txt', 'r')
        f.read()
        f.close()

lab10 = Laboratory("lab10", 1200)


lab10.addLabToFile()

lab10.readLaboratoriesFile()

class Management:
    def displayMenu(self):
        num = 1
        while num != 0:
            print("Welcome to Alberta Hospital (AH) Managment system")
            num = input("Select from the following options, or select 0 to stop:")
            if num == 0:
                break
            