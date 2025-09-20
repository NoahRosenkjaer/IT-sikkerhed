## Honeypots

En honeypot er en virtuel maskine, hvis eneste formål er at vildlede en angriber.
Når en angriber får adgang til honeypot-maskinen, tror vedkommende måske, at det er en legitim kontorcomputer, men den er lavet så sikkerhedsteamet kan analysere de teknikker angriberen bruger, og måske finde ud af hvad angriberen er ude efter.

Oftest er angriberen også en maskine, der bare udfører automatisk rekognoscering, og nu bruger de deres tid på at forsøge at udnytte et system, der faktisk ikke er en del af virksomhedens produktion.

Nu er en lille kamp mellem sikkerhedsteamet og angriberen begyndt. Angriberen forsøger at finde ud af, om de er fanget i en honeypot eller ej, og sikkerhedsteamet laver flere og gør dem mere komplekse, efterhånden som angriberen bliver bedre til at identificere honeypots.

## Honeynets

Det er almindeligt at lave mange honeypots og forbinde dem til et »rigtigt« netværk, kaldet et honeynet. Et honeynet er et helt netværk af honeypots, der arbejder sammen for yderligere at vildlede angriberen. Et honeynet kan omfatte servere, arbejdsstationer, routere, switche, firewalls og mere. Dette gør det lettere at afgøre, hvad angriberen er ude efter, for hvis angriberen bliver ved med at forsøge at få adgang til honey-serveren, er det sandsynligvis også det, han er ude efter i det rigtige virksomhedsnetværk.

## Honeyfiles

Honeyfiles er ligesom honeypots, men for filer. Lad os sige, at angriberen fik adgang til serveren, hvor filen passwords.txt med falske adgangskoder var gemt. Angriberen vil muligvis finde denne fil meget værdifuld og bruge meget tid på at gennemgå den for at finde adgangskoder, der fungerer på andre systemer.  

Det er god praksis at have en form for alarm, når nogen får adgang til en honeypot eller honeyfile.

## Honeytokens

Honeytokens er igen ligesom de andre, idet de er falske og lavet for at vildlede indtrængende. Det er sporbare data, der kan findes i filen passwords.txt på serveren, og når data stjæles fra honeynet og placeres på internettet, ved du, hvor de kommer fra.

Dette kan omfatte:
- Falske API-legitimationsoplysninger
    - Som ikke giver adgang til noget
    - Men en alarm som f.eks. en notifikation udløses, når de bruges

- Falske e-mailadresser
    - Føj dem til en kontaktliste
    - Overvåg internettet for at se, hvem der poster/bruger dem

Generelt kan disse tokens være enhver type data, der kan forfalskes. 