# 1 Intro to List
print("\n# 1")
a = [1, 2, 3,]
print(a)
b = ['a', 'b', 'c',]
print(b)
c = [1, 'x', 10, 'abc', 10.0,]
print(c)

# 2 Indexing and Slicing
print("\n# 2")
a = ['a', 'b', 'c', 'd', 'e', 'feg',]
print("a:", a)
print()
print("a[3]:", a[3])
print("a[2:5]:", a[2:5])
print("a[-3:]:", a[-3:])
print("a[-1][:-2]:", a[-1][:-1])

# 3 List Methods
print("\n# 3")
team = ["Ceos", 2018, "8th",]
nums = [2, 4, 4, 1,]
words = ["alssong", "dalssong", "pythong",]

print("team:", team)
print("nums:", nums)
print("words:", words)
print()

print("len(words):", len(words))
print("max(nums):", max(nums))
print("min(nums):", min(nums))
print("sum(nums):", sum(nums))
print("nums.count(0):", nums.count(0))
print("nums.index(1):", nums.index(1))
team.reverse()
print("After team.reverse():", team)
team.clear()
print("After team.clear():", team)
nums.append(38)
print("After nums.append(38):", nums)
nums.extend([9,1])
print("After nums.extend([9,1]):", nums)
nums.remove(4)
print("After nums.remove(4):", nums)
words.insert(1, 'hago')
print("After words.insert(1, 'hago'):", ' '.join(words))
words.insert(-1, 'han')
print("After words.insert(-1, 'han'):", ' '.join(words))
print("nums + words:", nums + words)
print("nums * 2:", nums * 2)


