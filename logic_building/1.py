#Check if a number is positive, negative, or zero.
number=int(input("Enter Any Number:"))
if(number==0):
    print(f"Number is zero.")
elif(number>0):
    print(f"Number {number} is Positive.")
else:
    print(f"Number {number} is Negative.")