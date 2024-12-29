#write a program which will find all such numbers which are divisible by 7 but are not multiple of 5
for number in range (0,101):
    if(number%7==0) and (number%5!=0):
        print(number)
    

#write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically
words=input("Enter Words:").split()
unique_words=sorted(set(words))
print(" ".join(unique_words))
