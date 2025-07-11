Acc = [
    ["ibrahim", "6415"],
    ["naseem", "2323"],
    ["bilal", "8008"]
]

AccDetails = [
    [250,1000,350],
    [100,250,100],
    [300,500,200]
]

name=input("Enter Account Name:")
flag_name = False
flag_pin = False

for i in range(3):
        if name.lower() in Acc[i]:
            pin = input("Enter Password:")
            flag_name = True
            if pin in Acc[i]:
                flag_pin = True
                print("1.Display Balance")
                print("2.Withdraw Money")
                print("3.Deposit Money")
                print("4.Exit")
                menu = input("Please Enter your choice:")
                if menu=="1":
                    print(AccDetails[i][0])
                elif menu=="2":
                    amount = input("Enter Withdrawal Amount:")
                    if int(amount)<=AccDetails[i][2] and int(amount)<AccDetails[i][1]:
                        print(f"${amount} is being printed")
                    else:
                        print("Withdrawal limit or overdraft limit is being exceeded")
                elif menu=="3":
                    amount = input("Enter Deposit Amount:")
                    AccDetails[i][0] += int(amount)
                else:
                    print("GoodBye!")


if not flag_pin:
    print("Pin and Account Name do not match")
if not flag_name:
    print("Account Name was no found")
