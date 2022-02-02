import budgets

bclor = open("budgetclothing.txt", "r")
bentr = open("budgetentertainment.txt", "r")
bfoor = open("budgetfood.txt", "r")

clothing, entertainment, food = [], [], [] 

month = int(input("What month do you want to budget for? Please enter one of the following numbers.\n1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. July\n8. August\n9. September\n10. October\n11. November\n12. December\n")) - 1

print(month)

to = int(input("What budget do you want to access? Please enter one of the following numbers.\n1. Clothing\n2. Entertainment\n3. Food\n"))

for m in bclor.readlines():
    lines = m.split('\\n')
    clothing.append(int())

for m in bentr.readlines():
    entertainment.append(int())

for m in bfoor.readlines():
    food.append(int())

if to == 1:
    print(clothing)
    tomonths1 = range(0,month)
    tomonths2 = range(month,11)
    bclor.seek(month)
    print("Your budget is: " + "£" + bclor.readline())
    move = "\n1. Entertainment\n2. Food\n"
    bclor.seek(month)
    out = budgets.Clothing("Clothing", int(bclor.read()))
    bclor.close()
elif to == 2:
    bentr.seek(month)
    print("Your budget is: " + "£" + bentr.readline())
    move = "\n1. Clothing\n2. Food\n"
    bentr.seek(month)
    out = budgets.Entertainment("Entertainment", int(bentr.read()))
    tomoney = bentr.readline()
    bentr.close()
elif to == 3:
    bfoor.seek(month)
    print("Your budget is: " + "£" + bfoor.readline())
    move = "\n1. Clothing\n2. Entertainment\n"
    bfoor.seek(month)
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