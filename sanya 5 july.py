#pattern
print("star pattern")
rows = 7
for i in range(0, rows):
    print("*" * i)

rows = 5
for i in range(rows):
    print(" " * (rows-i), end="")
    print("*" * (2*i+1))

rows = 6
for i in range(1 , rows+1):
    print("*" *i)
for i in range(rows-1, 0, -1):    
    print("*" *i) 


#operations
print("area & perimeter")
x = 7
perimeter = 2*3.14*x
area = 3.14*x*x
print(perimeter)
print(area)


#prime numbers
print("prime no.s from 2 to 101")
for num in range(2, 101):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)

#payment gateway
print("payment gateway")
class payment:
    def pay(amount):
        amount=int(input("enter payment amount: "))
        print("amount: ",amount)

class creditcard(payment):
    pass
class upi(payment):
    pass
class netbanking(payment):
    pass

print("choose payment method")
print("1. credit card")
print("2. upi")
print("3. netbanking")
choice=int(input("enter choice: "))

if choice==1:
    payment=creditcard()
    print("payment through credit card")

elif choice==2:
    payment=upi()
    print("payment through upi")

elif choice==3:
    payment=netbanking()
    print("payment through netbanking")

else:
    print("invalid choice")


payment.pay()

#season determination
print("guessing the season")
age=int(input("enter age: "))
month=int(input("enter current month(1-12): "))
day=int(input("enter date(1-31): "))

if month==12 or month==1 or month==2 and day>=1 or day<=31:
    season="winter"

if month==3 or month==4 or month==5 and day>=1 or day<=31:
    season="spring"

if month==6 or month==7 or month==8 and day>=1 or day<=31:
    season="summer"

if month==9 or month==10 or month==11 and day>=1 or day<=31:
    season="autmn"

print("age: ",age)
print("date: ",day,"-",month)
print("season: ",season)
