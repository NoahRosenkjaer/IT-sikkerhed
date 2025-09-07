# Introduktion til faget

!!! note "Praktiske mål"
    - At alle studerende har installeret Burp suite
    - At alle studerende har installeret Postman
    - At alle studerende har installeret Docker
    - At alle studerende er bekendt med fagets læringsmål
    - At alle studerende er introduceret til OWASP Top 10
    - At alle studerende er introduceret til ASVS.

!!! note "Læringsmål"
    Viden
    
    - Den studerende har viden om typiske trusler og sårbarheder forbundet med webapplikationer og deres årsager.
    - Den studerende har viden om gængse standarder og rammeværk inden for webapplikationssikkerhed.
    - Den studerende har viden om metoder til vurdering og efterprøvning af sikkerhedsmæssige foranstaltninger.
    
    kompetence
    
    - Den studerende kan strukturere egen faglig udvikling inden for området og følge med i nye teknologier og trusselsbilleder.

!!! note "Forberedelse"
    - Læs kapitel 1 i bogen "Hacking APIs"
    - Læs kapitel 2 i bogen “Hacking APIs”

??? note "Reflektions punkter efter forberedelsen"

    **_Kapitel 1:_**

    - Hvordan er et HTTP request udformet?
        - Den består af:
            - Methods
            - Resources
            - Protocol + protocol version
            - Headers
            - Message body
    - Hvad er en HTTP metode(method)?
        - En methods er det der viser hvad en given request vil gøre. De kan blandt andet få, fjerne, ændre, sende information til web aplicationen.
    - Hvordan er et HTTP response udformet?
        - De minder om en request, men har ikke resources eller protocol og version. Dog har de status koder der viser hvordan web aplicationen har håndteret en request.
        - Den har message body alt efter hvilken method var brugt i requesten.
    - Hvad er HTTP status koder?
        - De viser hvordan web aplicationen har håndteret en request.
            - 100: Information-based responses
            - 200: Successful responses
            - 300: Redirects
            - 400: Client errors
            - 500: Server errors
    - Hvad er en API?
        - En API er en teknologi der gør det muligt at hente data fra andre stedet på nettet. Hvis jeg vil lave en vejr web app så kan jeg bare bruge DMI's API til at hente temperaturen, så jeg selv kan fokusere på andre dele af min egen app.
    - hvad er forskellen på stateful og stateless?
        - Stateful: Det er når en web application husker hvad min bruger har lavet, så den husker at jeg har sat 4 ting i min vogn på en shopping app. hvis jeg logger ind på en anden enhed.
        - Stateless: Her husker den ikke på samme måde, man kan de samme ting, men man skal sende alt det data serveren skal bruge for at authenticate en. Eller husker den det ikke.

    _**kapitel 2:**_

    - Hvad er et RESTful API? (REST API)?
        - Det er en API som bruger CRUD metoderne og overholder API naming conventions, tokens for authorization.
    - Hvad brugers headers til?
        - Authorization
            - Til at bevise at du er en bruger.
        - Content type
            - Til at bestemme hvliken type dataen kan/vil være.
            - Det kan være JSON, YAML, eller XML
    - Hvad bruges JSON til?
        - TIl at overføre data i en bestemt struktur som er let læsligt af mennesker, såvel som maskiner.
    - Hvad er basic authentication?
        - Det er username/id og et password.
    - Hvad er en API nøgle?
        - Det er en nøgle som er auto generated af API holderen. Og den skal sende med hverd API request.
    - Hvad er en JWT token?
        - JWT er en type af API nøgle. og den sender man i Authorization headeren i ens request.

## Installation af værktøjer

1. Installer Burp suite community edition: Install burp suite
Er allerede installeret i Kali Linux, men er også praktisk at havde i windows
2. Installer Postman Install postman
I behøver ikke at oprette en bruger for at bruge postman
3. Installer docker desktop Install Docker
4. Installer Kali linux WSL ved at følge guiden How to install Linux on Windows with WSL.(Distributions navnet du skal anvende er kali-linux)
Bemærk at du skal skifte distributionen til Kali Linux

### Opsætning af test miljø i docker
I denne øvelse skal der laves en opsætning med de sårbar applikationer du skal bruge som test miljø i undervisningen .

