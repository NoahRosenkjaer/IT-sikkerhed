# Brute force

Når man åbner Brute Force siden, bliver vi mødt med en simpel login side, der har to forms og en knap.

![alt text](image-7.png)

Hvis man prøver at logge ind med forkert bruger navn eller password skriver siden "Username and/or password incorrect."

![alt text](image-8.png)

Jeg skyder et skud i tågen, ved at lave et brute force angreb hvor jeg kun bruger admin som username. Til passwords bruger jeg rockyou.txt (en fil med 14344392 passwords). Jeg har valgt at bruge Caidos automate funktion til at brute force.

For at gør dette, opfanger jeg en `GET` efter at have prøvet at logge ind. 

![alt text](image-9.png)

Som det kan ses på billedet er `pass` markeret, i en lille orange boks. Dette betyder at `pass` nu er en placeholder, og når den er startet vil Caido gå igennem hele `rockyou.txt`, ved at sende en masse requests hvor `pass` bliver erstattet med en linje fra filen. 

På billedet her under ses Caidos automate i aktion.
![alt text](image-10.png)

Jeg stoppede mit brute force angreb tideligt, da Caido fandt det rigtige password. Det kan man se ud fra den responce **length** såm bliver vist. Alle de fejlede forsøg har en længde på `4666`. Forsøg nummer 4 prøver passworded `password` og får en anden længde end de andre. Derfor tester jeg om det kunne være den, og ganske rigtigt så er det den som er det rigtige password.

![alt text](image-11.png)