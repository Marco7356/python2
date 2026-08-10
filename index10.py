# num = {1,2,2,3}
# print(num)

# nums=set([1,2,3,4])
# print(nums)
# print(type(nums))
# 
# nums={10,20,30}
# for item in nums:
#     print(item)
# nums={1,2,3}
# nums.add(3) add one element
# nums.update({3,4,5}) multiple element
#nums.remove(2) remove one element
#nums.discard(5) if value doesnot exist,no keyerror
# x= nums.pop()
# print(x)
# nums=nums.clear()
# print(nums)
# a={1,2,3}
# b={3,4,5}
# print(ab)
# print(a|b)
# print(a-b)
# print(a^b)
# nums={1,2,3}
# print(5 in nums)
# nums=frozenset([1,2,3,4])
# nums.add(4)
# print(nums)
# students={
#     "name":"rahul",
#     "age":20,
#     "course":"pyton"
# }
# print(students)
# data = {
#     "a":"rahul",
#     "a":"achu"
# }
# print(data)
# person = {
#     "name":"anitha",
#     "city":"delhi",
#     "age":23
# }
# print(person)
# person = dict(
#     name="anitha",
#     city = "delhi",
#     age = 30
# )
# print(person)
student = {
    "name": "rahul",
    "age": 20,
    # "city": "tvm"

}
student["age"]=22
student.update({
    "city":"chennai",
    "grade":"a"
})

x = student.del("age")
# print(x)

print(student)
