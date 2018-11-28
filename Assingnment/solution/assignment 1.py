"""
# 1
print("\n# 1")

birth_year = int(input("Enter your birth year: "))
this_year = int(input("Enter this year: "))

age = this_year - birth_year + 1

print(f"\nYour age is {age} !")
"""
# 2
print("\n# 2")

for i in range(5):
    n = 2 * i + 1
    print("*" * n)
