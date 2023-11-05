import time

print('')
print('')
print('This is a program designed to help you breathe in and breathe out slowly')
print('Breathe in for abour five seconds and then breathe out for the same')
print('')
print('')
print('')
print('For a count of 13 breaths....')

# assign variable for breathe in = breathe_in
# assign variable for breathe out = breathe_out
# assign variable for breathe count
# assign variable for breath max

breathe_in = 'breathe in'
breathe_out = 'breathe out'
max_breath = 13
breath_count = 1

while breath_count <= max_breath:
	print(breathe_in, breath_count)
	time.sleep(5)
	print(breathe_out)
	time.sleep(5)
	
	breath_count += 1
	end = " "

