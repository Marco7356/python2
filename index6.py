# x= "global"
# def outer():
#     x = "enclosing"
#     def inner():
#         x = "local"
#         print("inner x:", x)
#     inner()
#     print("outer x:", x)
# outer()
# print("global x:", x)
def countdown(n):
    print(n)
    if n > 1:
        countdown(n-1)
countdown(10)