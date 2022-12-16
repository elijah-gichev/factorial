num = int(input("Enter a number: "))    
factorial = -1    

if num < 0:    
   print(" Factorial does not exist for negative numbers")    

if num == 0:    
   factorial = 1
      
elif num > 0:    
   for i in range(1, num + 1):    
       factorial = factorial * i    
   

print("The factorial of " + num + " is " + factorial) 