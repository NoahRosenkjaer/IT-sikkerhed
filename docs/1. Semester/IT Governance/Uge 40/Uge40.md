# Risikostyring

!!! note "Overordnede læringsmål fra studie ordningen"

    **Viden**

    Den studerende har viden om og forståelse for:

    - Principper indenfor it-sikkerhed
    - Risikoanalyse
    - Standarder og organisationer i sikkerhedsarbejdet
    - Trusler og trusselsbilledet
    - Operationelle overvejelser for it-sikkerhed

    **Færdigheder**

    Den studerende kan:

    - Foretage risikovurdering af mindre systemer/virksomheder, herunder datasikkerhed
    - Vurdere hvilke sikkerhedsprincipper, der skal anvendes i forhold til en given kontekst.

    **Kompetencer**

    Den studerende kan:

    - Håndtere analyser om, hvilke sikkerhedstrusler der aktuelt skal behandles i et konkret it-system.

!!! note "Forberedelse"

    - Læs [Guide til risikostyring (Dansk Standard DS/INF 10017:2023)](guide-til-risikostyring-dansk-standard.pdf)

## Opgave - Risikostyring: Overblik

!!! note "Opgave beskrivelse"


    1. Lav et fælles dokument i deler i gruppen.
    1. Beskriv et virksomhedseksempel. Det må meget gerne være en virksomhed i kender i forvejen, hvis det ikke er muligt er det fint at konstruere en virkomhed. Uanset hvad i vælger skal i tage nedenstående parametre med når i beskriver virksomheden.
        En mere detaljeret beskrivelse af parametrene kan i læse i kapitel 2 i
        Guide til risikostyring (Dansk Standard DS/INF 10017:2023)
        Figur 1 (side 11) i vejledningen giver 3 eksempler på virksomhedseksempler.
        - digitalisering af virksomheden
        - fortrolighed af data anvendt i virksomheden
        - virksomhedens placering i leverandørhierarkiet
        - antallet af brugere.


Lille webshop, bogbutik

- Digitalisering af virksomheden
    - Online webshop med 100% digitalisering 
- Fortrolighed af data anvendt i virksomheden
    - Informationer om kunden bliver ikke liggende hos virksomheden, betalingsinformationer bliver håndteret af betalingsvinduet, og leveringsoplysninger givet videre til fragtfirmaet.
    - Nogen grad af fortrolige data, mht betalingsinformationer og leveringsadresse
-  placering i leverandør hierarkiet
    - Benytter sig i høj grad af leverandører i forhold til IT-driften.
    - IT er cloudbaserede løsninger, og et eks ternt webbureau har ansvaret for driften af webshoppen
- Antallet af brugere.
    - Mange brugere af webshoppen, nok til at outsourcing af it-drift, er en nødvendighed.
- Hændelsebaseret tilgang 
    - Der anvendes trusselskataloget fra sikkerdigital.dk

## Opgave - Risikostyring: Etablering af kontekst

!!! note "Opgave beskrivelse"


    1. Etabler en kontekst for jeres virksomhed, brug information og eksempler på side 13-18 i Guide til risikostyring (Dansk Standard DS/INF 10017:2023)
    Jeres kontekst skal indeholde:
        - Virksomhedens karateristika
        - Identifikation af iteressentlandskabet og interessenters forventninger
        - Identifikation af forretningsprocesser
        - Tilgang til at udregne risiko (kvantitativ eller kvalitativ)
        - Fastsættelse af niveauer for konsekvens og sandsynlighed og hvad de betyder.
        - Hvornår kan en risiko accepteres?
        - Definition af kriterier for risikoejer
    1. Beskriv konteksten på samme måde som eksemplerne på side 16-18 i Guide til risikostyring (Dansk Standard DS/INF 10017:2023)
        Det er vigtigt at i konstruerer tabeller for Konsekvens og sandsynlighed samt opstiller disse i en risiko matrix som for eksempel tabel A3, B3 eller C3. Skalaerne for hhv. sandsynlighed og konsekvens skal vælges ud fra jeres tilgang til at udregne risiko.

- Virksomhedens karateristika
    - Strategi: Vores webshop outsourcer, for at mindske kravet for egne ansatte, lager, drift af webshoppen osv. 
    - Mål: At sælge bøger.
    - Mission: Tilbyde et udvalg af bøger der inspirerer til større læseglæde