Docker-compose filen samt dokumentation kan findes her: [Link](https://github.com/mesn1985/HackerLab)

Gør følgende:

1. Klone repositoriet med git.
2. Følg instruktionerne for opsætningen i repositoriets README.md file.
3. Efter opsætningen test at du kan tilgå applikationerne,Juice shop og crAPI.
Portene hver applikation bruger kan du se i readme filen

## OPGAVE - OWASP Top 10: Injection Sårbarheder
### 1. forstå Injection Sårbarheder

!!! note "Opgave beskrivelse"
    Gå til [OWASP Top 10 Injection](https://owasp.org/Top10/A03_2021-Injection/#list-of-mapped-cwes) og læs beskrivelsen af injection-sårbarheder.
    Forklar med dine egne ord, hvad en injection-sårbarhed er, og hvordan den typisk kan udnyttes i webapplikationer. Giv eksempler på forskellige typer af injection-angreb, såsom SQL injection og command injection.

OWASP er en non-profit der prøver at hjælpe med at gøre sikkerhed i software bedre. De har lavet nogle guidelines og ressourcer, som man kan følge. Det er meget kendte for OWASP top 10 som er en liste over de mest sete sårberheder i web applikationer.

Injection rammer top 3 af sårbarheder, hvilket setter den højt med 3% af alle testede applicationer der var såbare for en form for injection angreb. De typer af injections includere Cross-site scriptign (XXS), SQL Injection (SQLI), og External Controll of File Name or Path.

Typisk er en applikation sårbar for injections når, der ikke er implamenteret korrekt sanitering, filtrering eller validering, af bruger input/data. Det vil sige at når en bruger søger efter noget i en applikation som bruger en SQL database, så kan de faktisk bruge SQL sproget til at enumerere rundt i databasen, da der ikke er noget der stopper brugeren. Det kan reusltere i at en bruger kan finde et table med usernames og passwords, som de ikke burde kunne få fat i.

Command injection er også en stor sårbarhed, da en applikation sårbar over for dette, vil give en bruger mulighed for at eksikvere komandoer. Dette er ikke godt at det giver en bruger mulighed for at gøre hvad de vil med servere, såsom at åbne og læse filer der kun er beregnet til admins/devs. Eller starte en reverse proxy, eller Remote Access Trodian (RAT)

### 2. Forståelse af Positive Server-Side Input Validation

!!! note "Opgave beskrivelse"
    Læs afsnittet How to Prevent på OWASP-siden om injection.
    Forklar, hvad der menes med "positive server-side input validation" som en metode til at forhindre injection-angreb. Hvorfor er denne metode effektiv, og hvordan adskiller den sig fra "negative validation" (sortlisting)?

Positive server-side input validering er det samme som white-listing/allow-list
Det er at man kun defindere hvad der er tilladt og blokere alt andet som standard. I modsætning til white-listing er der black-listing, som er når man kun defindere og blokere det som ikke er tilladt.
Når noget er server-side så er det noget der sker efter dataen er sendt, og det er servere selv der tjekker om noget data er tilladt eller ej. 

### 3. CWE-20 - Improper Input Validation

!!! note "Opgave beskrivelse"
    Find afsnittet List of Mapped CWEs på OWASP injection-siden og læs om CWE-20.
    Beskriv, hvad CWE-20 "Improper Input Validation" dækker over. Hvorfor er korrekt inputvalidering vigtig for applikationssikkerhed?

Det handler om hvordan input data skal håndteres, og det er vigtigt da svag eller ingen input validering vil resultere i en applikation der får sendt data den ikke er lavet til at håndtere, eller en bruger udnytter dette, til at få adgang til ting de ikke normalt har rettigheder til.

## Opgave - Insecure Design
### 1. Requirements and Resource Management

!!! note "Opgave beskrivelse"
    Læs afsnittet [Requirements and Resource Management](https://owasp.org/Top10/A04_2021-Insecure_Design/#requirements-and-resource-management) på OWASP-siden.
    Hvad beskrives der overordnet i dette afsnit, og kender du en tilgang, som dækker dele af det beskrevne?


Det beskriver at man skal snakke med det business der vil have lavet en applikation, spørg dem om hvilke krav de har, det skal inkludere krav om fortrolighed, integritet, tilgængelighed og ægthed af alle dataaktiver og den forventede business logic. Definer tekniske krav og planlæg en budget.

### 2. Forståelse af Secure Design

!!! note "Opgave beskrivelse"
    Hvad menes der med "Secure design"? Forklar begrebet, og hvordan det adskiller sig fra andre tilgange til sikkerhed i softwareudvikling.

Secure design er methodologi der overordnet handler om at producere kode med sikkerhed i tankerne, da det ofte er en eftertanke.

### 3. Modellering i Secure Design

!!! note "Opgave beskrivelse"
    I afsnittet Secure Design bliver der nævnt en type modellering, som bør indgå i en udviklingsproces.
    Hvilken type modellering er der tale om, og hvorfor er den vigtig for sikker softwareudvikling?

Det er Threat modeling, hvilket er en metode der beskriver hvordan man kan identifisere, forstå, og mindske sikkerheds risici. Det er vigtigt så man som developer kan finde og fikse mulige sårbarheder inden en hacker unytter dem.

## Opgave - ASVS
### 1. Input validering

!!! note "Opgave beskrivelse"
    Kig [OWASP ASVS 5.0.0](https://github.com/OWASP/ASVS/tree/v5.0.0#latest-stable-version---500)
    I hvilket afsnit kan man finde et overblik over, hvad man bør sikre sig i forhold til inputvalidering?

V2.2 Input Validation

### 2. Bilag D(Appendix D): Recommendations

!!! note "Opgave beskrivelse"
    Hvad beskrives der i Bilag D? Giv en kort opsummering af de vigtigste punkter.

Det handler om ting man kunne gøre for at gøre sin web applikation mere sikker. Punkterne er ikke krav, men strækt anbefalet.

Her er nogle af det vigtigste:

- Lav en security.txt fil med link eller email, så man kan kontakte ejeren i tilfælde af sikkerheds problemer.
- Brug robots.txt så sensitive sider ikke kommer frem på søge maskiner.
- Benyt client-side input validation sammen med server-side, så man akn opdage hvis noget har undgået client-side kontroller i et forsøg på at angribe applikationen.
- Implamenter et password strength meter, så brugere kan se hvor stærkt dere password er.

### 3. Niveauer i ASVS

!!! note "Opgave beskrivelse"
    Hvor mange niveauer er kravene i ASVS opdelt i ? Og hvorfor er de opdelt i flere niveauer?.

Den er delt op i 3 neveauer. Fordi ikke alle applikationer er ens, og alle har forskellige krav.

## Opgave - Request for Comments

### Hvad er Request for Comments?
### 1. Introduktion til RFC'er

!!! note "Opgave beskrivelse"
    Læs introduktionen til RFC'er på RFC Editorens hjemmeside. Beskriv med jeres egne ord, hvad en RFC er, og hvorfor den er vigtig for internettet.

Kort sagt er Request for Comments (RFC) officielle dokumenter, der definerer internetstandarder, protokoller og teknologier. De er vigtige da de bestemmer hvordan kommunikation forgår mellem computere, da det setter standarden.

### 2. HTTP/1.1: Semantics and Content (RFC 7231)

!!! note "Opgave beskrivelse"

    - Gå til [RFC 7231 - HTTP/1.1: Semantics and Content](https://datatracker.ietf.org/doc/html/rfc7231).
    - Beskriv kort, hvad RFC 7231 omhandler. Hvilke HTTP-metoder er defineret i RFC 7231, og hvad er formålet med hver metode? Hvordan er metoderne struktureret i dokumentet, og hvordan relaterer de sig til HTTP-standarden?

RFC 7231 beskriver Hypertext Transfer Protocol (HTTP/1.1)

|Metode|Beskrivelse|
|---|---|
|GET|Overfør en aktuel repræsentation af målressourcen|
|HEAD|Samme som GET, men overføre kun statuslinjen og header-sektionen.|
|POST|Udfør ressource-specifik behandling af request payload.|
|PUT|Erstat alle aktuelle repræsentationer af målressourcen med request payload.|
|DELETE|Fjern alle aktuelle repræsentationer af target resource.|
|CONNECT|Opret en tunnel til den server, der er identificeret af target resource.|
|OPTIONS|Beskriv kommunikationsindstillingerne for target resource.|
|TRACE|Udfør en meddelelses-loopback-test langs stien til target resource.|

### 3. Transport Layer Security (TLS) Protocol Version 1.3 (RFC 8446)

!!! note "Opgave beskrivelse"

    - Gå til [RFC 8446 - TLS Protocol Version 1.3](https://datatracker.ietf.org/doc/html/rfc8446).
    - Beskriv kort, hvad RFC 8446 omhandler. Hvad er TLS 1.3, og hvilke hovedkomponenter og funktioner beskrives i dokumentet? Hvordan er dokumentet struktureret, og hvilke sektioner fokuserer på de vigtigste aspekter af TLS 1.3?

RFC 8446 beskriver The Transport Layer Security (TLS) version 1.3 af protokollen. Kryptografi er en stor del af det skal der er algoritmer til at gøre det sikkert.

4. Handshake Protocol
7. Cryptographic Computations

### 4. OAuth 2.0 Authorization Framework (RFC 6749)

!!! note "Opgave beskrivelse"

    - Gå til [RFC 6749 - OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749).
    - Beskriv kort, hvad RFC 6749 omhandler. Hvad er hovedformålet med OAuth 2.0, og hvilke roller og komponenter defineres i dokumentet? Hvordan beskriver dokumentet de forskellige autorisationsmetoder og -flows, og hvordan er de struktureret?

OAuth 2.0 bruges til at giver andre applikationer adgang til en anden applikation.

der er roller som består af resource owner som er brugeren. så den ene app som får adgang til den anden.

Der er tale om Client Registration, da man være registreret ved begge applikationer. Begge applikationer skal have Protocol Endpoints implamenteret, og man skal da man skal authenticate ved begge applikationer.

### 5. JSON Web Token (JWT) (RFC 7519)

!!! note "Opgave beskrivelse"

    - Gå til [RFC 7519 - JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519).
    - Beskriv kort, hvad RFC 7519 omhandler. Hvad er JSON Web Tokens (JWT), og hvilke elementer består de af ifølge dokumentet? Hvordan beskriver dokumentet strukturen og formatet af JWT'er, og hvilke anvendelsesområder nævnes?

RFC 7519 handler om brugen af JSON Web Tokens, som man bruger til at authenticate, til en given web applikation eller API.

Creating and Validating JWTs