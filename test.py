x=input("enter your pin: ")
current_balance=200 
correct_pin=1111
if(int(x)!=correct_pin):
    print("acess denied")
if(int(x)== correct_pin):
    print("acess granted")
    p=input("choose your option check balance,deposit money,withdrawl money: ")
    if(p=="check balance"):
        print("your balance is",current_balance)
    if(p== "deposit money"):
        c=input("how much money u want to deposit: ")
        current_balance=int(c) + current_balance
        print("now your current balance is",current_balance)
    if(p== "withdrawl money"):
        d=input("how much money u want to withdrawl: ")
        if(int(d)>current_balance):
            print("sorry insufficient amount")
        else:
            print("withdrawl sucessfull thank you")




