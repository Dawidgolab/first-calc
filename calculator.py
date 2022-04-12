Choice = input("1 - '*', 2 - '/', 3 - '+', 4 - '-'")

a = int(input("First number:"))
b = int(input("Second number:"))

if(Choice == '1'):
    print(a * b)
    
elif(Choice == '2'):
    if(b == 0):
        print('The wrong answer')
    else:
        print(a / b)
        
elif(Choice == '3'):
    print(a + b)
    
elif(Choice == '4'):
    print(a + b)
    
else:
    print("You chose wrong")
