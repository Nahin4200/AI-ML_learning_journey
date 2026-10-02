
squ = []

for i in range(6):
    squ.append(i*i)

print (squ)  

sq = [i*i for i in range(6)]
print(sq)

sq1 = [i*i for i in range(6) if i%2 !=0]
print (sq1)

sq2 = [i*i for i in range(6) if i%2 ==0]
print (sq2)


num = [1,-3,-4,-6,9,2]

num = [0 if val <0 else val for val in num]
print (num)


words =["hello", "python", "nahin"]

# print (words[0].upper())

words = [val.upper() for val in words]
print (words)
