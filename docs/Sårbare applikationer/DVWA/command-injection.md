# Command Injection

Command Injection sårbarheden giver lidt sig selv, men kort sagt sker det når en applikation eksikvere kode på baggrund af bruger input. I dette eksempel er det en applikation, som en bruger kan bruge til at pinge en IP addrese med 4 ICMP (Ping protokol) pakker. Her giver applikationen brugeren mulighed for at eksikvere kommandoer i den shell som ligger bag applikationen.

![alt text](image-12.png)

Hvis man ved noget om kommandoer i for eksempel **Linux** så ved man måske at man kan bruge `;` eller `&&` til at køre flere kommandoer på en linje.

Når vi som bruger skiver en IP ind i feltet appender applikationen den IP bag på en ping commando. den fulde ping kommande burde se sådan ud: `ping -c 4 <IP>`, hvor `<IP>` er det vi skriver ind i feltet.

Med dette i tankerne, prøver jeg at skrive dette i feltet: `8.8.8.8; whoami`. Det resultere i at jeg får brugeren på systemet tilbage efter ping kommandoen. Dette vil sige at applikationen er sårbar for command injection angreb.

![alt text](image-13.png)

