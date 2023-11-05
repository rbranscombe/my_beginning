#Sandwich lists
import random

main  = ["aubegine", "coppa", "fruliano salami", "haloumi"]
veggies = ["grilled aubegine", "roasted red petter", "grilled baby marrow", "grilled portobello mushroom"]
dressing = ["balsamic reduction", "Lemon-garlic ailoli", "red wine viegrette", "dijon"]
bread = ["ciabatta", "baguette", "artisan bread", "sourdough"]




print("")
print("")

print("Welcome to Lazy Chef")
print("")
print("- Sandwich de Jour -")

# comment out easier exercise from Lists 1 
#print(random.choice(main))
#print(random.choice(veggies))
#print(random.choice(dressing))
#print(random.choice(bread))
#print("")
#print("Enjoy!")
#print("")



#write program to generate random sami name and ingredients to generate menu board options.
#no repetitions of sami names or ingredients


handle = ['fiera', 'San Giovessi', 'San Giacmo', 'Siena']   
handle_old = handle
handle_new = handle
print(f"handle: {handle}")
print(f"handle_old: {handle_old}")
print(type(handle))
print(type(handle_old))
print(type(handle_new))
print("Output of random choice sandwich")
sh1 = [random.choice(handle)]
print(sh1)
print("condition output to be rid of braces and quotes")
print(*sh1, sep=", ")
print("condition output to be ready to remove it from original list via slice")
sh2 = str(sh1)[2:-0]
print(sh2)

for sh2 in handle_old:
    #slice to remove option from list
    handle_test = handle_old.remove(sh2)
print(handle_old)
print(handle_new)
print(handle)
print(handle_test)




print("")
print("Enjoy")
print("")
