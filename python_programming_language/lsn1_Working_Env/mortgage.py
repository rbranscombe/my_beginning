#mortgage.py
#
#Find out how long i talkes to pay off a mortgage

#store values

principal = 500000
payment = 2684.11
rate = 0.05
total_paid = 0

#Extra payment infor
extra_payment = 1000
extra_payment_start_month = 1
extra_payment_stop_month = 60
month = 0

#add code to print to output file
fileout = open('schedule.txt', 'w') #open file for writing

#modify print statement to write data to fileout
print('{:>5s} {:>10s} {:>10s} {:>10s}'.format('Month', 'Interest', 'Principal', 'Remaining'),file=fileout)
while principal >0:
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_stop_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    interest = principal*(rate/12)
    principal = principal + interest - total_payment
    total_paid += total_payment
    #print a table showing unformatted data - month, interest, amount of payment on principal, principal remaining)
   # print(month, interest, total_payment - interest, principal)

   #add formatting
    print('{:>5d} {:>10.2f} {:>10.2f} {:> 10.2f}'.format(month, interest, total_payment - interest, principal), file=fileout)

fileout.close()    
print('Total paid:', '{:>10.2f}'.format(total_paid))
