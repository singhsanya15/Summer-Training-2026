class account:
    pass
a1=account()
a2=account()
a3=account()
print(a2)
print(a3)
print(a1)


#student information system
print("student information system ")
class student():
    def init(values):
        values.name= ''
        values.rollno=[]
        values.marks=[]

    def getdata(values):
        values.name= input('enter the name of student: ')
        values.rollno= int(input('enter the rollno of student: '))
        values.m1= int(input('enter marks of subject1: '))
        values.m2= int(input('enter marks of subject2: '))
        values.m3=int(input('enter marks of subject3: '))

    def calculate_percentage(values):
        values.percentage=(values.m1+values.m2+values.m3)/3

    def display_data(values):
        print('name: ',values.name)
        print('rollno: ', values.rollno)
        print('percentage: ',values.percentage, '%')

s=student()
s.getdata()
s.calculate_percentage()
s.display_data()


#bank account
print(" bank account ")
class bankaccount():
    def init(acc):
        acc.name=''
        acc.number=[]
        acc.balance=[]

    def getdata(acc):
        acc.name=input('enter the account holder name: ')
        acc.number=int(input('enter the account nymber: '))
        acc.balance=float(input('enter the account balance: '))

    def deposit(acc):
        amount=int(input('enter the amount you want to deposit: '))

        if amount>0:
            acc.balance+=amount
            print('amount deposited successfully')

    def withdraw(acc):
        amount=int(input('enter the amount you want to withdraw: '))
 
        if amount<=acc.balance:
            acc.balance-=amount
            print("collect your cash")
        else:
            print("insufficient balance")

    def display_balance(acc):
        print('your balance is: ', acc.balance)

b=bankaccount()
b.getdata()
b.deposit()
b.withdraw()
b.display_balance()

#employee salary calculator
print(" employee salary calculator ")
class employee():
    def init(emp):
        emp.id=[]
        emp.name=''
        emp.salary=[]

    def getdata(emp):
        emp.id= int(input('enter the employee id: '))
        emp.name= input('enter the employeename: ')
        emp.salary=int(input('enter the employee salary: '))

    def calculate_salary(emp):
        emp.hra=emp.salary*0.20
        emp.da=emp.salary*0.10
        emp.gross_salary=emp.salary+emp.hra+emp.da

    def display(emp):
        print(" employee id: ", emp.id)
        print('employee name: ',emp.name)
        print('basic salary: ',emp.salary)
        print('hra: ',emp.hra)
        print('da: ',emp.da)
        print('gross salary: ',emp.gross_salary)

e=employee()
e.getdata()
e.calculate_salary()
e.display()

        
#rectangle operations
print(" rectangle operations ")
class rectangle():
    def init(obj):
        obj.length=[]
        obj.breadth=[]

    def getdata(obj):
        obj.length=int(input('enter the length of rectangle: '))
        obj.breadth=int(input('enter the breadth of rectangle: '))

    def operations(obj):
        obj.area=obj.length*obj.breadth
        print('area of rectangle is: ', obj.area)
        obj.perimeter=2*(obj.length+obj.breadth)
        print('perimeter of rectangle is: ',obj.perimeter)

    def check_square(obj):
        if obj.length==obj.breadth:
            print(' it is a square ')
        else:
            print(' it is not a square ')

r=rectangle()
r.getdata()
r.operations()
r.check_square()
        

#vehicle management system
print(' vehicle management system ')
class vehicle():
    def init(v):
        v.brand=''
        v.model=''

    def getdata(v):
        v.brand=input('enter the brand of vehicle: ')
        v.model=input('enter the model of vehicle: ')

    def display(v):
        print('brand: ', v.brand)
        print('model: ', v.model)

class car(vehicle):
    def getcar(v):
        v.fueltype=input('enter fuel type: ')

    def display(v):
        print(" car details")
        print('brand: ', v.brand)
        print('model: ',v.model)
        print('fueltype: ',v.fueltype)

class bike(vehicle):
    def getbike(v):
        v.enginecapacity=input('enter engine capacity: ')

    def display(v):
        print(' bike details ')
        print('brand: ',v.brand)
        print('model: ',v.model)
        print('fuel capacity: ',v.enginecapacity)

c=car()
c.getdata()
c.getcar()
c.display()

b=bike()
b.getdata()
b.getbike()
b.display()
        
        

        
