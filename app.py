import budgets

January = budgets.Food("January", 200)
February = budgets.Food("February", 200)

print(January)
print(February)

February.deposit(January.withdraw(35))
print(January)
print(February)