- Identifikation af iteressentlandskabet og interessenters forventninger
    - Kunder
    - Leverandøre
    - Medier
    - Medarbejdere

- Identifikation af forretningsprocesser
    - Hvordan får vi kunder: 
        - Reklamering for webshop
        - Omtale, pga. god service.
    - Hvordan udføres arbejdet for kunden?
        - Vare(r) bestilles fra en leverandør, pakkes, og sendes videre til kunden
    - Hvordan faktureres kunden?
        - Kunder modtager faktura via mail.
    - Hvilke processer er kritiske for, at I som virksomhed kan fungere – både på kort og langt sigt?
        - Levering af bøger fra leverandør
        - Kunder 
        - Webshop tilgængelighed
        - leverandørenes service
        - GDPR
- Tilgang til at udregne risiko (kvantitativ eller kvalitativ)
    - Kvalitativ

- Fastsættelse af niveauer for konsekvens og sandsynlighed og hvad de betyder.

|Konsekvens|Lav|Middel|Høj|
|---|---|---|---|
|Beløb|0-25.000 kr.|25.001-200.000 kr.|200.001+ kr.|

|Sandsynlighed|Lav|Middel|Høj|
|---|---|---|---|
|Interval|’Forventer ikke, at det kan ske’|Kan ske inden for 2 år| Forventer, det sker mindst årligt|

|Konsekvens/Sandsynlighed|Lav|Middel|Høj|
|---|---|---|---|
|Lav|Lav/Lav|Middel/Lav|Høj/Lav|
|Middel|Lav/Middel|Middel/Middel|Høj/Middel|
|Høj|Lav/Høj|Middel/Høj|Høj/Høj|



- Hvornår kan en risiko accepteres?
    - Hvis sandsynligheden eller konsekvensen er lav
- Definition af kriterier for risikoejer
    - Risikoejeren skal have en position, der gør dem i stand til at udføre opgaven, og træffe informerede beslutninger

2. Beskriv konteksten i brød tekst

Webshoppen består af 4 personer og er 100% baseret på webshoppen, hvor alle ordrer behandles. Beskæftiger sig i nogen grad af fortrolige data, mht betalingsinformationer og leveringsadresse og er derfor underlagt GDPR lovgivning. Al IT er cloudbaserede løsninger hvilket også har ansvaret for driften af webshoppen. Risikoen er kvalitativ og baseres ud fra en høj/middel/lav sandsynlighed og risiko, alle risici som ligger i enten lav konsekvens eller sandsynlighed bliver accepteret, hvor middel/middel bliver vurderet løbende. 

|Konsekvens|Lav|Middel|Høj|
|---|---|---|---|
|Beløb|0-25.000 kr.|25.001-200.000 kr.|200.001+ kr.|

|Sandsynlighed|Lav|Middel|Høj|
|---|---|---|---|
|Interval|’Forventer ikke, at det kan ske’|Kan ske inden for 2 år| Forventer, det sker mindst årligt|

|Konsekvens/Sandsynlighed|Lav|Middel|Høj|
|---|---|---|---|
|Lav|Lav/Lav|Middel/Lav|Høj/Lav|
|Middel|Lav/Middel|Middel/Middel|Høj/Middel|
|Høj|Lav/Høj|Middel/Høj|Høj/Høj|

## Opgave - Risikostyring: Identifikation af risici

!!! note "Opgave beskrivelse"


    1. Brug information og eksempler på side 19-21 i Guide til risikostyring (Dansk Standard DS/INF 10017:2023) når i arbejder.
    1. Beslut om i vil anvende en hændelsesbaseret eller aktivbaseret tilgang til at identificere risici.
    1. Identificer mindst 3 risici i jeres virksomhed (meget gerne flere).
    1. Beskriv hvem der er ansvarlig for de enkelte risici, brug de ledelsestitler i arbejdede med i øvelse 2
    1. Lav en liste over identificerede risici med ejere tilknyttet.

1. Beslut om i vil anvende en hændelsesbaseret eller aktivbaseret tilgang til at identificere risici.
    - Hændelsesbaseret
1. Identificer mindst 3 risici i jeres virksomhed (meget gerne flere).
    1. Webshoppen er ude af drift i en længere periode
    1. Kunder har mistro til webshoppen
    1. Leverandører kan ikke levere(bøger, betalingsservice, webshop)

