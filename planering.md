# Lab 1 – Planering
## Problem 1
• Vad är indata?
Data som matas in av användaren, till exempel platskod (STO), enhetstyp (srv) och det senast använda numret (7).
• Vad är utdata?
Data som programmet visar, till exempel det nya hostnamnet (sto-srv-08).
• Vilka regler gäller? Tänk på små bokstäver, bindestreck och två siffror.
Hostnamnet ska bestå av en platskod, enhetstyp och ett tvåsiffrigt nummer. Allt ska skrivas med små bokstäver och delarna ska separeras med bindestreck.
• Vad kan gå fel?
Användaren kan mata in fel data, till exempel bokstäver i stället för ett nummer eller fel platskod och enhetstyp.

Planera:
1. LÄS IN platskod.
2. LÄS IN enhetstyp.
3. LÄS IN det senast använda numret.
4. BERÄKNA nästa nummer genom att öka det senaste numret med 1.
5. GÖR platskoden och enhetstypen till små bokstäver.
6. BERÄKNA hostnamnet genom att sätta ihop platskoden, enhetstypen och nästa nummer med bindestreck.
7. SKRIV UT nästa hostnamn.


Felmedelande TypeError: can only concatenate str (not "int") to str

svar:
Felet uppstår eftersom input() sparar inmatningen som text. Därför kan programmet inte addera texten med heltalet 1.

test:
| Platskod | Typ | Senaste nr | Förväntat  | Faktiskt | OK? |
|----------|-----|------------|------------|----------|-----|
| STO      | srv | 7          | sto-srv-08 | sto-srv-08   ja
| gbg      | SW  | 11         | gbg-sw-12  |  gbg-sw-12   ja
| sto      | srv | 0          | sto-srv-01 | sto-srv-01   ja
| mal      | pc  | 99         | ?mal-pc-100 | mal-pc-100  nej
| sto      | srv | sju        | ?  error    |   error    nej  

Vad händer med testet mal, pc, 99? Följer namnet fortfarande standarden? Vad borde företaget göra?

Numret går över till 100. Det följer inte standarden eftersom numret ska bestå av två siffror. Företaget borde bestämma vad som ska hända när numret går över 99.

Vilket fel ger det sista testet? Hur kan man förhindra sådana krascher?

Man kan använda en if-sats för att kontrollera att användaren matar in rätt data.



## Problem 2

 Kommer du ihåg från genomgången hur många bitar som går på en byte?
8 bitar.

## Problem 3
## Del 4: Från källkod till körning