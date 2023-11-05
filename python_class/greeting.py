name = input("Enter your given name ")
print(name)


#Condition the input
name = name.lower()
#print(name)
name = name.replace(" ", "_")
#print(name)
name = name.replace(".", "_")
print(name)
print(type(name))
print(" ")

#Check for [m,t] in it
#first initialise message string

message = "Oh. Hi." 
if "m" in name:
    message = "Wow, you have such an MT filled name - how lovely!"
elif "t" in name:
    message = "Wow, you have such an MT filled name - how lovely!"

print(message)


    



