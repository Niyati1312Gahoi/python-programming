#program to find the total number of currency notes of each type (Rs 2000,Rs500,Rs100,Rs200)
#when the total number of currency notes counted altogrther is minimum and there  must be at
#least a 100 rupee note dispensed .the amount to be withdraw is tobe entered by the user

#input section
amt=eval(input("entre the amount required two we withdraw "))
# logic section
amt=amt-200
twok=amt//2000
amt=amt%2000
fiveh=amt//500
amt=amt%500
twoh=amt//200+1
amt=amt%200
oneh=amt//100




#output section
print(f'no.of 100 notes {oneh}')
print(f'no.of 200 notes {twoh}')
print(f'no.of 500 notes {fiveh}')
print(f'no.of 2000 notes {twok}')


