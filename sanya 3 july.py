'''
h.w. ques =1. wap to find a user's age, any day, any season by user input
2. create a github and linkedin account
3. create summer training repository in github for programs and project


is- identity operator

Q.1 wap to find fibanacci series
Q.2 wap to evaluate a string whther it is palindrome.
Q.3 wap to calculate the gross income of family
Q.4 wap to make a calculator
'''


#to find fibonacci series
print(' fibonacci series ')
n=int(input('enter number of terms: '))
a=0
b=1
for i in range(n):
    c=a+b
    a=b
    b=c
    print(a,' ')


#to check palindrome
print( ' palindrome ')
n=input('enter a string: ')
if n==n[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")


#to calculate gross income of family
print(' gross income ')
class gross():
    def init(s):
        name1=''
        salary1=[]
        name2=''
        salary2=[]
    def getdata(s):
        s.name1=input('enter the name of first family member: ')
        s.salary1=int(input('enter the salry: '))
        s.name2=input('enter the name of second family member: ')
        s.salary2=int(input('enter the salary: '))
    def salary(s):
        s.hra1=s.salary1*0.20
        s.hra2=s.salary2*0.20
        s.da1=s.salary1*0.10
        s.da2=s.salary2*0.10
        s.gross_salary=s.hra1+s.da1+s.hra2+s.da2
    def display(s):
        print('name1: ', s.salary1)
        print('name2: ',  s.salary2)
        print('gross salary: ', s.gross_salary)

g=gross()
g.getdata()
g.salary()
g.display()
     

#to create calculator
while True:
    print( 'calculator ')
    print('1. addition')
    print('2. subtraction')
    print('3. division')
    print('4. multiplication')
    print('5. exit')

    n=int(input('enter the choice from 1-4: '))
    a=int(input('enter first number: '))
    b=int(input('enter second number: '))


    if n==1:
        print('addition of two numbers: ', a+b)
    elif n==2:
        print('subtraction of two numbers: ', a-b)
    elif n==3:
        if b==0:
            print("division by 0 not possible")
        else:
            print('division of two numbers: ', a/b)
    elif n==4:
        print('multiplication of two numbers: ', a*b)
    elif n==5:
        print('exit')
    else:
        print("option does not exist")

    x=input('do you want to continue yes or no: ')
    if x!='yes':
        print('close')
        break


    


