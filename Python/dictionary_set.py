

# info = {
# "name": "Nahin",
# "cg": 3.5,
# "sub":["math","science"],

# }

# print (info)
# print (info["name"])
# print(type(info))

# info ["cg"]= 3.9
# print(info["cg"]) 

# info.update({
#     "city": "sylhet"
# })


# print (info.get("cg"))
# print (info.get("cgpa"))

# dict_keys = info.keys()
# print (dict_keys)

# dict_keys = list(info.keys())
# print (dict_keys)

# dict_value = info.values()
# print(dict_value)
# print(type(dict_value))

# dict_value = list(info.values())
# print(dict_value)
# print (type(dict_value))

# print (info.items())



#sets


# s = {1,2,3,3,3}

# print(s)

# s.add(5)
# s.remove(1)
# print(s)

# s.pop()
# print(s)

# s.clear()
# print(s)


# s1 ={1,2,3,4,5}
# s2 = {6,7,8,4,5}

# print (s1.union(s2))
# print (s1.intersection(s2))


info  = [
    ("nahin","math"),
    ("fahiyan","science"),
    ("nahin","science"),
    ("fardin","math"),
    ("fahiyan","math"),
    ("nahin","english"),
    ("fardin","english")
]

uniqe_courses = set()

# for tup in info:
#     # print(tup[0])
#     #print (tup[1])
#     uniqe_courses.add(tup[1])
# print (uniqe_courses)   
 
 
# for name, course in info:
#     if (course=="english"):
#         print (name)    


dict1 = {}
for name, course in info:
    if(dict1.get(name) == None):
        dict1.update({name: set()})
        dict1[name].add(course)
    else:
        dict1[name].add(course)    
print(dict1)                     


