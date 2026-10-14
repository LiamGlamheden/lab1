platskod = input("Ange platskod: ")
enhetstyp = input("Ange enhetstyp: ")
senasteNumret = input("Ange senasteNumret: ")

nästaNummer = int(senasteNumret) + 1

platskod = platskod.lower()
enhetstyp = enhetstyp.lower()

nästaNummer = str(nästaNummer).zfill(2)

hostnamn = platskod + "-" + enhetstyp + "-" + nästaNummer

print("Nästa hostnamn:", hostnamn)