# 1. Alssong Dalssong Pythong
print("\n# 1")

s = "AlsongDalsongPythong" # from this string, we want to print the right one

for c in s:
    print(c, end='')
    
    # 's' one more
    if(c == "s"):
        print(c, end='') # or just print("s", end='')

    # blank after 'g'
    if(c == "g"):
        print(end=' ') # or print(' ', end='') or print('', end=' ')


# 2. How much did I pay..? (or get?)
print("\n# 2")

# list for account, - for pay, + for get
account = [-100, 30, 51, -35, 20, -82, 14]

pay_or_get = input("Want to know 'pay' or 'get'?: ")

total = 0

for money in account:
    if pay_or_get == "pay":
        if money < 0:
            total += money
    else:
        if money > 0:
            total += money
            
total = abs(total)

print(f"{pay_or_get}: {total}")


# 3. How many days are there in a year?
print("\n# 3")

total = 0

days_30 = [4, 6, 9, 11]
days_31 = [1, 3, 5, 7, 8, 10, 12]

for i in range(1, 13):
    if i in days_30:
        total += 30
    elif i in days_31:
        total += 31
    else:
        total += 28
        
print(f"There are {total} days in a year!")

