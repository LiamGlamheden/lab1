storlek = float(input("Ange filens storlek i gigabyte: "))
bandbredd = float(input("Ange nätverkets bandbredd i megabit per sekund: "))

tidSek = (storlek * 1000 * 8) / bandbredd
tidMin = tidSek / 60

tidSek = round(tidSek, 1)
tidMin = round(tidMin, 2)

print("Överföringstid i sekunder:", tidSek) 
print("Överföringstid i minuter:", tidMin)