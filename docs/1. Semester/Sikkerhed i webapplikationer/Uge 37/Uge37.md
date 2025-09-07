# Sårbarheder i API'er

!!! note "Praktiske mål"

    - Hver studerende har anvendt BURP suite til at analyser forspørgelser fra en web applikation.
    - Hver studerende har identificeret en simpel BOLA sårbarhed.
    - Hver studerende har identificeret en simpel Excessive data exposure sårbarhed.

!!! note "Læringsmål"

    **Viden**

    - teorier, metoder og praksis relateret til webapplikationssikkerhed, herunder principper for sikring af API’er.
    - typiske trusler og sårbarheder forbundet med webapplikationer og deres årsager
    - metoder til vurdering og efterprøvning af sikkerhedsmæssige foranstaltninger.

    **færdigheder**

    - anvende metoder til at identificere og analysere sikkerhedsmæssige svagheder i webapplikationer
    - tolke og vurdere testresultater i forhold til kendte sikkerhedsprincipper

!!! note "Forberedelse"

    - Skim læs kapitel 0 i bogen "Hacking APIs"
    - Læs kapitel 3 i bogen "Hacking APIs"

??? note "Reflektions punkter efter forberedelsen"

    **Kapitel 0**:

    - Hvad er en trusselsaktør?
        - En trusselsaktør er den som angriber API'en eller applikation.  Trusselsaktøren kan være alle, lige fra en random person, til en insider der ved næsten alt om applikationen.
    - hvad menes der med black,grey & whitebox testing?
        - Blackbox testing er når man som pen-tester kun kender firmaet man skal teste, og det eneste information man får er måske en IP adresse. Her fra skal man så lave rekognoscering, for at finde information om målet.
        - Graybox testing er når man får givet mere information, såsom hvad man må og ikke må teste (In and out of scope), adgang til API dokumentationen og så videre. I graybox testing skipper man rekognoscering, så der kan bruges mere tid på at teste applikationen eller API'en. Typisk falder bug bounty ind i mellem balck og graybox, da man får givet et scope, man skal stadig lave rekognoscering.
        - Whitebox testing er når klienten giver så meget information og adgang til pen-testeren som muligt. Dette kunne være source code adgang, eller adgang til deres software development kit (SDK). Denne metodes formål er at demonstrære en inside attacker.

    **Kapitel 3**:

    - Hvilken information kan du finde på OWASP API top 10 list?
        - OWASP API Security Top 10 er en liste over de mest almene API sårbarheder.
    - Hvad er en BOLA sårbarhed?
        - broken object level authorization (BOLA) sårbarheder, sker når en API ikke ordenligt tjekker om en given bruger er tilladt til at hente resourcer. Det kan være at man henter data om sig selv med sit user id `5000`. Men hvad sker der hvis man så prøver at hente data fra bruger `5001`, hvis man kan det uden at API'en tjekker om man har tilladelse til bruger data for bruger `5001` så er der tale om BOLA. 
    - Excessive data exposure?
        - Excessive data exposure sårbarhed, kan ske når en API svare tilbage med alt det information den har på det ønskede data. Lad os sige at man bruger en API til at få sin egen bruger data, men den også sender bruger data for den bruger der lavede ens egen bruger. Her udstiller API'en en anden bruger uden grund da de sender for meget data. Dette sker oftest når en API forventer at brugere sortere det data fra de ikke skal bruge.