# System & sikkerheds mål, samt ASP .Net core

!!! note "Læringsmål"

    **Viden**

    - Hvilken betydning programkvalitet har for it-sikkerhed.
    - Trusler mod software.
    - Kriterier for programkvalitet.
    - Forståelse for security design principles.

!!! note "Praktiske mål"

    - Den studerende kan udarbejde system mål.
    - Den studerende kan anvende CIA modellen til at udlede sikkerheds mål fra system mål.
    - Den studerende har grundlæggende forståelse for ASP .Net core.

!!! note "Forberedelse"

    - Læs dokumentet ”Introduktion til Sikker software udvikling- Del 1”.
    - Læs dokumentet ”Introduktion til Sikker software udvikling- Del 2”.
    - Bemærk at brugstilfælde/system mål skrives ud fra det forretningsmæssige formål,
    - altså de viser hvordan systemet kan skabe værdi for foretningen. 
    - Læs dokumentet ”Introduktion til Sikker software udvikling- Del 3”.
    - Bemærk at sikkerhedes målene ikke skrives ud fra tekniske specifikationer, men udfra hvad der kan skade forretningen som software systemet understøtter.
    - Læs kapitel 1 i bogen “Secure by design”. 
    - Læs Netcompany GDPR bøde
    
        Beskrivelsen viser et tilfælde hvor der opstår uhensigtmæssig implementering, tiltrods for at der i systemets brugstilfælde er en (efter datatilsynets vudering) åbenlys risiko (Misbrugstilfælde). Datatilsynet vurder også at den uhensigtsmæssige implementering kunne være undgået ved at anvendelse af privacy by design principper (som egentlig høre under security by design)

!!! note "Reflektions punkter efter forberedelsen"

    - Hvad er læren fra Öst-Götha Bank røveriet?
        
        (Tænk security in depth)
    - Bør sikkerhed tænkes ind i software design/udvikling som en selvstændig Feature?
    - Hvilket type angreb er XSS overordnet? (Listing 1.1 viser en klasse som er sårbar overfor dette)
    - Hvad er samhængen mellem security in depth og software design?
    - Hvad er forskellen på en use case , og et use case diagram?

## Opgave - Fælles forståelse af system- og sikkerhedsmål

!!! note "Opgave brskrivelse"

    1. Hvad kan vi lære af Öst-Götha Bank-røveriet?

        - Hvilke sikkerhedsmæssige principper blev ignoreret?

        "The system was designed without considering that insiders might abuse their access, even though real-world banking systems do not trust employees unconditionally."

    2. Bør sikkerhed integreres som en selvstændig feature i softwareudvikling?
    
        - Hvorfor / hvorfor ikke?

        "Security is not a feature – it’s a property of the entire system."

    3. Hvorfor er det vigtigt at kende systemmålene, når sikkerhed skal indtænkes?
    
        - Hvad risikerer man, hvis man ikke har styr på mål og kontekst?

        "Det er nødvendigt at forstå, hvad systemet skal kunne og beskytte, for at kunne vurdere hvilke trusler der er relevante."

    4. Hvilket abstraktionsniveau bør systemmålene have?

        - Hvor detaljerede bør de være – og hvorfor?

        "Systemmål bør være formuleret med et klart sprog, så de kan danne grundlag for en fælles forståelse med alle intressenter."

    5. Hvorfor er det en fordel at udlede sikkerhedsmål ud fra systemmålene?
    
        - Hvordan hænger det sammen med risikobaseret sikkerhed?

        "Et sikkerhedsmål er en negation af et systemmål – noget vi ikke vil have sker."



1. Hvad kan vi lære af Öst-Götha Bank-røveriet? Hvilke sikkerhedsmæssige principper blev ignoreret?
    - Sikkerhed skal dække alle “dele”
    - Man kan ikke komme på kompromi med sikkerhed
2. Bør sikkerhed integreres som en selvstændig feature i softwareudvikling? Hvorfor / hvorfor ikke?
    - Nej det skal det ikke. Det skal være en skal af processen (secure by design)
