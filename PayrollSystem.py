import datetime
import calendar

class PayrollManagement():
    
    def calculate_payroll(self,employees):
        
        print("Payroll Management System")
        print("=========================")
        
        for employee in employees:
            print("Employee Name : {}\nEmployee ID : {}".format(self.name, self.id))
            print("Amount : {}".format(employee.calculate_payroll()))
            print("================================================")
            
class SalaryPolicy:
    def __init__(self,rate_per_day):
        self.rate_per_day = rate_per_day
        
    def calculate_payroll(self):
        today = datetime.datetime.now()
        Total_days = calendar.monthrange(today.year,today.month)[1]
        
        return Total_days * self.rate_per_day
        
class ParttimePolicy:
    def __init__(self,rate_per_hour,total_hours):
        self.rate_per_hour = rate_per_hour
        self.total_hours = total_hours
        
    def calculate_payroll(self):
        return self.rate_per_hour * self.total_hours
    
class CommissionPolicy(SalaryPolicy):
    def __init__(self,rate_per_day,commission):
        super().__init__(rate_per_day)
        self.commission = commission
        
    def calculate_payroll(self):
        salary = super().calculate_payroll()
        return salary + self.commission
        