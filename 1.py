import time
print("---Welcome---")
print("--ATM CARD Service--")
a = input("Enter your name: ")
print(a)

c = int(input("Enter your CARD last four digits: "))
print(c)

#for dealy of process accessing CARD
time.sleep(5)

password=1234

pin=int(input("Enter your ATM pin: "))

balance = 10000


if pin==password:
    while True:
        print("""
            1 == Balance
            2 == Withdraw balance
            3 == Deposit balance
            4 == Exit 
            """
        )
        try:
            option=int(input("Please enter your choise: "))
        except:
            print("Please enter valid option ")
            #for option 1 Balance
        if option==1:
            print("********************")
            print(f"Your current balance is {balance}")

            print("********************")
            print("********************")
        if option==2:

            withdraw_amount=int(input("Please enter withdraw amount: "))

            balance=balance-withdraw_amount
            print("********************")
            print(f"{withdraw_amount} is debited from your account")
            print("********************")
            print(f"Your updated balance is {balance}")
            print("********************")           
            print("********************")
        if option==3:
            deposit_amount=int(input("Please enter Deposit amount: "))

            balance=balance+deposit_amount
            print("********************")
            print(f"{deposit_amount} is cradited your account")
            print("********************")
            print(f"Your updated balance is {balance}")
            print("********************")
            print("********************")  
        if option==4:
            break

else:
    print("Wrong pin please try again")
    print("********************") 
    print("********************")
    print("********************")
