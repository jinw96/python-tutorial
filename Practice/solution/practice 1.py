# Solutions for Practice 1

# 1
print("\n# 1")
print("끝말잇기!")

new = input("첫 단어를 입력해주세요: ")
prev = " "

words = []
words.append(new)

is_first = True

while (is_first or new[0] == prev[-1]) and words.count(new) < 2:
  is_first = False
  
  for i in range(len(words)-1):
    print(words[i], " -> ", end='')
  print(words[-1])
  
  prev = new
  new = input("다음 단어를 입력해주세요: ")
  words.append(new)

print("패배 !")


# 2
print("\n# 2")

num = int(input("Enter a natural number: "))

is_prime = True

if num == 1:
    is_prime = False

for i in range(2, int(i**(1/2))+1):
    if num % is_prime == 0:
        is_prime = False
        break

if is_prime:
    print(f"It's a prime number!")    

else:
    print(f"It's not a prime number!")


# 3
print("\n# 3")

year = int(input("Enter a year: "))

is_leap = False

if year % 4 == 0:
    is_leap = True
    if year % 100 == 0:
        is_leap = False
        if year % 400 == 0:
            is_leap = True

if is_leap:
    print("It's a leap year!")
else:
    print("It's not a leap year!")
