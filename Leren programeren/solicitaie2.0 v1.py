print("vacature opleiding circus")
print("   ")

#vragen 

vraag_1 = ("ben u een man of vrouw ? :  ")
vraag_2 = ("heeft u meer dan 4 jaar praktijk ervaring ja / nee :  ")
vraag_4 = ("bent u is het bezit van een diploma in MBO 4 ondernemen? ja / nee :")
vraag_5 = ("bent u in het bezit van een vrachtwagen rijbewijs ja / nee : ")
vraag_6 = ("bent u in het bezit van een hoge hoed ja / nee : ")
vraag_7 = ("heeft u een snor ja / nee : ")
vraag_8 = ("heeft u rood krul haar ja / nee : ")
vraag_9 = ("hoe lang ben u in cm ? : ")
vraag_10 = ("hoeveel kilo gram weegt u ? : ")
vraag_11 = ("heeft u een certificaat overleven met gevaarlijk personeel ja / nee : ")

#antwoorden
ja = "ja"
nee = "nee"

man = ("man")
vrouw = ("vrouw")
a_1 = ("door u ingevuld antwoord = nee :  ")
a_2 = ("door u in gevulde antwoord = ja :")
a_3 = ("meer dan 4 jaar praktijk ervaring? ")
a_4 = ("ja ik heb praktijk ervaring")
a_5 = ("ja ik ben in  het bezit van een vrachtwagen rijbewijs ")
a_6 = ("nee ik ben niet in het bezit van een vrachtwagen rijbewijs ")
a_7 = ("is u snor grooter dan 10 cm ")
a_8 = ("snor niet breder dan 10 cm")
a_9 = ("snor breder dan 10 cm ")
a_10 = ("draagt rood krulhaar langer dan 20 cm ")
a_11 = ("draagt geen rood krul haar kosrten dan 20 cm ")
a_12 = ("is langer dan 150 cm ")
a_13 = ("is niet langer dan 150 cm")
a_14 = ("weegt meer dan 90 kg")
a_15 = ("weegt minder dan 90 kg ")
a_16 = ("heeft wel een cetificaat gevaarlijk personeel ")
a_17 = ("heeft geen cetificaat gevaarlijk personeel ")



antwoord_1=input(vraag_1)

if antwoord_1==(man):#------------------------Vragen voor de man---------------------------------
    
    antwoord_7=input(vraag_7)
    antwoord_4=input(vraag_4)
    antwoord_5=input(vraag_5)
    antwoord_10=input(vraag_10)
    antwoord_6=input(vraag_6)
    antwoord_9=input(vraag_9)
    antwoord_11=input(vraag_11)

    #------Weergeven uitslag gegevent vrouw ------------------------------------------------------------
    print("...........................................")
    print("hier door u ingevulde antwoorden ")
    print("  ")
    
    print("Ü ben een " , antwoord_1)
    
    if antwoord_7=="ja":
        print("U heeft een snor ")
    else:
        print("U heeft geen snor ")
    
    if antwoord_4=="ja":
        print(" U bent in  het bezit van een diploma in MBO 4 ondernemen")
    else:
        print("U bent niet in het bezit van een diploma in mbo 4 ondernemen ")  

    if antwoord_5=="ja":
        print("U bent in het bezit van een vrachtwagen rijbewijs ") 
    else:
        print("U bent niet in het bezit van een vrachtwagen rijbewijs ")   

    print("u weegt ", antwoord_10, " kg ")  

    if antwoord_6=="ja":
        print("u bent in het bezit van een hoge hoed ") 
    else:
        print("u bent niet in het bezit van een hoge hoed ")             

    print("u lengte is " , antwoord_9, " kg" )

    if antwoord_11=="ja":
        print("u heeft wel een certificaat gevaarlijk personeel ")
    else:
        print("u heeft geen certificaat gevaarlijk personeel ")    
    print("................................................................")


else:#-----------------------------Vragen voor de Vrouw----------------------------
    
    antwoord_8=input(vraag_8)
    antwoord_4=input(vraag_4)
    antwoord_5=input(vraag_5)
    antwoord_10=input(vraag_10)
    antwoord_6=input(vraag_6)
    antwoord_9=input(vraag_9)
    antwoord_11=input(vraag_11)
    #-----Weergeven uitslag gegevens vrouw--------------------------------------------

    print("................................................................")
    print("  ")
    print("hier door u ingevulde antwoorden ")


    print("Ü ben een " , antwoord_1)
    
    if antwoord_8=="ja":
        print("u heeft rood krulhaar  ")
    else:
        print("u heeft geen rood krulhaar ")
    
    if antwoord_4=="ja":
        print(" u bent in  het bezit van een diploma in MBO 4 ondernemen")
    else:
        print("u bent niet in het bezit van een diploma in mbo 4 ondernemen ")  

    if antwoord_5=="ja":
        print("U bent in het bezit van een vrachtwagen rijbewijs ") 
    else:
        print("U bent niet in het bezit van een vrachtwagen rijbewijs ")       

    print("u weegt ", antwoord_10, " kg ")    

    if antwoord_6=="ja":
        print("u bent in het bezit van een hoge hoed ") 
    else:
        print("u bent niet in het bezit van een hoge hoed ") 
    
    print("u lengte is " , antwoord_9, " kg" )

    if antwoord_11=="ja":
        print("u heeft wel een certificaat gevaarlijk personeel ")
    else:
        print("u heeft geen certificaat gevaarlijk personeel ")  

    print("............................................................................")


input("druk op enter om verder te gaan ")          

    





