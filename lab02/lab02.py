import mysql.connector
from mysql.connector import errorcode



class Employee:
    employees=[]
    db_config={'user':'mahmoud', 
                'password':'qw1234554321',
                'host':'127.0.0.1',
                'database':'employees'
                }
    
    def __init__(self,first_name,last_name,age,department,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.department=department
        self.salary=salary
        self.__class__.employees.append(self)
        self.__class__.insert_employee_into_db(self)
        

    def transfer(self,new_department):
        self.department=new_department
        self.update_employee_into_db()
    
    def fire(self):
        self.__class__.employees.remove(self)
        self.delete_employee_into_db()
    
    
    def show(self):
        
        print(f"first_name: {self.first_name}")
        print(f"last_name: {self.last_name}")
        print(f"age: {self.age}")
        print(f"department: {self.department}")
        print(f"salary: {self.salary}")


    @classmethod
    def List_employees(cls):
        try:
            cnx = mysql.connector.connect(**Employee.db_config)
            cursor = cnx.cursor()
            cursor.execute(f"select * from `employee` where `managed_department` is Null")
            for emp in cursor:
                print(f"first_name: {emp[1]}")
                print(f"last_name: {emp[2]}")
                print(f"salary: {emp[3]}")
                print(f"age: {emp[4]}")
                print(f"department: {emp[5]}")
                print("============================")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.commit()
            cnx.close()

    @staticmethod
    def insert_employee_into_db(employee):
        print(employee)
        try:
            cnx = mysql.connector.connect(**Employee.db_config)
            cursor = cnx.cursor()
            cursor.execute(f"insert into `employee` (`first_name`,`last_name`,`age`,`department`,`salary`) VALUES (%s, %s, %s, %s, %s)",
                            (employee.first_name,employee.last_name,employee.age,employee.department,employee.salary))
            print(cursor)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.commit()
            cnx.close()
    
    def update_employee_into_db(self):
        try:
            cnx = mysql.connector.connect(**Employee.db_config)
            cursor = cnx.cursor()
            cursor.execute(f"update `employee` set department =%s where first_name= %s and last_name = %s",
                            (self.department,self.first_name,self.last_name))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.commit()
            cnx.close()
    
    def delete_employee_into_db(self):
        try:
            cnx = mysql.connector.connect(**Employee.db_config)
            cursor = cnx.cursor()
            cursor.execute(f"delete from `employee` where first_name= %s and last_name = %s",
                            (self.first_name,self.last_name))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.commit()
            cnx.close()
    
class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary,managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department=managed_department
        self.update_manager_department_into_db()

    @classmethod
    def List_managers(cls):
        try:
            cnx = mysql.connector.connect(**Employee.db_config)
            cursor = cnx.cursor()
            cursor.execute(f"select * from `employee` where `managed_department` is not Null")
            for emp in cursor:
                print(f"first_name: {emp[1]}")
                print(f"last_name: {emp[2]}")
                print(f"salary: ******")
                print(f"age: {emp[4]}")
                print(f"department: {emp[5]}")
                print(f"managed_department: {emp[6]}")
                print("============================")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.commit()
            cnx.close()
    
    def show(self):
        print(f"first_name: {self.first_name}")
        print(f"last_name: {self.last_name}")
        print(f"age: {self.age}")
        print(f"department: {self.department}")
        print(f"managed_department: {self.managed_department}")
        print(f"salary: *******")

    def update_manager_department_into_db(self):
        try:
            cnx = mysql.connector.connect(**Employee.db_config)
            cursor = cnx.cursor()
            cursor.execute(f"update `employee` set managed_department =%s where first_name= %s and last_name = %s",
                            (self.managed_department,self.first_name,self.last_name))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.commit()
            cnx.close()

def menu():
    flag=True
    while flag:
        print("Please select an operation:")
        print("Add new employee: a")
        print("Add new manager: m")
        print("List all employees: le")
        print("List all managers: lm")

        print("Exit program: q")
        key=input().lower()
        if key=="e":
            data=get_employee_data()
            Employee(*data)
        elif key=="m":
            data=get_manager_data()
            Manager(*data)
        elif key=="le":
            Employee.List_employees()
        elif key=="lm":
            Manager.List_managers()
        elif key=="q":
            flag=False

def get_employee_data(type="employee"):
    first_name=input(f"\nEnter {type} first_name: ")
    last_name=input(f"\nEnter {type} last_name: ")
    age=int(input(f"\nEnter {type} age: "))
    department=input(f"\nEnter {type} department: ")
    salary=float(input(f"\nEnter {type} salary: "))
    return [first_name,last_name,age,department,salary]

def get_manager_data():
    data=get_employee_data("manager")
    managed_department=input("\nEnter manager managed_department: ")
    data.append(managed_department)
    return data

menu()