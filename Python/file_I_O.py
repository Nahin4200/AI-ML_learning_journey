# read file


# f = open("demo.txt", "r")

# # data = f.read()
# # print (data)

# data = f.readline()
# print (data)



#write file


# f = open("demo.txt", "w")
# f.write("NAHIN")
# f.close()


#append

# with open("demo.txt", "a") as f:
#     f.write("\nI am learning java")


#create new file

# f = open("demo1.txt", "x")
# f.write("I am learning python")


# delete file

# import os
# os.remove("demo1.txt")





data = True
count = 1
word = "java"

with open("demo.txt", "r") as f:
    while data:
        data = f.readline()
        if (word in data):
            print (f"{word} found in line {count} ")
            break
        count +=1





