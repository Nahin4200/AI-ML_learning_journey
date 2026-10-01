 
# class Student:
    # sub = "python"
    # college = "ABC college"
#     def __init__(self, name, cgpa):
#         self.name = name 
#         self.cgpa = cgpa

#     def get_cgpa(self):
#         return self.cgpa




# std1 = Student("nahin", 3.50)
# std2 = Student("fahim", 3.50)
# std3 = Student("sid", 3.50)

# # print(std1.name,std1.cgpa)  
# # print(std2.name,std2.cgpa)  
# # print(std3.name,std3.cgpa) 

# print(f"{std1.name} has cgpa {std1.get_cgpa()}college {std1.college}")  
# print (std1.college)
# print (Student.college)
        




# class Laptop:
#     storage_type = "SSD"

#     def __init__(self, RAM, storage):
#         self. RAM = RAM
#         self.storage = storage

#     @classmethod
#     def get_storage_type(cls):
#                 print (f"storage type =  {cls.storage_type}")

#     def get_info(self):
#         print (f"latop has {self.RAM} RAM and {self.storage} {self.storage_type}")

#     @staticmethod
#     def calc_discount(price, discount):
#         final_price = price - (price*discount/100)
#         print(f"discount price = {final_price}")
          

# l1 = Laptop("16gb","512gb")               
# l2 = Laptop("8gb","256gb")

# l1.get_info()
# l2.get_info()
# Laptop.get_storage_type()
# l1.calc_discount(40_000, 10)



# class store:
#     product_count = 0

#     def __init__(self, name, price):
#         self.name = name 
#         self.price = price
#         store.product_count += 1
        

#     @staticmethod
#     def discount_price(price, discount):
#         print (f" discount price = {price - price*discount/100}")

#     @classmethod
#     def get_count(cls):
#         print (f"total product in store = {cls.product_count}") 

# p1 = store("laptop",40_000)
# p2 = store("phn",20_000)
# p3 = store("pc",20_0000)

# print (p1.name,p1.price)

# store.get_count()

# store.discount_price(p1.price, 10)




# class BankAccount:
#     def __init__(self, name, balance):

#         self.name =  name 
#         self.__balance = balance


#     def get_balance(self):
#             return self.__balance

#     def set_balance(self,new_balance):
#             self.__balance = new_balance

# acc1 = BankAccount("Nahin",20000)

# acc1.set_balance(400000)

# print (acc1.name, acc1.get_balance())




#inheritance


# class employee:
#     start_time = "10am"
#     end_time = "6pm"

#     def change_time (self, new_end_time):
#         self.end_time = new_end_time


# class teacher (employee):
#     def __init__(self, subject):
#         self.subject = subject
           
# t1 = teacher ("math")
# t1.change_time("5pm")

# print(t1.subject, t1.start_time, t1.end_time)





# class employee:
#     start_time = "10am"
#     end_time = "6pm"

# class adminstaff(employee):
#     def __init__(self, role ):
#         self.role = role

# class accountant (adminstaff):
#     def __init__(self, salary, role):
#         super().__init__(role)
#         self.salary = salary


# acc1 = accountant(25_000,"CA") 

# print (f"role is {acc1.role} salary is {acc1.salary} start time {acc1.start_time} end time {acc1.end_time}")





# class teacher:
#     def __init__(self, salary):
#         self.salary = salary

# class student:
#     def __init__(self, cgpa):
#         self.cgpa = cgpa

# class TA (teacher,student):
#     def __init__(self, salary, cgpa, name):
#         teacher.__init__(self,salary)
#         student.__init__(self, cgpa) 
#         self.name = name    


# ta1 = TA(15000, 3.9, "nahin")
# print (ta1.name, ta1.salary, ta1.cgpa)





#abstraction 




from abc import ABC, abstractmethod

class Animal (ABC):
    @abstractmethod
    def make_sound(self):
        pass

class lion(Animal): 
    def make_sound(self):
        print ("Roar!")

l1 = lion()
l1.make_sound()        




