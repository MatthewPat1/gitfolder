class employee:

    def __init__(self, name, id, start, status):
        self.name = name
        self.id = id
        self.start = start
        self.status = status

    def getName(self):
        return self.name
    def getId(self):
        return self.id
    def getStart(self):
        return self.start
    def getStatus(self):
        return self.status

class employeeController:
    
    
    def __init__(self, unitName):
            self.unitname = unitName
            self.employeeList = [] 

    def addEmployee(self, employee):
       self.employeeList.append((employee.getName(), employee.getId()))
        
    def pel(self):
        print(self.employeeList)

        
empctl = employeeController('sales')
matt = employee('matthew',32,'5/31/2022', 'employed')

empctl.addEmployee(matt)
empctl.addEmployee(matt)
empctl.addEmployee(matt)
empctl.pel()
