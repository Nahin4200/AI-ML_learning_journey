 
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
        




class Laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self. RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
                print (f"storage type =  {cls.storage_type}")

    def get_info(self):
        print (f"latop has {self.RAM} RAM and {self.storage} {self.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (price*discount/100)
        print(f"discount price = {final_price}")
          

l1 = Laptop("16gb","512gb")               
l2 = Laptop("8gb","256gb")

l1.get_info()
l2.get_info()
Laptop.get_storage_type()
l1.calc_discount(40_000, 10)
