# Kryptering

Kryptering tager læsbar information (klartekst) og omdanner den ved hjælp af matematik og en kryptografisk nøgle (et kodeord) til ulæselig kryptotekst (eller chiffertekst)

## Symmetrisk kryptering

I symmetrisk kryptering genereres der kun en enkelt nøgle, og denne nøgle kan både kryptere og dekryptere de samme data. Dette ses typisk i film, hvor målet er at få fat i en kuffert, der er håndjernet til en bud. Hvis nøglen kommer ud, skal du bruge en anden nøgle. 

Denne type kryptering kan ikke skaleres særlig godt, for hvis 10 personer ønsker at have private krypterede chats med hinanden, skal de alle holde styr på, hvilken nøgle hver person bruger, og det bliver bare sværere derfra, for ikke at nævne, at hvis en af dem opfanger en krypteret besked, kan de også dekryptere den og se dataene.

I dag bruges symmetrisk kryptering stadig på trods af dens iboende mangler, fordi den er meget hurtig at bruge sammenlignet med asymmetrisk kryptering.
På grund af dette bruges de begge for at kompensere for deres individuelle mangler. SHH-protokollen bruger begge.

## Asymmetrisk kryptering

I modsætning til symmetrisk kryptering krypteres asymmetrisk kryptering med to forskellige nøgler. En privat og en offentlig.
Den private nøgle bruges til at dekryptere data, og den offentlige bruges til at kryptere disse data. Som navnet antyder, skal den private nøgle forblive privat, mens den offentlige nøgle frit kan gives videre. Da de to nøgler er matematisk forbundne, kan en person med din offentlige nøgle dekryptere alt, men kan ikke bruge den offentlige nøgle til at lave en kopi af din private nøgle.

## Nøgleparret
Asymmetrisk kryptering er også kendt som offentlig nøglekryptografi.

Når nøglerne genereres, laves de begge på samme tid ved hjælp af masser af randomisering, store primtal og masser af matematik.
Hvis min ven Jacob og jeg vil sende hinanden beskeder ved hjælp af offentlig nøglekryptografi, skal vi hver især lave et nøglepar. Derefter sender vi hinanden vores offentlige nøgler, og inden jeg sender ham en besked, krypterer jeg den ved hjælp af hans offentlige nøgle, og når han modtager den krypterede tekst (den krypterede besked), kan han dekryptere den med sin private nøgle og omvendt. Enhver, der har adgang til den krypterede tekst og den offentlige nøgle, har ingen mulighed for at finde ud af, hvad der er i den i teksten, de kan ikke reverse engineere den offentlige nøgle for at få den private nøgle.

## Nøgleudveksling
Hvordan sender du andre den nøgle, de har brug for til at dekryptere nogle data? Det er ikke en god idé at sende den via internettet, da andre kan opfange den og få adgang til dataene.

Du kan gøre det manuelt, over telefonen, ved hjælp af en kurér eller personligt.
På internettet kan du bruge yderligere kryptering ved at anvende asymmetrisk kryptering på en symmetrisk nøgle og derefter sende den asymmetrisk krypterede nøgle til en tredjepart, som kan dekryptere den for at få den symmetriske nøgle. Dette giver dig mulighed for at oprette sessionsnøgler.

### Kryptering/dekryptering i realtid

En klient kan kryptere en symmetrisk nøgle med en servers asymmetriske offentlige nøgle og sende den til serveren, hvorefter serveren dekrypterer den og bruger den til at kryptere data relateret til den pågældende klient. Dette er en sessionsnøgle.

### Symmetriske nøgler fra asymmetriske nøgler

Hvis Jacob og Noah ønsker at dele en symmetrisk nøgle, men ikke ønsker at sende den over netværket, kan de gøre det.
Hvis Jacob kombinerer sin private nøgle og Noahs offentlige nøgle og omvendt. De opretter hver især nøjagtig den samme symmetriske nøgle, fordi deres nøgler var matematisk relaterede.