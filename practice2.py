num1=int(input("enter a number: "))
num2=int(input("enter another number: "))
if num1<num2:
    print("The smaller number is:", num1)
if num1>num2:
    print("The smaller number is:", num2)
if num1==num2:
    print("Both numbers are equal.")    
if num1!=num2:
    print("The numbers are not equal.")    
if num1<=num2:
    print(num1, "is less than or equal to", num2)
if num1>=num2:
    print(num1, "is greater than or equal to", num2)
else:
    print("End of comparisons.")