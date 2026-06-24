balance=20000
pin="4567"
attempts=0
while attempts<3:
    e=input("enter pin:")
    if e==pin:
        print("correct pin:")

        
        #if atm condition are true
        while True:
            print("1.withdraw")
            print("2.deposite")
            print("3.check balance")
            print("4.exit")
            #to check the true input values
            choice=input("enter your choice:")
            #conditions apply
            if choice=="1":
                amount=float(input("enter amount to withdraw:"))
                if amount<=balance:
                    balance -= amount
                    print("withdraw successfull")
                    print("Remaining Balance:",balance)
                else:
                    print("Insufficient Balance")
            if choice=="2":
                amount=float(input("enter amount to deposite:"))
            if amount%100==0:
                balance+=amount
                print("deposite successfull")
                print("Remaining balance",balance)
            else:
                print("Invalid amount")
                print("pls deposit only multiples of 100")
                    
            #else:
             #   print("deposite unsuccessfull")
            if choice=="3":
                print("current balance",balance)
            if choice=="4":
                print("Thank you for using ATM")
                break
            #attempts+=1
        break
    else:
        print("Invalid pin")
        attempts+=1
else:
    print("card block")
            
        

                             
            
            
    
    
    