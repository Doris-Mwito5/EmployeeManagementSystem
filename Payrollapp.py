import PayrollSystem
import Employee
import PerformanceTrackSystem


Manager = Employee.Manager("Eastus",2098634,1000)
Developer = Employee.Developer("Doris",2569014,1200)
Salesman = Employee.SalesPerson("Kamau",2791652,500,10)
Cook = Employee.Cook("Sally",3025678,450,4)
Consultant = Employee.Consultant("James",3256782,600,10)
employees = [Manager,Developer,Salesman,Cook,Consultant]

system = PerformanceTrackSystem.Peformance()
system.track(employees,40)
payrollsystem = PayrollSystem.PayrollManagement()
payrollsystem.calculate_payroll(employees)
