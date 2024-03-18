from PayrollSystem import(SalaryPolicy,ParttimePolicy,CommissionPolicy)
from PerformanceTrackSystem import(ManagerRole,DeveloperRole,SalesRole,WorkerRole)

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
#code based on different roles
class Manager(Employee,ManagerRole,SalaryPolicy):
    def __init__(self, name, id,rate_per_day):
        SalaryPolicy.__init__(self,rate_per_day)
        super().__init__(name, id)
        
class Developer(Employee,DeveloperRole,SalaryPolicy):
    def __init__(self, name, id,rate_per_day):
        SalaryPolicy.__init__(self,rate_per_day)
        super().__init__(name, id)
 
class SalesPerson(Employee,SalesRole,CommissionPolicy):
    def __init__(self, name, id,rate_per_day,commission):
        CommissionPolicy.__init__(self,rate_per_day,commission)
        super().__init__(name, id)                        

class Cook(Employee,WorkerRole,ParttimePolicy):
    def __init__(self, name, id,rate_per_hour,total_hours):
        ParttimePolicy.__init__(self,rate_per_hour,total_hours)
        super().__init__(name, id)
      
class Consultant(Employee,DeveloperRole,ParttimePolicy):
    def __init__(self, name, id,rate_per_hour,total_hours):
        ParttimePolicy.__init__(self,rate_per_hour,total_hours)
        super().__init__(name, id)
    