account =[
    ["Najam",  "6415"],
    ["Naseem", "2323"],
    ["Bilal", "8008"]
]
flag = False
flag2 = False
AccountDetails = [
    [2500,100000,3500],
    [10000,235350,1000],
    [3000,524200,20000]
]
name = input("Enter your name: ")
for a in range(3):
    if name in account[a][0]:
        z = a
        flag = True
        pin = input("Enter your pin: ")
        if pin == account [a][1]:
            flag2 = True
            print("access granted")
        else:
            print("access denied")
process = False
if flag == False:
    print("invalid name ")
elif flag2 == True:
    choice = input("""
    withdraw (1)  
    deposit  (2) 
    balance  (3)
    exit     (4)
    """)
    if choice == "1":
        withdraw_ammount = int(input("Enter withdraw amount: "))
        process = True
        if withdraw_ammount > AccountDetails[z][1]:
            print("insufficient balance")
        else:
            AccountDetails[z][1] -= withdraw_ammount
            print(f'{"new balance is "}{AccountDetails[z][1]}')
    if choice == "2":
        process = True
        deposit_ammount = int(input("Enter deposit amount: "))
        AccountDetails[z][1] += deposit_ammount
        print(f'{"new balance is "}{AccountDetails[z][1]}')
    if choice == "3":
        process = True
        print(f'{"current balance:"}{AccountDetails[z][1]}')
    if choice == "4":
        process = True
        pass
    if process == False:
        print("invalid choice")
