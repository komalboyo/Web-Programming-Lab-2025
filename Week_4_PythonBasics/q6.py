# Write a Python class to implement pow(x, n)

class Power:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def my_pow(self):
        return self.x ** self.n

x = float(input("Enter base x: "))
n = int(input("Enter exponent n: "))

power_calculator = Power(x, n)
result = power_calculator.my_pow()
print(f"{x} raised to the power of {n} is: {result}")
