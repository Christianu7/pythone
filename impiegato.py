class Employee :
    def __init__(self, nome, cognome, salario) :
        self._nome= nome
        self._cognome= cognome
        self._salario= salario
    def __repr__(self):
        return f"Employee: {self._nome} {self._cognome}, Salario: {self._salario}"
class Manager (Employee) :
    def __init__(self, nome, cognome, salario, reparto) :
        super().__init__(nome, cognome, salario)
        self._reparto= reparto
    def __repr__(self):
        return f"Employee:  {self._nome} {self._cognome}, Salario: {self._salario}, Reparto: {self._reparto}"
    
employee = Employee("Lorenzo", "Scavolini", 1400)
manager = Manager("Christian","Paperi", 2500, "contabilita")

print(employee)
print(manager)
