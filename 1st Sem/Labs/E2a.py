s1 = {"1","2","3"}
s2 = {"4", "3", "5", "6"}

print("add element in 1st set: ")
s1.add("8")
print(*s1)

print("Remove element from set: ")
s1.remove("2")
print(*s1)

print("Union of sets: ")
newList = s1.union(s2)
print(*newList)

print("Intersection: ")
secList = s1.intersection(s2)
print(*secList)

print("Loop throught the set: ")
for x in s1:
	print(x)
print()

print("Pop operations:")
s1.pop()
print(*s1)

print("Sum of all the elemets: ")
sum=0
for x in s1:
	sum += int(x)
print(sum)

print("Extend set1 with set2: ")
for x in s2:
	s1.add(x)
print(s1)
