# 1 Advanced Version
print("\n# 1")

for i in range(-6, 7, 2):
    print("*" * (abs(i) + 1))

# 2
print("\n# 2")

n = int(input("How many elements do you want?: "))
l = []

for _ in range(n):
    l.append(input("Input: "))

for i in range(n-1, -1, -1):
    print(l[i], end=' ')

# 3
print("\n# 3")

month = int(input("Enter the month: "))
date = int(input("Enter the date: "))

if month == 1:
    if date >= 1 and date <= 19:
        print("CAPRICORN!")
    elif date >= 20 and date <= 31:
        print("AQUARIUS!")
    else:
        print("You entered the wrong DATE!!")
    
elif month == 2:
    if date >= 1 and date <= 18:
        print("CAPRICON!")
    elif date >= 19 and date <= 29:
        print("PISCES!")
    else:
        print("You entered the wrong DATE!!")
        
elif month == 3:
    if date >= 1 and date <= 20:
        print("PISCES!")
    elif date >= 21 and date <= 31:
        print("ARIES!")
    else:
        print("You entered the wrong DATE!!")
        
elif month == 4:
    if date >= 1 and date <= 19:
        print("ARIES!")
    elif date >= 20 and date <= 30:
        print("TAURUS!")
    else:
        print("You entered the wrong DATE!!")

elif month == 5:
    if date >= 1 and date <= 20:
        print("TAURUS!")
    elif date >= 21 and date <= 31:
        print("GEMINI!")
    else:
        print("You entered the wrong DATE!!")

elif month == 6:
    if date >= 1 and date <= 21:
        print("GEMINI!")
    elif date >= 22 and date <= 30:
        print("CANCER!")
    else:
        print("You entered the wrong DATE!!")

elif month == 7:
    if date >= 1 and date <= 22:
        print("CANCER!")
    elif date >= 23 and date <= 31:
        print("LEO!")
    else:
        print("You entered the wrong DATE!!")

elif month == 8:
    if date >= 1 and date <= 22:
        print("LEO!")
    elif date >= 23 and date <= 31:
        print("VIRGIO!")
    else:
        print("You entered the wrong DATE!!")

elif month == 9:
    if date >= 1 and date <= 23:
        print("VIRGIO!")
    elif date >= 24 and date <= 30:
        print("LIBRA!")
    else:
        print("You entered the wrong DATE !!")

elif month == 10:
    if date >= 1 and date <= 22:
        print("LIBRA !")
    elif date >= 23 and date <= 31:
        print("SCORPIO!")
    else:
        print("You entered the wrong DATE!!")

elif month == 11:
    if date >= 1 and date <= 22:
        print("SCORPIO!")
    elif date >= 23 and date <= 30:
        print("SAGGITARIUS!")
    else:
        print("You entered the wrong DATE!!")

elif month == 12:
    if date >= 1 and date <= 24:
        print("SAGGITARIUS!")
    elif date >= 25 and date <= 31:
        print("CAPRICORN!")
    else:
        print("You entered the wrong DATE!!")

else:
    print("You entered the wrong MONTH!!")
        