3. Hvorfor er det vigtigt at kende systemmålene, når sikkerhed skal indtænkes? Hvad risikerer man, hvis man ikke har styr på mål og kontekst?
    - Fordi forretningen kommer først. Hvis man ikke tænker system målene ind, så “glemmer” man den forretningsmæssige mål
    - Så ved man hvor man skal lægge sin energi.
4. Hvilket abstraktionsniveau bør systemmålene have? Hvor detaljerede bør de være – og hvorfor?
    - De skal være så abstrakte at de ikke-tekniske også kan læse det
    - Så højt så alle forstår det.
5. Hvorfor er det en fordel at udlede sikkerhedsmål ud fra systemmålene? Hvordan hænger det sammen med risikobaseret sikkerhed?
    - Det skal give værdi for forretningen.
    - Vi skal vide hvad vi passer på.


### Metodisk overblik – sådan hænger det hele sammen

Denne øvelse ligger i starten af en metode, som vi skal bruge i analysen af vores eksamensprojekt. Metoden ser sådan ud:

```linenums="0"
🎯 Systemmål  
   ↓  
🔐 Sikkerhedsmål (= misbrug)  
   ↓  
⚖️ Risikovurdering  
   ↓  
🕵️ Trusselsmodellering (STRIDE)  
   ↓  
🛡️ Valg af foranstaltninger  
     – ASVS  
     – Secure by Design  
     – Kodepraksis og CI/CD-sikkerhed  
     – Understøttet af ISO/IEC 27002:2022 kap. 8.25–8.31  
   ↓  
🧱 Design og implementering  
   ↓  
🔍 Verifikation (ASVS 5.0.0)
```

## Opgave - Udarbejdelse af systemmål for borger.dk

