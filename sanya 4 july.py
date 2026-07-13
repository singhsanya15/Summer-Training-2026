#shape area calculator
print("shape area calculator")
class shape():
    def init(obj):
        length=[]
        breadth=[]
        base=[]
        height=[]
        radius=[]

class circle(shape):
    def area(obj):
        print("circle")
        obj.radius=float(input("enter the radius of circle: "))
        obj.area=3.14*obj.radius*obj.radius
        print("area of circle is: ",obj.area)

class rectangle(shape):
    def area(obj):
        print("rectangle")
        obj.length=float(input("enter the length: "))
        obj.breadth=float(input("enter the breadth: "))
        obj.area=obj.length*obj.breadth
        print("area of rectangle: ",obj.area)

class triangle(shape):
    def area (obj):
        print("triangle")
        obj.base=float(input("enter the base: "))
        obj.height=float(input("enter the height: "))
        obj.area=0.5*obj.base*obj.height
        print("area of triangle: ",obj.area)

c=circle()
c.area()

r=rectangle()
r.area()

t=triangle()
t.area()       

#result grading
print("result grades")
s1 = int(input("enter marks: "))
s2 = int(input("enter marks: "))
s3 = int(input("enter marks: "))
result = 0
result = ((s1 + s2 + s3) / 300)*100

if result >= 90:
    print("Grade A")
elif result >= 80:
    print("Grade B")
else:
    print("Grade C")


#factorial
print("factorial of number")
a = int (input("enter a number: "))
fact = 1
for i in range(1, a + 1):
    fact = fact * i
print("Factorial of", a, "is: ", fact)


#largest and smallest number
print("number")
n = [20,21,70,80,64,36]
largest=max(n)
smallest=min(n)
print("largest number is: ",largest)
print("smallest number is: ",smallest)
        

#average
print("average of number")
number = [20,21,70,80,64,36]
total = 0
for i in number:
    total += i
average = total / len(number)    
print("The average is: ", average)
