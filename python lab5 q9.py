string1 = "hello"
string2 = "world"
new_string = string2[:2] + string1[2:] + " " + string1[:2] + string2[2:]
print(new_string)
