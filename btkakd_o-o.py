# # class Person:
# #     # class attributes
# #     address = "not available"

# #     # constructor
# #     def __init__(self, name, year):

# #         # object attributes
# #         self.name = name
# #         self.year = year

# #     #instance methods
# #     def intro(self):
# #         print("Hello World. I am " + self.name)

# #     def calculateAge(self):
# #         return 2022 - self.year


# # p1 = Person(name ="Furkan", year= 2000)
# # p2 = Person(name = "Nebiye", year = 2000)

# # print(f"{p1.name} is {p1.calculateAge()} years old.")
# # print(f"{p2.name} is {p2.calculateAge()} years old")




# class Circle:
#     # Class object attribute
#     pi = 3.14

#     def __init__(self, radius = 1):
#         self.radius = radius
    
#     # Methods
#     def calcCircumference(self):
#         return 2 * self.pi * self.radius

#     def calcArea(self):
#         return self.pi * (self.radius)**2 

# p1 = Circle()
# p2 = Circle(5)

# print(f"The circumference of the circle is {p1.calcCircumference()} meters")
# print(f"The circumference of the circle is {p2.calcCircumference()} meters")

# print(f"The area of the circle is {p1.calcArea()} metersquares")
# print(f"The area of the circle is {p2.calcArea()} metersquares")


#INHERITANCE

# class Person():
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#         print("Person created")
#     def who_am_i(self):
#         print("I am a person")


# class Student(Person):
#     def __init__(self, fname, lname, number):
#         Person.__init__(self, fname, lname) # equivalent to super().__init__(fname, lname)
#         self.studentnumber = number
#         print("Student created")

#     #overriding 
#     def who_am_i(self):
#         print("I am a student")

#     def say_hello(self):
#         print("Hello I am a student")

# class Teacher(Person):
#     def __init__(self, fname, lname, branch):
#         super().__init__(fname, lname)
#         self.branch = branch
    
#     def who_am_i(self):
#         print(f"I am a {self.branch} teacher")


# x = Person("Furkan", "??elen")
# y = Student("Nebiye", "Yavuz", 1269)
# z = Teacher("Ali Tamer", "??nal", "IE" )

# print( x.firstname + " " + x.lastname )
# print( y.firstname + " " + y.lastname + " " + str(y.studentnumber))
# print( z.firstname + " " + z.lastname + " " + str(z.who_am_i()))


# ??ZEL METOTLAR

# mylist = [1, 2, 3]
# myString = "my string"

# print(len(myList))
# print(len(myString)) 
# "len" metodu her bir obje i??in farkl?? ??al??????r.

# class Movie():
#     def __init__(self, title, director, duration):
#         self.title = title
#         self.director = director
#         self.duration = duration
#         print("movie objesi olu??turuldu")
    
#     def __str__(self):
#         return f"{self.title} by {self.director}"
    
#     def __len__(self):
#         return self.duration

#     def __del__(self):
#         print("Movie object has been deleted")



# m = Movie("filmin ad??", "y??netmen ad??", 120)

# # print(str(myList))
# print(str(m)) #  Output olarak Movie objesinin RAM ??zerinde hangi konumda olu??turuldu??unu verir.

# # print(len(myList))
# # print(len(m))

# # del m

# # print(m)





