# Endpoint analyse med postman.

!!! note "Læringsmål"
    
    **Viden**

    - metoder til vurdering og efterprøvning af sikkerhedsmæssige foranstaltninger.

    **Færdighed**

    - anvende metoder til at identificere og analysere sikkerhedsmæssige svagheder i webapplikationer.
    - tolke og vurdere testresultater i forhold til kendte sikkerhedsprincipper.

!!! note "Praktiske mål"

    - Den studerende har lavet en Postman collection til crAPI.
    - Den studerende har lavet en Postman collection til Juiceshop
    - Den studerende er informeret om hvad en test case er.

!!! note "Forberedelse"


    - Læs kapitel 7 i bogen "Hacking APIs"
    - Se videon How to write test cases.
        Jeg har valgt denne video, fordi test cases skal udarbejde på samme måde, uagtet om det ser en funktionel test af softwaren man udføre, eller en pentest af software. Ignorer delen med post condition og reetablering af systemet til den oprindelige tilstand.

??? note "Reflektions punkter efter forberedelsen"

    - Hvorfor kan API dokumentationen være en godt sted at starte analysen?
        - Man kan finde ud af hvordan en API er opbygget og men kan finde ud af hvad den forventer af brugeren og hvad man som bruger kan forvente af API'en
    - Hvorfor bør man starte med at teste API’ets tiltænkte funktioner?
        - Så man kan få en fornemmelse og forståelse af hvorden dens brug er tiltænkt. Når man ved hvordan noget virker er det nemmere at finde svagheder og sårbarheder. Lige som at finde brugstilfælde og misbrugstilfælde.
    - Hvad menes der med fejl i forretnings logikken, og hvorfor kan det føre til sårbarheder?
        - Når logikken i en applikation bliver brugt mod applikationen selv.
        - Det kan føre til sårbarheder, da det er svært at scanne efter dette da, det jo eneligt er en del af funktionen, som bliver misbrugt. Det kan ske når funktioner i logikken ikke er specifik nok.
    - Hvor er dokumenteret test cases vigtige når en sårbarhed skal præsenteres for andre?
        - Ikke sikker på jeg forsår spørgsmålet.
