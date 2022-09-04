a = int(input("Enter first number : \t"))
b = int(input("Enter sec number : \t"))
if a > b: #First number is greater
    print("Square of smaller number is : ", b**2)
    print("Cube of the greater number is : ", a**3)

elif b > a: #Second number is greater
    print("Square of greater number is : ",b**2 )
    print("Cube of smaller number is : ", a**3)
    
else:
    print("Enter valid choice...")        
    
