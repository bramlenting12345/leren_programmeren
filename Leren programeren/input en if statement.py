
j = "ja"# andwoord ja
n = ('nee')#andwoord nee

Vraag_1 = ('Is de kaas geel? (ja / nee) ')                                    # vraag 1
vraag_2 = ('zitten er gaten in de kaas ( ja / nee )')                         # vraag 2
vraag_3 = ('heeft de kaas blauwe schimels ( ja / nee ) ')                     # vraag 3
vraag_4 = ('heeft de kaas een korts ( ja / nee ) ')                           # vraag 4
vraag_5 = ('is de kaas belachelijk duur ( ja / nee )')                        # vraag 5
vraag_6 = ('is de kaas hard als steen ( ja / nee ) ')   
vraag_7 = ('heeft de kaas een korst ( ja / nee )')                                                                               

g  = ('gamebert')                                                            # andwoord 1
h  = ('mozzarella')                                                          # andwoord 2
i  = ('emmenthaler')                                                         # andwoord 3
k  = ('leerdammer ')                                                         # andwoord 4
l  = ('pamigano-regiano')                                                    # andwoord 5
m  = ('goudse kaas')                                                         # andwoord 6
o  = ('bleu-de-rochbarron ')                                                 # andwoord 7
p  = ('foume- d,ambert ')                                                    # andwoord 8

antwoord_1=input(Vraag_1)
if antwoord_1=="ja":
    antwoord_2=input(vraag_2)
    if antwoord_2 == "ja":    
        antwoord_5=input(vraag_5)
        if antwoord_5=="ja":
            print(i)
        else:           
            print(k)

    
              
    else:   
        antwoord_6 = input(vraag_6)
        if antwoord_6 == "ja":
            print(l)
        else:
            print(m)

else:
    antwoord_3 = input(vraag_3)
    if antwoord_3=="ja":
        antwoord_4=input(vraag_4)
        if  antwoord_4=="ja":
            print(o)
        else:
            print(p)
    else:
        antwoord_7= input(vraag_7)
        if antwoord_7 =="ja":
            print(g)
        else:
            print(h)

            
            
input("Druk op enter om af te sluiten")