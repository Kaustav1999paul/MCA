l1 = ["1","2","3","4"]
l2 = ["5","6","7","8","9"]
finallist = []
print("List1 length: ", len(l1))
print("List2 lenth: ", len(l2))
print("Elenety at 2", l1[1]) 
l1.sort()
print(l1)
l1.extend(l2)
print(l1)
print("Count 2: ", l1.count("2"))
print("Print range", l1[1:5])
print("Reverse: ", l1[::-1])
sum=0
for x in l1:
 sum+=int(x)
print("Sum", sum)
