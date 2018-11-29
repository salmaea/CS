def change(amount):
    if amount<=1:
        print('error, must be positive change')
    else:
        quarters = amount // 25
        dimes = (amount % 25) // 10
        nickels = (amount % 25 % 10) // 5
        pennies = amount % 5
    print(quarters, " quarters", dimes, " dimes", nickels, "nickels", pennies, " pennies")
change(120)
