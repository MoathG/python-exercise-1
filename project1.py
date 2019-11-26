# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:20:41 2019

@author: Moath
"""

class Person:
    def __init__(self, name, address):
        self._name = name
        self._address = address
        
        
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name

    def getAddress(self):
        return self._address
    
    def setAddress(self, address):
        self._address = address
        
    def __del__(self):
        print(self._name + ' have been deleted')

            
        
p1 = Person('rashed', 'amman')

class Employee(Person):
# =============================================================================
#     employee_number = 0
#     __salary = 0.0
#     __job_title = ''
#     __loans = []
# =============================================================================
    
    def __init__(self, employee_number, name, address, salary, job_title, loans):
        self.employee_number = employee_number
        Person.__init__(self, name, address)
        self.__salary = salary
        self.__job_title = job_title
        self.__loans = loans
        
    def getSalary(self):
        return self.__salary
    
    def setSalary(self, salary):
        self.__salary = salary
        
    def getJobTitle(self):
        return self.__job_title
    
    def setJobTitle(self, job_title):
        self.__job_title = job_title
        
    def getTotalLoans(self):
        s = 0
        for n in self.__loans:
            s = s + n
        return s
    
    def getMaxLon(self):
        #import functools
        #Max = functools.reduce(lambda a,b : a if a > b else b, self.__loans)
        return max(self.__loans)
    
    def getMinLon(self):
        if len(self.__loans) < 1 : 
            return None
        return min(self.__loans)
    
    def setLoans(self, add):
        self.__loans.append(add)
        
    def getLoans(self):
        return self.__loans
        
    def print_info(self):
        print(f'''
Employee Number: {self.employee_number}
Salary : {self.__salary}
Job Title: {self.__job_title}
Loans: {self.__loans}
Total Loans: {self.getTotalLoans()}
        ''')
        
    def __del__(self):
        print(self._name + ' have been deleted')
    
# =============================================================================
# p2 = Employee(1, 200.3, 'engineer', [30, 60, 90])
# 
# print(p2.getTotalLoans())
# print(p2.getMaxLon())
# print(p2.getMinLon())
# p2.setLoans(75)
# print(p2.getTotalLoans())
# p2.print_info()
# =============================================================================
    
        
class Student(Person):
# =============================================================================
#     student_number = 0
#     subject = ''
#     marks = {}
# =============================================================================

    def __init__(self, student_number, name, address, subject, marks):
        Person.__init__(self, name, address)
        self.student_number = student_number
        self.__subject = subject
        self.__marks = marks
        
    def getSubject(self):
        return self.__subject
    
    def setSubject(self, subject):
        self.__subject = subject

    def getMarks(self):
        return self.__marks
    
    def setMarks(self, key, value):
        self.__marks[key] = value
        
    def getAverage(self):
        sum1 = 0
        c = 0
        for k,v in self.__marks.items():
            sum1 = sum1 + v
            c = c + 1
        return sum1/c
    
    def print_info(self):
        print(f'''
Student Number: {self.student_number}
Student subject: {self.__subject}
Student Marks: {self.__marks}
Student Average: {self.getAverage()}
        ''')
        
# =============================================================================
#     def __del__(self):
#         print(" I have been Delete!")
# =============================================================================
        
# =============================================================================
# p3 = Student(1, 'math', {'math': 85, 'science': 90, 'English': 87})
# print(p3.getMarks())
# p3.setMarks('Arabic', 79)
# print(p3.getMarks())
# print(p3.getAverage())
# p3.print_info()
# =============================================================================


"""1"""
EmployeesList=[]
Employee1= Employee(1000,"Ahmed Yazan","Amman, jordan",500,"HR Consultant",[434,200,1020])
EmployeesList.append(Employee1)
Employee2= Employee(2000,"Hala Rana","Aqaba, jordan",750,"Department Manager",[150,3000,250])
EmployeesList.append(Employee2)
Employee3= Employee(3000,"Mariam Ali","Mafraq, jordan",600,"HR s Consultant",[304,1000,250,300,500,235])
EmployeesList.append(Employee3)
Employee4= Employee(4000,"Yasmin Mohamed","Karak, jordan",865,"Director",[])
EmployeesList.append(Employee4)
"""2"""
StudentsList=[]
Student1= Student(20191000,"Khalid ali","Irbid, jordan","History",{"English":80,"Arabic":90,"Art":95,"managment":75})
StudentsList.append(Student1)
Student2= Student(20182000,"Reem Hani","Zaraqa, jordan","Softwere Eng",{"English":80,"Arabic":90,"managment":75,"Calculus":85,"OS":73,"Programming":90})
StudentsList.append(Student2)
Student3= Student(20161001,"Nawras Abdallah","Amman, jordan","Art",{"English":83,"Arabic":92,"Art":90,"managment":70})
StudentsList.append(Student3)
Student4= Student(20172030,"Reem Hani","Zaraqa, jordan","Softwere Eng",{"English":83,"Arabic":92,"managment":70,"Calculus":80,"OS":79,"Programming":91})
StudentsList.append(Student4)
Student5= Student(20172030,"Reem Hani","Zaraqa, jordan","Softwere Eng",{"English":83,"Arabic":92,"managment":70,"Calculus":80,"OS":79,"Programming":91})

for x in StudentsList:
    x.print_info()
    
for y in EmployeesList:
    y.print_info()
    
print('we have', len(EmployeesList), 'employees')
print('We have', len(StudentsList), 'students')


the_average = list(map(lambda x: x.getAverage(), StudentsList))
print(max(the_average))

#8
employee_loans = list(filter(lambda x: x.getMinLon(), EmployeesList))
min_employee_loan = min(list(map(lambda x: x.getMinLon(), employee_loans)))
print('Employees Min loans is: ' + str(min_employee_loan))

#9
max_employee_loans = max(list(map(lambda x: x.getMaxLon(), employee_loans)))
print('Employees Max loans is: ' + str(max_employee_loans))

#10
employees_loans = list(map(lambda x: x.getLoans(), employee_loans))
employees_total_loans = list(map(lambda x: x.getTotalLoans(), employee_loans))
print(f'''
Employees Loans: {employees_loans}
Employees Total Loans: {employees_total_loans}      
''')

# =========================================================

# 11
LoanDictionary = list(map(lambda e: {e.employee_number: e.getLoans()}, employee_has_loans))
# print(LoanDictionary)
for item in LoanDictionary:
    print(item)


# 12
def get_max_loan(employee_loans):
    max_loan = reduce(lambda a, b: a if a > b else b, employee_loans)
    return max_loan


def get_min_loan(employee_loans):
    min_loan = reduce(lambda a, b: a if a < b else b, employee_loans)
    return min_loan


for employee in employee_has_loans:
    print(
        f'Employee Name: {employee._name} Min Loan: {get_min_loan(employee.getLoans())} Max Loan: {get_max_loan(employee.getLoans())}')

# 13
students_got_a = list(filter(lambda s: s.getAllMarks(), StudentsList))
for student in students_got_a:
    print(f'''
Name: {student.getName()}
Subject: {student.getSubject()}
Marks: {student.getMarks()}
''')

# 14
employee_salaries = list(map(lambda e: e.getSalary(), EmployeesList))
max_employee_salary = max(employee_salaries)
print('Maximum Employee Salary', max_employee_salary)

# 15
min_employee_salary = min(employee_salaries)
print('Minimum Employee Salary', min_employee_salary)
# 16

total_salaries = reduce(lambda a, b: a + b, employee_salaries)
print('Total Employees Salaries ', total_salaries)


# 17
def delete_object(lst_object):
    for item in lst_object:
        del item


delete_object(EmployeesList)
delete_object(StudentsList)







