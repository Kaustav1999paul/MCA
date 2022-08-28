a=[int (x) for x in input("Enter the numbers : ").split(" ")]
print(f"The 3 entered numbers are {a[0]} , {a[1]}, {a[2]}")
if a[0]>a[1] and a[0]>a[2] :
  print(f"{a[0]} is the greatest number")
else:
  if(a[1]>a[2]):
    print(f"{a[1]} is greatest number.")
  else:
    print(f"{a[2]} is the greatest number.")

