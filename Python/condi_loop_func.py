
#conditional statement


# age = int (input("enter age:"))

# if(age>18):
#     print ("adult")
# else:
#     print ("not adult")   


# marks  = int (input("enter marks:"))

# if (marks>=80):
#     print ("A+")
# elif(marks>=70):
#     print ("A")
# elif(marks>=60):
#     print("A-")
# elif(marks>=40):
#     print("B")
# elif(marks<40):
#     print("F")    


# user_name = input ("enter user_name:")
# passw = input ("enter pass:")

# if (user_name == "admin" and passw == "123"):
#     print("success")
# else:
#     if (user_name != "admin"):
#         print ("rong user_name")
#     else:
#         print ("rong pass")  



# color = input ("enter color:")

# match color:
#     case "green":
#         print("go")
#     case "yellow":
#         print("look")
#     case "red":
#         print("stop")
#     case _:
#         print ("wrong color")            




#loops


# n = 0
# while (n < 5):
#     print("nahin ")
#     n += 1

# count= 0
# while (count<= 5):
#     print(count)
#     count += 1   


# n = int (input("enter n:"))

# i = 1
# while (i <= 10):
#     print(n * i)
#     i += 1


# i = 1
# while (i <= 10):
#     if(i % 6 == 0):
#         break
#     print(i)
#     i += 1

# i = 1
# while (i <= 20):
#     if(i % 2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1    


# str1 = "hello"

# for i in str1:
#     print (i)

# for i in range(6):
#     print(i)  
# for i in range(1,6):
#     print(i)  
# for i in range(1,10,2):
#     print(i)            

# word = "artificial intelligence"
# count = 0
# for ch in word:
#     if (ch == "i"):
#         count += 1
# print("count of i = ", count)




#Functions


# def hello():
#     print ("hello")

# hello()    

# def sum (a,b):
#     s = a+b
#     return s

# print(sum(4,5))
# print(sum(9,5))


# avg = lambda a,b: (a+b)/2
# print(avg(4,5))


#a = 1
def fac (n):
    a = 1
    for i in range(1,n+1):
        a *=i
    return a 

n = int (input("enter num:"))
print(fac(n))      



