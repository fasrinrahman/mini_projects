# =========================
# MINI PROJECT 1
# Calculator App
# =========================

print("=== SIMPLE CALCULATOR ===")


# -------------------------
# FUNCTIONS
# -------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b


# -------------------------
# MENU
# -------------------------

print("\nSelect Operation")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


choice = input("\nEnter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))


# -------------------------
# OPERATIONS
# -------------------------

if choice == "1":

    print(
        "Result:",
        add(num1, num2)
    )

elif choice == "2":

    print(
        "Result:",
        subtract(num1, num2)
    )

elif choice == "3":

    print(
        "Result:",
        multiply(num1, num2)
    )

elif choice == "4":

    print(
        "Result:",
        divide(num1, num2)
    )

else:

    print("Invalid choice")
    
    