!!! note "Opgave beskrivelse"

    1. Besøg [borger.dk](https://www.borger.dk/)
    2. Vælg en kontekst, fx en aktør, I vil fokusere på
    3. Definér minimum 3 systemmål med tilhørende brugstilfælde – brug forberedelsen som vejledning
    4. Udarbejd et brugstilfældediagram – brug forberedelsen som vejledning

2. Vælg en kontekst, fx en aktør, I vil fokusere på
    - Vi valgte at fokusere på en lønmodtager som bestiller feriepenge.
    - Der kan også komme andre aktøre
3. Definér minimum 3 systemmål med tilhørende brugstilfælde – brug forberedelsen som vejledning
    1. systemmål 1: 
        - Aktør: Lønmodtager
        - Brugstilfælde: Lønmodtager bestiller feriepenge
        - Forudsætning: Lønmodtager har logget ind med MitID

            Lønmodtageren går på borger.dk og logger ind. Derefter bestiller lønmodtageren feriepenge for det ønskede arbejde.

    2. Systemmål 2:
        - Aktør: Medarbejder hos borger.dk
        - Brugstilfælde: Feriepenge bliver udbetalt til lønmodtager
        - Forudsætning: Lønmodtager har bestilt feriepenge
            
            Medarbejder i borger.dk godkender bestilling af feriepenge

    3. Systemmål 3:
        - Aktør: Lønmodtager
        - Brugstilfælde: Lønmodtager modtager løn
        - Forudsætning: Lønmodtagers kontonummer har integritet og er uændret

            Lønmodtager går ind på feriepenge website og tjekker 
Arbejdsgiver sender lønseddel til borger.dk

4. Udarbejd et brugstilfældediagram – brug forberedelsen som vejledning

    ![brugstilfældediagram](brugstilfældediagram.png)

## Opgave - Udarbejdelse af sikkerhedsmål for borger.dk

!!! note "Opgave beskrivelse"

    **Brainstorm misbrugstilfælde**

    - Gennemgå brugstilfældediagrammet fra forrige øvelse.
    - Identificer mulige misbrugstilfælde, hvor systemet kan blive udnyttet til skade for forretningen(CIA).
    - Påtegn misbrugstilfælde på diagrammet løbende.
    - Se eksemplet fra dagens forberedelse som vejledning.

    **Udarbejd sikkerhedsmål**

    - Formulér minimum 1 misbrugstilfælde baseret på det identificerede brugstilfælde på diagrammet.
    - Anvend CIA-modellen til at sikre, at sikkerhedsmålene dækker fortrolighed, integritet og tilgængelighed, hvor relevant.
    - Se eksemplet fra dagens forberedelse som vejledning.


1. Formulér minimum 1 misbrugstilfælde baseret på det identificerede brugstilfælde på diagrammet.

    Sikkerhedsmål:

    - Misbrugstilfælde: Lønmodtager bestiller flere feriepenge end der er til rådighed eller bestiller flere gange.
    - Aktør: Ondsindet lønmodtager
    - Tilknyttede brugstilfælde nr. 1
    - Forudsætning: Aktøren kan overtrække mængden af feriepenge bestilt

        Den kriminelle manipulere bestillingen, og bestiller flere feriepenge end til stede på hans/hendes konto

2. Anvend CIA-modellen til at sikre, at sikkerhedsmålene dækker fortrolighed, integritet og tilgængelighed, hvor relevant.

    Ved at bruge CIA modellen er vi kommet frem til en prioiteret af de tre katagorier.

    1. Integitet
        - Denne mener vi er mest vigtig da ænding eller tilintetgørelse af en borgers feriepenge eller data vil være worst case.
    2. Tilgængelighed
        - Denne er nummer to da den også er megte vigtig, men man kan godt overleve hvis borger.dk bliver DDOS'et da man også kan hente feriepenge efter sin ferie. Så man kan vente til borger.dk er oppe igen.
    3. Fortrolighed
        - Denne er også meget vigtig, men det er ikke verdens undergang hvis fortroligheden af antallet af feriepenge man kan få udbetalt bliver brudt.

3. Påtegn misbrugstilfælde på diagrammet løbende.

    - Her er et misbrugstilfældediagram:
        ![misbrugstilfældediagram](brugstilfældediagram2.png)

## Opgave - Opret en applikation med ASP.NET Core

!!! note "Opgave beskrivelse"

    - Gennemfør [tutorialen](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-web-api?view=aspnetcore-9.0&tabs=visual-studio-code) og implementer API’et.
    - Brug læseguiden nedenfor til at reflektere over nøglebegreber i hvert afsnit.
    - Vi gennemgår applikationen sammen i næste undervisningsgang.

Her er refleksionspunkter over tutorialen:

**Overview**

- Beskrivelse af API’ets URL paths og arkitektur.
    - `/api/TodoItems`
        - `POST`: Med `POST` på dette API endpoint kan man insette et nyt todo item
        - `GET`: Med `Get` kan man få alle todo items
    - `/api/TodoItems/{id}`
        - `GET`: Med `Get` kan man få et enkelt specifikt item per ID
        - `PUT`: Med `PUT` kan man opdatere items.
        - `DELETE`: Med `DELETE` kan man fjerne items igen.
- "Client" refererer til en anden applikation, som kommunikerer med API’et.

**Add a model class**
- Overvej hvordan objekter kan oprettes uden konstruktør eller andre begrænsninger.
    - Det er fordi de i TodoItems.cs er sat til at være public.

**Controllerens rolle og ansvar**

- Hvad er controller-klassens funktion i applikationen?
    - Det er at håntere HTTP methods, som POST, GET osv.
- Hvordan fungerer den som bindeled mellem klienten og applikationens data?
    - Den håntere hvad der skal ske med dataen beseret på hvilken method den får.
- Hvilken betydning har [HttpGet], [HttpPost] og andre attributter for controllerens opførsel?
    - Alt. De definere hvordan den håntere henholdsvist GET og POST.
    - Controlleren håndterer udefrakommende HTTP-requests. 