#worldcup program
worldcup2021= ( 2021, "india", "pakistan", "netherlands", "10 july 2021", 11, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k')
worldcup2027= {"year": 2027, "host country": "nil", "winner": "nil", "runnerup": "nil", "date": "nil", "team members":"tbd", "tm1": "tbd","tm2":"tbd","tm3":"tbd","tm4":"tbd", "tm5":"tbd","tm6":"tbd","tm7":"tbd","tm8":"tbd","tm9":"tbd","tm10":"tbd","tm11":"tbd"}

year= int(input("enter the world cup year 2021 or 2027: "))

if year==2021:
    print(worldcup2021)
elif year==2027:
    print(worldcup2027)
else:
    print("sorry this year data does not exist")

print("updation of worldcup2027")

a=worldcup2027
a["host country"]=input("enter the name of host country: ")
a["winner"]=input("enter the name of winner country: ")
a["runnerup"]=input("enter the runner up country: ")
a["date"]=input("enter the date: ")
a["team meambers"]=input("enter the no of team members: ")

print("updated 2027worldcup details")
for key,value in worldcup2027.items():
    print(key, ":", value)


#atm program
input(" ATM MENU ")

balance= 10000
pin=1005

print(" choose language")
print("1. hindi")
print("2. english")
language= int(input("enter your choice"))
if language==1:
    print("english selected")
else:
    print("this language is not available")
    
newpin= int(input("enter the four digit pin: "))
if newpin==pin:
    while True:
        print(" welcome to ATM")
        print("1. check balance")
        print("2. withdraw")
        print("3. deposit")
        print("4. exit")
        choice= int(input("enter your choice"))
        if choice==1:
            print(" your current balance is: ", balance)
        elif choice==2:
            value=int(input("enter the amount you want to withdraw"))
            if value<=balance:
                balance-=value
                print("cpollect your cash")
                print("remaining balance", balance)
            else:
                print("insufficient balance")
        elif choice==3:
            value=int(input("enter the amount you want to deposit"))
            balance+=value
            print(" successful deposit ")
            print(" updated balance", balance)
        elif choice==4:
            print(" thank you for using ATM")
            break

            
    
