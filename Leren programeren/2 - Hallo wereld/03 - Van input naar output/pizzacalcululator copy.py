#pizza calculator

#smal is 5$
#medium is $8
#large is $13print


menu="""-------------------------------------------
Small pizza kost    5   euro
Medium pizza kost   8   euro
Large pizza kost    13  euro
----------------------------------------------------
"""
print (menu)

pizzasmall=int(input("hoeveel small pizza wil je "))
pizzamedium=int(input("hoeveel medium pizza wil je "))
pizzalarge=int(input("hoeveel large pizza wil je "))
print ("------------------------------------------------")

prijssmall=(pizzasmall * 5)
prijsmedium=(pizzamedium * 8)
prijslarge=(pizzalarge * 13)

print("de prijs is dan " + str(prijssmall + prijsmedium + prijslarge) + " euro")


