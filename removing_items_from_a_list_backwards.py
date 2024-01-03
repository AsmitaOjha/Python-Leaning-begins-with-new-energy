data = [102,101,4,105,308,103,5,108]
min_valid =100
max_valid= 200
for index in range(len(data)-1,-1,-1):
    if data[index]<min_valid or data[index]>max_valid:
        print(index,data)
        del data[index]
print(data)

# //reversed() function and it's use
original_list = [1,2,3,4,5]
reversed_list = list(reversed(original_list))
print(reversed_list)
#revisit print
name= "Asmita"
age=19
print(name,age,2024, "girl", sep=',')

#join functrion
flower = ["Rose","lily","sunflower","marigold","lavendar","evening primrose"]
separator = " | "
joinning = separator.join(flower)
print(joinning)

#split function
Myself = "Hello, Dudy. How are you? Call me naa 😟"
words = Myself.split("?git")
print(words)