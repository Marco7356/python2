# def welcome():
#     print("hello")

# welcome()
# welcome()
# def add(a,b):
#     return a+b
# result = add(10,25)
# print(result)
# name= "achu"
# def greet():
#     print("hi",name,"how are you")


# greet()
  
# square = lambda x: x*x
# print(square(10))
#  

# def greet(name,age):
#     print("name",name)
#     print("age", age)

# # greet("rahul",25)    
# def greet(name= "user"):
#     print("Helo",name)

# # greet()   
# def total(*numbers) :
#     result = 0
#     for n in numbers:
#         result += n
#     return result

# print(total(10,10,20,20,30,55))

def studentinfo(**data):
    for key, value in data.items():
        print(key,":", value)


studentinfo(name="rahu",age=16,marks=88)        
    

 


