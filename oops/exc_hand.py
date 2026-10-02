
try:
    x= int (input("enter x:"))
    ans = 10/x
except ZeroDivisionError:
    print ("con't divide by zero")

except ValueError:
    print("invalid input")  

else:
    print (f"ans = {ans}")  

finally:
    print("end of code")          