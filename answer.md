(1)
today = datetime.now()
employee = Employee(emp_num = 168, emp_fname = "John", emp_lname = "Doe", emp_initial = "JD", job_code = 500, emp_hiredate = today)
session.add(employee)
session.commit()

(2)
employees = session.query(Employee, Job).filter(Employee.job_code == Job.job_code).filter(Employee.emp_num == 168).all()

for employee in employees:
    print(employee.Employee.emp_num, employee.Employee.emp_fname, employee.Employee.emp_lname, employee.Employee.emp_initial, employee.Job.job_description, employee.Job.job_chg_hour, employee.Employee.emp_hiredate)

(3)
employee = session.query(Employee).filter(Employee.emp_num == 168).first()
employee.job_code = 502
session.commit()

(4)
projects = session.query(Project, Employee).filter(Project.emp_num == Employee.emp_num).filter(Employee.job_code == 500).all()

for project in projects:
    print(project.Project.proj_num, project.Project.proj_name, project.Employee.emp_fname, project.Employee.emp_lname)

(5)
employee = session.query(Employee).filter(Employee.emp_num == 168).first()
session.delete(employee)
session.commit()
