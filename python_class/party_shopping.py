# This is a program that prompts a user to enter the number of guests expected at a party.
# In turn the program is written to calculate
# Print the number of packages of hotdog buns to order. 8 per pack 
# Prints the number of packages of hotdogs to order. 10 per pack
# Prints the number of fun pack chip boxes needed. 32 per pack
# Prints the number of drink 6-packs needed. 6 per pack


guests = int(input("How many guests are expected at your party? "))

#condition input to ensure -ve or non-zero value

if guests <= 0:
	print("Go on... go invite some friends to a party and then we can plan...") 

else:

#Initialise hot dog bun packages order
	hot_dog_buns_per_pack = 8
	hot_dog_bun_pack_float = guests / hot_dog_buns_per_pack

	hot_dog_bun_pack_int = int(hot_dog_bun_pack_float)
	hot_dog_bun_part_pack = hot_dog_bun_pack_float - hot_dog_bun_pack_int

	hot_dog_bun_pack_order = hot_dog_bun_pack_int
	if hot_dog_bun_part_pack > 0:
		hot_dog_bun_pack_order = hot_dog_bun_pack_order + 1

#print(type(hot_dog_buns_per_pack))
#print(type(hot_dog_bun_pack_order))
#print(type(hot_dog_bun_part_pack))
#print(f"{hot_dog_bun_part_pack}")
#print(f"{hot_dog_bun_pack_order}")

#initialise hot dog order

	hot_dogs_per_pack = 10
	hot_dog_pack_float = guests / hot_dogs_per_pack

	hot_dog_pack_int = int(hot_dog_pack_float)
	hot_dog_part_pack = hot_dog_pack_float - hot_dog_pack_int

	hot_dog_pack_order = hot_dog_pack_int
	if hot_dog_part_pack >0:
		hot_dog_pack_order = hot_dog_pack_order + 1


#print(type(hot_dogs_per_pack))
#print(type(hot_dog_pack_order))
#print(type(hot_dog_part_pack))
#print(f"{hot_dog_part_pack}")
#print(f"{hot_dog_pack_order}")


#initialise crisp packet data
	chip_boxes_per_pack = 32
	chip_boxes_float = guests / chip_boxes_per_pack

	chip_boxes_int = int(chip_boxes_float)
	chip_boxes_part_box = chip_boxes_float - chip_boxes_int

	chip_boxes_order = chip_boxes_int
	if chip_boxes_part_box >0:
		chip_boxes_order = chip_boxes_order + 1

#print(type(chip_boxes_per_pack))
#print(type(chip_boxes_order))
#print(type(chip_boxes_part_box))
#print(f"{chip_boxes_part_box}")
#print(f"{chip_boxes_order}")

#initiialis drink data
	drink_boxes_per_pack = 6 
	drink_packs_float = guests / drink_boxes_per_pack

	drink_packs_int = int(drink_packs_float)
	drink_packs_part_pack = drink_packs_float - drink_packs_int

	drink_packs_order = drink_packs_int
	if drink_packs_part_pack > 0:
		drink_packs_order = drink_packs_order +1


	print(f"Based on your guest tally of  {guests} guests: ")
	print(f"You will need to order {hot_dog_bun_pack_order} packages of  hotdog buns @ {hot_dog_buns_per_pack} per packs, ")
	print(f"order {hot_dog_pack_order} packages of hot dogs @ {hot_dogs_per_pack} per pack, ")
	print(f"order {chip_boxes_order} boxes of crisp packets -  assumming {chip_boxes_per_pack} packets per box, and ")
	print(f"order {drink_packs_order} packs of drinks @  {drink_boxes_per_pack}  per pack.")  
