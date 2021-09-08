#pizza calculator

#smal is 5$
#medium is $8
#large is $13print

print("...........................")
print("small pizza kost $ 5 ")
print("medium pizza kost $ 8 ")
print("large pizza kost $13 ")
print(".................................")

pizzasmall=int(input("hoeveel small pizza wil je "))
pizzamedium=int(input("hoeveel medium pizza wil je "))
pizzalarge=int(input("hoeveel large pizza wil je "))


prijssmall=(pizzasmall * 5)
prijsmedium=(pizzamedium * 8)
prijslarge=(pizzalarge * 13)

print("de prijs is dan " + str(prijssmall + prijsmedium + prijslarge) + " euro")


