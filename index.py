#BANKING MANAGEMENT#
acdetails={}
newacno = 1000


def createac():#ac creation
    global newacno
    accno = str(newacno)
    
    name = input("enter the name  ")
    balance = float(input("Enter your first deposit  "))
    
    acdetails[accno]={"Name":name,
    "Balance":balance,"hist":[f"initial deposit:  {balance}"]
    
    }
    print("Account created successfully your account no is " ,accno)
    print("**",accno,"**")
    newacno+= 1
    
def deposit():#deposit function 
    accno=input("Please enter the account number" )
    if accno not in acdetails:
        print("Error account not found ")
        return
    amount= float(input("Enter the amount to deposit"))
    if amount<=0:
        print("Amount must be postive")
        return
    acdetails[accno]["Balance"] += amount
    acdetails[accno]["hist"].append(f"Deposited : {amount}")
    print("successfuly deposited")
    print("new balance is ",acdetails[accno]['balance'])
    
def withdraw():  # withdraw
    accno = input("Please enter the account number  ")
    if accno not in acdetails:
        print("Error account not found ")
        return

    amount = float(input("Enter the amount for withdrawal  "))

    if amount <= 0:
        print("please select correct amount")
        return

    if amount > acdetails[accno]["balance"]:
        print("insufficient balance")
        return

    acdetails[accno]["Balance"] -= amount
    acdetails[accno]["hist"].append(f"Withdrew : {amount}")
    print(
        amount,
        "successfully withdrawed balance is ",
        acdetails[accno]["Balance"],
    )
        
  
    
def balcheck():#balance check
    accno=input("Please enter the account number  " )
    if accno not in acdetails:
        print("Error account not found ")
        return 
    balance=acdetails[accno]['Balance']
    name=acdetails[accno]['Name']
    print(f"your balance : {balance}")
    
    
def loan():#loan
    accno=input("Please enter the account number  " )
    balance=acdetails[accno]['Balance']
    if accno not in acdetails:
        print("Error account not found ")
        return
    loan=float(input("Enter desired loan amount"))
    sal=float(input("Enter your current salary"))
    if sal>= (loan* 0.20)and balance >=(
        loan* 0.10):
         print("Loan approved cash will be credited to your account ")
         return 
    print("not approved ×")
        
        
def show():  # display all saved account details
    if not acdetails:
        print("\nNo accounts saved yet!")
        return

    print("\n================ ALL SAVED ACCOUNTS ================")
    for accno, details in acdetails.items():
        print(f"Account Number  : {accno}")
        print(f"Account Holder  : {details['Name']}")
        print(f"Current Balance : ${details['Balance']:.2f}")
        print("Transaction History:")
        for item in details["hist"]:
            print(f"   - {item}")
        print("--------------------------------------------------")
        
                
def transactionhistory():  # transaction history
    accno = input("please enter Account Number: ")
    if accno not in acdetails:
        print("Error: Account not found")
        return

    print(f"\n--- History for {acdetails[accno]['name']} ---")
    for item in acdetails[accno]["hist"]:
        print(item)    
#*****MAIN MENU*****#
while True:
    print("=================================")  
    print("=== BANKING MANAGEMENT SYSTEM ===")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Check Loan Eligibility")
    print("6. Transaction history")
    print("7. show saved details")
    print("8. exit")
    print("=================================")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        createac()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        balcheck()
    elif choice == "5":
        loan()
    elif choice =="6":
        transactionhistory()
    elif choice =="7":
        show()
    elif choice == "8":
        print("Thank you for using our bank. Goodbye!")
        break
    else:
        print("Invalid choice! Please choose a number from 1 to 6")