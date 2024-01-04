user_input = input("Please enter three numbers:")
string_tokens = user_input.split(",")
#convert the tokens intp integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

#calculate the result : a+b-c
a,b,c = int_tokens
result = a+b-c
#result = int_tokens[0] + int_tokens[1]-int_tokens[2]


#output the result
print(result)
