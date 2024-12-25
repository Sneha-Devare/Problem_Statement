#Find the largest of three numbers.
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
if(a>b) and (a>c):
   print("a is greater than b and c")
elif(b>a) and (b>c):
   print("b is greater than a and c")
elif(c>a) and (c>b):
   print("c is greater than a and b")
else:
   print("You put something different ")