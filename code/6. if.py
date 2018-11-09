# 1 Odd, Even
print("\n# 1")

a = int(input("Enter a number: "))

if a%2 == 0:
    print("It's even number!")
else:
    print("It's odd number!")


# 2 +, - / Odd, Even
print("\n# 2")

a = int(input("Enter a number: "))

if a > 0 and a %2 == 0:
    print(f"{a} is positive even number!")
elif a < 0 and a%2 == 0:
    print(f"{a} is negative even number!")
elif a > 0 and a%2 == 1:
    print(f"{a} is positive odd number!")
elif a < 0 and a%2 == 1:
    print(f"{a} is negative odd number!")
else:
    print(f"{a} is zero!")

# 3 A Multiple of Three but Not Even
print("\n# 3")

a = int(input("Enter a number: "))

if a >= 0:
    print(f"{a} is 1-digit number!")
elif a >= 10:
    print(f"{a} is 2-digit number!")
elif a >= 100:
    print(f"{a} is 3-digit number!")
elif a >= 1000:
    print(f"{a} is 4-digit number!")

# 4 A Multiple of Three but Not Even
print("\n# 4")

a = int(input("Enter a number: "))

if a%2 == 0:
    if a%3 == 0:
        print(f"{a} is a multiple of both 2 and 3.")
    else:
        print(f"{a} is a multiple of 2 but not 3.")
else:
    if a%3 == 0:
        print(f"{a} is a multiple of 3 but not 2.")
    else:
        print(f"{a} is not a multiple of 2 or 3.")
