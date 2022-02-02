import budgets

bclor = open("budgetclothing.txt", "r")
bentr = open("budgetentertainment.txt", "r")
bfoor = open("budgetfood.txt", "r")

to = int(input("What budget do you want to access? Please enter one of the following numbers.\n1. Clothing\n2. Entertainment\n3. Food\n"))

if to == 1:
    print("Your budget is: " + "£" + bclor.readline())
    move = "\n1. Entertainment\n2. Food\n"
    bclor.seek(0)
    out = budgets.Clothing("Clothing", int(bclor.read()))
    bclor.close()
elif to == 2:
    print("Your budget is: " + "£" + bentr.readline())
    move = "\n1. Clothing\n2. Food\n"
    bentr.seek(0)
    out = budgets.Entertainment("Entertainment", int(bentr.read()))
    tomoney = bentr.readline()
    bentr.close()
elif to == 3:
    print("Your budget is: " + "£" + bfoor.readline())
    move = "\n1. Clothing\n2. Entertainment\n"
    bfoor.seek(0)
    out = budgets.Food("Food", int(bfoor.read()))
    tomoney = bfoor.readline()
    bfoor.close()

into = int(input("\nWhat budget do you want to transfer to? Please one of the following numbers." + move))

if to == 1:
    boutw = open("budgetclothing.txt", "w")
    if into == 1:
        print("Your budget is: " + "£" + bentr.read())
        bentr.seek(0)
        to = budgets.Entertainment("Entertainment", int(bentr.read()))
        btow = open("budgetentertainment.txt", "w")
        bentr.close()
    elif into == 2:
        print("Your budget is: " + "£" + bfoor.read())
        bfoor.seek(0)
        to = budgets.Food("Food", int(bfoor.read()))
        btow = open("budgetfood.txt", "w")
        bfoor.close()
elif to == 2:
    boutw = open("budgetentertainment.txt", "w")
    if into == 1:
        print("Your budget is: " + "£" + bclor.read())
        bclor.seek(0)
        to = budgets.Clothing("Clothing", int(bclor.read()))
        btow = open("budgetclothing.txt", "w")
        bclor.close()
    elif into == 2:
        print("Your budget is: " + "£" + bfoor.read())
        bfoor.seek(0)
        to = budgets.Food("Food", int(bfoor.read()))
        btoow = open("budgetfood.txt", "w")
        bfoor.close()
elif to == 3:
    boutw = open("budgetfood.txt", "w")
    if into == 1:
        print("Your budget is: " + "£" + bclor.read())
        bclor.seek(0)
        to = budgets.Clothing("Clothing", int(bclor.read()))
        btow = open("budgetclothing.txt", "w")
        bclor.close()
    elif into == 2:
        print("Your budget is: " + "£" + bentr.read())
        bentr.seek(0)
        to = budgets.Entertainment("Entertainment", int(bentr.read()))
        btow = open("budgetentertainment.txt", "w")
        bentr.close()

money = int(input("\nHow much do you want to transfer?\n£"))

to.deposit(out.withdraw(money))

outs = str(out.amount)
tos = str(to.amount)

print(out)
print(to)

boutw.write(outs)
boutw.close()
btow.write(tos)
btow.close()

bclor.close()
bentr.close()
bfoor.close()