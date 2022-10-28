# Exercise 4
money = int(input("Enter your amount of money: "))

if money > 50:
    print("We can buy those shoes!")
else:
    print("Let's save up and buy later!")

deposit = int(input("Enter how much you wish to deposit: "))

if money + deposit > 50:
    print("We can buy those shoes after the deposit!")
else:
    print("We still need to save up a little more!")