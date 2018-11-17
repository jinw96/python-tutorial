# 1
print("\n# 1")

string = "Life is short, you need python."

print(string[:4])
print(string[8:13])
print(string[-12:-8])
print(string[-7:-1])


# 2
print("\n# 2")

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

print(string1.upper() == string2.upper())

# 3
print("\n# 3")

scores = []

scores.append(int(input("Chan: ")))
scores.append(int(input("A-hyeon: ")))
scores.append(int(input("wooZine: ")))
scores.append(int(input("SSoyeon: ")))
scores.append(int(input("SeungRock: ")))
scores.append(int(input("ur_doyeon: ")))
scores.append(int(input("1000_sso: ")))

scores.remove(max(scores))
scores.remove(min(scores))

print("ZingWoo's score:", sum(scores) / len(scores))