1. Beskriv hvem der er ansvarlig for de enkelte risici, brug de ledelsestitler i arbejdede med i øvelse 2
    - Da det er en lille virksomhed og en hændelsesbaseret tilgang, er risikovurderingen en uformel samtale der sker én gang om året

1. Lav en liste over identificerede risici med ejere tilknyttet.

|Risici|Ejer|
|---|---|
|Webshoppen er ude af drift i en længere periode |CEO|
|Kunder har mistro til webshoppen|CEO of Marketing|
|Leverandører kan ikke levere(bøger, betalingsservice, webshop)|CEO|

## Opgave - Risikostyring: Analyse af risici

!!! note "Opgave beskrivelse"

    1. Brug information og eksempler på side 22-23 i Guide til risikostyring (Dansk Standard DS/INF 10017:2023) når i arbejder.
    1. Tal i gruppen om hver af jeres identificerede risici og fastslå konsekvens samt sandsynlighedsniveau for hver risici.
    1. Beskriv hver risici på samme måde som eksemplerne i guiden (side 23)

- Tal i gruppen om hver af jeres identificerede risici og fastslå konsekvens samt sandsynlighedsniveau for hver risici.

- Webshoppen er ude af drift i en længere periode
    - Hvis webshoppen bliver utilgængelig i forbindelse med et DDoS-angreb, vurderer vi, at det vil koste virksomheden omkring 25.000 kr. om dagen i tabt omsætning
    - Vi sætter dette til Lav/Lav risiko, da webshoppen outsource it driften, og deres leverandør burde have DDOS-prevention. Så det kan godt være at nogen angriber websiden, men ikke nødvendigvis at det er et succesfuldt DDOS angreb.
- Kunder har mistro til webshoppen
    - Hvis kunder har mistro til webshoppen vurderer vi, at det vil koste virksomheden omkring 25.000 kr. om dagen i tabt omsætning, over længere periode
    - Dette har en Høj/Lav risiko, da konsekvensen er høj da det resultere i tab af kunder og derved kan driften af webshoppen ikke finansieres, men sandsynligheden er lav da servicen er pålidelig
- Leverandører kan ikke levere(bøger, betalingsservice, webshop)
    - Hvis leverandører kan ikke levere vurderer vi, at det vil koste virksomheden omkring 25.000 kr. om dagen i tabt omsætning, over længere periode
    - Dette har en Høj/Middel risiko, konsekvensen er høj da det vil påvirke driften af hele webshoppen, og sandsynligheden er middel da det er leverandørene til diverse services som webshoppen afhænger af, men har ingen direkte indflydelse på

- Beskriv hver risici på samme måde som eksemplerne i guiden (side 23)

Boghandlens webshop er essentiel for deres forretning, da alt indtægt for virksomheden kommer igennem den webshop. Hvis webshoppen bliver ramt af et DDOS-angreb og websiden bliver utilgængelig i en periode, vurdere vi at virksomheden vil miste omkring 25.000 kr. om dagen i tabt omsætning. Dog har virksomheden foranstaltninger i form af den service som den valgte webhost leverandørs (Såsom cloudflare) DDOS-prevention foranstaltninger. 

Web Shoppens kunder er 100% af virksomhedens indtægt, mistillid og mistro til virksomheden fra kundernes side, vil betyde mindre kunder og mindre indtægt. Sandsynligheden er lav da det ikke forventes at ske, fordi servicen er pålidelig og webshoppen har en god rating, så selvom konsekvensen er alvorlig, forbliver risikoen lav.

Webshoppen er afhængig af sine leverandøre så det er ude af vores kontrol hvis leverandørene bliver komprimeret. Sandsynligheden er middel fordi det er en udefrakommende faktor der ikke kan forebygges på, og konsekvensen er høj da webshoppen er afhængig af de samme leverandøre. 


## Opgave - Risikostyring: Evaluering af risici

!!! note "Opgave beskrivelse"

    1. Prioritér listen med risici i forhold til sandsynlighed og konsekvens med angivelse af niveau fra jeres risikomatrix.
    1. Opdel listen i de risici der kan accepteres (grøn) og de risici der bør nedbringes (gul og rød).
    1. Opdel de risici der bør nedbringes i hhv. risici der kan accepteres af produktejer og de risici der skal accepteres på direktionsniveau.

1. Prioritér listen med risici i forhold til sandsynlighed og konsekvens med angivelse af niveau fra jeres risikomatrix.
    1. Webshoppen er ude af drift i en længere periode
    1. Leverandører kan ikke levere(bøger, betalingsservice, webshop)
    1. Kunder har mistro til webshoppen

