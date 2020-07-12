amount = float(input(" please enter a non negative amount " ))
while amount<0:
  amount = float(input(" please enter a non negative amount " ))

#print ("good to go")
cents = round(amount * 100)
#print (RoundedRealAmount)
coins = 0
pennys = [25,10,5,1]

for count in pennys:
    while cents >= count:
        cents = cents - count
        coins = coins + 1
print (coins) 

