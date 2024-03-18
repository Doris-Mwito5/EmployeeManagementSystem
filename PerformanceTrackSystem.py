
class Peformance:
    def track(self,employees,hours):
        print("Employees Performance")
        print("=====================")
        
        for employee in employees:
            status = employee.work(hours)
            print(f"{employee.name} : {status}")
            print("===========================")
        
class ManagerRole:
    def track(self,hours):
        return f"The manager is handling the team for {hours} hours"
    
class DeveloperRole:
    def track(self,hours):
        return f"The developer has been working for {hours} hours"
    
class SalesRole:
    def track(self,hours):
        return f"The salesperson will be working for {hours} hours"
    
class WorkerRole:
    def track(self,hours):
        return f"All casual workers are supposed to work for {hours} hours"
    
               