1. Opdel listen i de risici der kan accepteres (grøn) og de risici der bør nedbringes (gul og rød).
    1. RØD: Webshoppen er ude af drift i en længere periode
    1. GUL: Leverandører kan ikke levere(bøger, betalingsservice, webshop)
    1. GRØN: Kunder har mistro til webshoppen



        Vi har lavet denne prioritering og opdeling af vores 3 identificeret risici, baseret på at, hvis en gruppe af kunder mister tillid til boghandlen og stopper med at være kunde, så vil det ikke være så stort et hit på virksomheden, som at Blive ramt af en succesfuldt DDOS-angreb, eller at en leverandør ikke kan levere ordentligt, hvor alle kunder vil blive påvirket. Der ud over er det en mulighed at finde nye og andre leverandører, hvis en leverandør ikke ender med at leve op til kravene.

1. Opdel de risici der bør nedbringes i hhv. risici der kan accepteres af produktejer og de risici der skal accepteres på direktionsniveau.

    - Accepteres af produktejer (risikoejer)
        - Kunder har mistro til webshoppen
        - Leverandører kan ikke levere(bøger, betalingsservice, webshop)
            - I første omgang, hvis denne forekommer i næste iteration, skal den afleveres til topledelse.
    - Accepteres på direktionsniveau (topledelsen)
        - Webshoppen er ude af drift i en længere periode

## Opgave - Risikostyring: Håndtering af risici

!!! note "Opgave beskrivelse"


    1. For hver risici der skal håndteres vælger i hvordan det skal udføres (accepteres, undgås, flyttes/deles, forøges/minimeres)
    1. For hver risici udvælger i foranstaltninger der understøtter håndteringen ud fra listen af foranstaltninger i ISO/IEC 27002:2022.
    1. Beskriv jeres håndtering af de enkelte risici, i kan bruge eksemplerne i guiden som inspiration (side 28)

1. For hver risici der skal håndteres vælger i hvordan det skal udføres (accepteres, undgås, flyttes/deles, forøges/minimeres)
    1. Webshoppen er ude af drift i en længere periode
        1. Denne minimeres ved hjælp af website drifts udbyder, som fx. cloudflare med dered DDOS-prevention.
    1. Leverandører kan ikke levere(bøger, betalingsservice, webshop)
        1. Hvis der er en leverandør der ikke kan levere, er der lavet en backup i form af en liste af andre leverandøre der kan levere samme produkt, i tilfælde af den første fejler
1. For hver risici udvælger i foranstaltninger der understøtter håndteringen ud fra listen af foranstaltninger i ISO/IEC 27002:2022.

    - Webshoppen er ude af drift i en længere periode
        - 5.22: Overvågning, vurdering og ændringsstyring af leverandørydelser
        - 5.29 Informationssikkerhed under driftsforstyrrelse
        - 5.23 Informationssikkerhed ved brug af cloudtjenester
        - 8.16 Overvågning af aktiviteter
        - 8.30 Outsourcet udvikling
    - Leverandører kan ikke levere(bøger, betalingsservice, webshop)
        - 5.22: Overvågning, vurdering og ændringsstyring af leverandørydelser
        - 5.29 Informationssikkerhed under driftsforstyrrelse


1. Beskriv jeres håndtering af de enkelte risici, i kan bruge eksemplerne i guiden som inspiration (side 28)

    - Webshoppen er ude af drift i en længere periode
        - For at undgå at webshoppen er ude af drfit i en længere periode udføres der godkendelsestest af kvaliteten af de outsouret IT tjenester
        - Der foretages overvågning af ændringer foretaget af leverandøren, herunder ændringer og opdateringer til systemer
        - Der vurderes servicerapporter udarbejdet af leverandøren og aftalt regelmæssige statusmøder i henhold til aftalerne
    - Leverandører kan ikke levere(bøger, betalingsservice, webshop)
        - Organisationen bør regelmæssigt overvåge, vurdere, evaluere og styre ændringer i leverandørers informationssikkerhedspraksis og levering af ydelser.
        - Der sikres, at leverandøren fastholder tilstrækkelig kapacitet for ydelsen tillige med realistiske planer, som skal sikre, at det aftalte niveau for ydelsen opretholdes efter et alvorligt nedbrud eller en katastrofe
        - Det sikres at leverandører opretholder de krav der stilles til dem 
