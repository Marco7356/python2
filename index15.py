# text = "banana"
# frequency ={}

# for char in text:
#     if char in frequency:
#         frequency[char]+=1
#     else:
#         frequency[char]=1
# maxi = 0
# second=0
# freq=""
# second_freq=""
# for key,value in frequency.items():
#     if maxi<value:
#         second=maxi
#         second_freq=freq
#         maxi=value
#         freq=key
#     elif value>second:
#         second = value
#         second=value
#         second_freq=key

# print("most freq char",freq,"is repeated",maxi,"Times")
# print("second freq char is ",second_freq,second,"times")
# for i in range(1,6,1):
#     print(i*"*", end="")
# for i in range(1,6):
#     for j in range(i):
#         print("*", end="")
num=10
n=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end="")
        num+=1
    print()
    
    