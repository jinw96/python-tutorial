# 1. 3xn
print("\n# 1")

a = int(input("Enter a number: "))

total = 0

for i in range(a):
    total += 3

print(f"3 x {a} = {total}")


# 2. 3^n
print("\n# 2")

a = int(input("Enter a number: "))

result = 1

for i in range(a):
    result *= 3

print(f"3 ^ {a} = {result}")


# 3. P(n, r)
print("\n# 3")

n = int(input("Enter 'n' for P(n, r): "))
r = int(input("Enter 'r' for P(n, r): "))

P = 1 # Permutation

for i in range(n, n-r, -1):
    P *= i

print(f"P({n}, {r}) = {P}")


# 4 Loop with List
print("\n# 4")

month = ["january", "february", "march", "april",
         "may", "june", "july", "august",
         "september", "october", "november", "december"]

for m in month:
    print(month.index(m)+1, m.capitalize())

# 5 Loop with String
print("\n# 5")

string = "Hello World!"

for c in string:
    print(c*2, end='')



    

