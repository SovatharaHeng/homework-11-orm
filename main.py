from Model import Assignment, Employee
from db import session, engine
from sqlalchemy import text


'''
Query all employee records from the employee table
And query employee with condition, emp_num > 101
'''
# employees = session.query(Employee).all()
# for employee in employees:
#     print(employee.emp_fname, employee.emp_lname, employee.emp_initial)
    
# employees = session.query(Employee).filter(Employee.emp_num > 101).all()
# for employee in employees:
#     print(employee.emp_lname, employee.emp_fname, employee.emp_hiredate)

'''
Join employee with job
'''
# employees = session.query(Employee, Job).filter(Employee.job_code == Job.job_code).all()
# for employee in employees:
#     print(employee.Employee.emp_lname, employee.Employee.emp_fname, employee.Job.job_description)

'''
Insert new employee record
'''
# employee = Employee(emp_num=999, emp_lname="Doe", emp_fname="John", emp_initial="D", emp_hiredate="2020-01-01")
# session.add(employee)
# session.commit()

'''
Update employee record

'''
# employee = session.query(Employee).filter(Employee.emp_num == 999).first()
# employee.job_code = 510
# session.commit()

'''
Delete employee record
'''
# employee = session.query(Employee).filter(Employee.emp_num == 999).first()
# session.delete(employee)
# session.commit()

'''
Query assigment where assign_date is larger than 2010-01-01
'''
# assignments = session.query(Assignment).filter(Assignment.assign_date > "2010-01-01").all()
# for assignment in assignments:
#     print(assignment.assign_num, assignment.assign_date, assignment.assign_job)

connection = engine.connect()
query = "Select * FROM employee WHERE emp_num > :value"
sql_expression = text(query)
param = {'value': 101}
result = connection.execute(sql_expression, param)

for row in result:
    print(row[0])

connection.close()

