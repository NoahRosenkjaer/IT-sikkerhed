# Trusselsbillede

!!! note "Overordnede læringsmål fra studie ordningen"

    **Viden**

    Den studerende har viden om og forståelse for:

    - Trusler og trusselsbilledet
    - Operationelle overvejelser for it-sikkerhed

    **Færdigheder**

    Den studerende kan:

    - Vurdere hvilke sikkerhedsprincipper, der skal anvendes i forhold til en given kontekst.

    **Kompetencer**

    Den studerende kan:

    - Håndtere analyser om, hvilke sikkerhedstrusler der aktuelt skal behandles i et konkret it-system.
    
!!! note "Læringsmål den studerende kan bruge til selvvurdering"

    **Viden**

    Den studerende har viden om og forståelse for:

    - Trusselsaktører og deres arbejdsmetoder

    **Færdigheder**

    Den studerende kan:

    - Anvende værktøjer til at analysere angrebsfaser og arbejdsmetoder
    - Udføre en simpel trusselsanalyse

!!! note "Forberedelse"

    - Kig på et par [trusselsvurderinger](https://www.cfcs.dk/da/cybertruslen/trusselsvurderinger/) fra Styrelsen for samfundssikkerhed.
    - Se video der introducerer MITRE ATT&CK framework: [MITRE ATT&CK® Framework](https://youtu.be/Yxv1suJYMI8?si=ccP67mtIvSpB0bJX)
    - Læs om APT gruppen "Salt Typhoon" på TV2 nyhederne: [Salt Typhoon har udført det mest ambitiøse cyberangreb nogensinde](https://nyheder.tv2.dk/udland/2025-09-04-salt-typhoon-har-udfoert-det-mest-ambitioese-cyberangreb-nogensinde)
    - Læs om Salt Typhoons Taktikker, Teknikker og Procedurer på MITRE ATT&CK: Groups: [Salt Typhoon](https://attack.mitre.org/groups/G1045/)

## Opgave - Trusselsbillede, et overblik

!!! note "Opgave beskrivelse"

    1. Rangér kategorierne (de syv primære cybertrusler) efter cfcs trusselsniveau for hver kategori hvor det er muligt - brug højest 10 minutter på dette
    1. Find eksempler fra virkeligheden (husk et link som reference, eksempler er herunder) der passer på hver kategori, start med dem der har det højeste CFCS trusselsniveau.
        - Cyberkrig (Ukraine/Rusland?)
        - Politisk påvirkning (Valg i USA?)
        - Cyberterrorisme (elbiler? kritisk infrastruktur?)
        - Cyberspionage (mod lande eller virksomheder?)
        - Cyberkriminalitet (Er der penge i det?)
        - Hacktivisme (er hackere onde??)
        - Overvågning (hvem kan dog finde på at overvåge andre?)

1. Rangér kategorierne (de syv primære cybertrusler) efter cfcs trusselsniveau for hver kategori hvor det er muligt - brug højest 10 minutter på dette

    - cyberkrig: 2,5 (statslig destruktive angreb)
    - desinformation: Ikke taget i betraktning
    - cyberterrorisme: (religiøs eller politisk ikke statslig gruppe der selvstændigt begår destruktive angreb på sektorer eller grupper af mennesker for at gøre skade)
    - cyberspionage: 5,5
    - overvågning: Ikke taget i betraktning
    - cyberkriminalitet: 7,5
    - hacktivisme: 4

1. Find eksempler fra virkeligheden (husk et link som reference, eksempler er herunder) der passer på hver kategori, start med dem der har det højeste CFCS trusselsniveau.
    - Cyberkrig (Ukraine/Rusland?)
        - [Rusland står bag destruktivt cyberangreb mod satellitudstyr i forbindelse med invasionen af Ukraine](https://www.fmn.dk/da/nyheder/2022/rusland-star-bag-destruktivt-cyberangreb-mod-satellitudstyr-i-forbindelse-med-invasionen-af-ukraine/)
    - Politisk påvirkning (Valg i USA?)
        - [Putins propagandamaskine: Sådan ser krigen ud på russisk stats-tv](https://www.dr.dk/nyheder/udland/hvilke-loegnhistorier-fortaeller-russiske-medier)
    - Cyberterrorisme (elbiler? kritisk infrastruktur?)
        - Ikke fundet
    - Cyberspionage (mod lande eller virksomheder?)
        - [Chinese Hackers Breach Juniper Networks Routers With Custom Backdoors and Rootkits](https://thehackernews.com/2025/03/chinese-hackers-breach-juniper-networks.html)
    - Cyberkriminalitet (Er der penge i det?)
        - [Famous Phishing Incidents from History](https://www.hempsteadny.gov/635/Famous-Phishing-Incidents-from-History)
    - Hacktivisme (er hackere onde??)
        - [Pro-Iranian Hacktivist Group Leaks Personal Records from the 2024 Saudi Games](https://thehackernews.com/2025/06/pro-iranian-hacktivist-group-leaks.html)
    - Overvågning (hvem kan dog finde på at overvåge andre?)
        - Ikke fundet

## Opgave - Hvordan arbejder en trusselsaktør?

!!! note "Opgave beskrivelse"

    1. Hver gruppe har en trusselsaktør tildelt (se herunder):
        - Min gruppe fik **[Transparent Tribe](https://attack.mitre.org/groups/G0134/)**
    2. Brug ressourcerne nedenfor (suppler gerne med andre kilder) til at indsamle information om jeres tildelte trusselsaktør. 
        
        Undersøg følgende:

        - Hvem er aktøren? (Baggrund, motivation, kendte angreb/kampagner)
        - Hvilke metoder anvender de? (Teknikker, værktøjer, målgrupper)
        - Eksempler på angreb (Hvem blev angrebet, hvordan, hvornår, konsekvenser)
    3. Forbered en kort præsentation (5-10 minutter - stikordsform)

    4. Del jeres OSINT CTI ved at fremlægge det for en anden gruppe (begge grupper skal fremlægge).

    ressourcer:
    
    - [MITRE ATT&CK](https://attack.mitre.org/)
    - [MITRE CVE](https://www.cve.org/)
    - [malpedia/actors (MISP Galaxy)](https://malpedia.caad.fkie.fraunhofer.de/actors)
    - [CFCS ordforklaringer](https://www.cfcs.dk/da/cybertruslen/ordforklaringer/)


1. Brug ressourcerne nedenfor (suppler gerne med andre kilder) til at indsamle information om jeres tildelte trusselsaktør. 
    
    Undersøg følgende:

    - Hvem er aktøren? (Baggrund, kendte angreb/kampagner)
        - Baggrund: “Transparent Tribe is a suspected Pakistan-based threat group that has been active since at least 2013, primarily targeting diplomatic, defense, and research organizations in India and Afghanistan.”
        - Kendt kampange: “[C0011](https://attack.mitre.org/campaigns/C0011/) was a suspected cyber espionage campaign conducted by Transparent Tribe that targeted students at universities and colleges in India. Security researchers noted this campaign against students was a significant shift from Transparent Tribe's historic targeting Indian government, military, and think tank personnel, and assessed it was still ongoing as of July 2022.”
    - Hvilke metoder anvender de? (Teknikker, værktøjer, målgrupper)
        - Phishing: Spearphishing Attachment
        - Compromise Infrastructure: Domains
        - Stage Capabilities: Upload Malware
        - User Execution: Malicious Link
        - Acquire Infrastructure: Making fake domains

    - Eksempler på angreb (Hvem blev angrebet, hvordan, hvornår, konsekvenser)
        - [C0011](https://attack.mitre.org/campaigns/C0011/): Igen her brugte de blandt andet falske domains, og phishing til at sende malicious filer til studerende i Indien. Målet var at få Crimson på de studerendes computere. Crimson er en remote access trojan (RAT) malware.

## Opgave - Hvilke konsekvenser har et angreb?

!!! note "Opgave beskrivelse"

    Dette er en gruppeøvelse

    1. Find et eksempel, gerne nyere, på en Dansk virksomhed eller organisation der er blevet ramt af et cyberangreb.
    1. Undersøg hvilken konsekvens det har haft for virksomheden?
    1. Hvad mener i virksomheden/organisationen kunne have gjort for at undgå eller nedbringe konsekvensen?
    1. Forbered en helt kort præsentation af ovenstående (2 minutter), dvs. virksomhed, angrebet, konsekvens og bud på hvad de kunne have gjort.
    1. Præsentation på klassen afrunder øvelsen.

1. Find et eksempel, gerne nyere, på en Dansk virksomhed eller organisation der er blevet ramt af et cyberangreb.
    
    - Fredag aften var TV2.dk og TV 2 PLAY kortvarigt ramt af at DDoS-angreb. Det oplyser TV 2 Kommunikation, som også fortæller, at det var hackergruppe Anonymous Sudan, der stod bag. TV 2s tekniske teams sørgede hurtigt for at genoprette stabiliteten, og som en del af indsatsen blev der fredag aften kortvarigt lukket for adgang fra udlandet. [Link](https://icare.dk/ddos/)

2. Undersøg hvilken konsekvens det har haft for virksomheden?
    - TV2.dk og TV2 Play er jo services som ikke er sundhedskritisk og da TV2 er stats ejet så er den økonomiske konsekvens nok ikke særlig kritisk, især når TV2 fik hjemmesiderne op at køre inden for en dag.

    - Der er dog konsekvenser ved tab a penge i den periode. I form af reklamer som ikke kunne blive vist.

3. Hvad mener i virksomheden/organisationen kunne have gjort for at undgå eller nedbringe konsekvensen?
    
    [Network Denial of Service](https://attack.mitre.org/techniques/T1498/)

    When flood volumes exceed the capacity of the network connection being targeted, it is typically necessary to intercept the incoming traffic upstream to filter out the attack traffic from the legitimate traffic. Such defenses can be provided by the hosting Internet Service Provider (ISP) or by a 3rd party such as a Content Delivery Network (CDN) or providers specializing in DoS mitigations.

    Det vil sige at rate limiting er det bedste forsvar. Flere lag af filter er bedre end et lag.


## Opgave - Trusselsvurdering af virksomhed

!!! note "Opgave beskrivelse"

    1. Vælg i gruppen om i vil arbejde med den fiktive virksomhed Sentinel Surveillance Systems eller den virksomhed/organisation i selv arbejder i.
    1. Vurder hvilke kategorier af trusselsaktører virksomheden er udsat overfor (brug ressourcerne fra øvelse 30).
    1. Identificér, en eller flere trusselsaktører der er mest relevante for virksomheden (brug ressourcerne fra øvelse 31)
    1. Analyser, hvilke Taktikker, teknikker og procedurer aktørerne kunne tænkes at bruge mod virksomheden (brug ressourcerne fra øvelse 31)
    1. Vurdér hvilke konsekvenser et cyberangreb kan have for virksomheden.
    1. Lav en kort skriftlig trusselsvurdering (1-2 sider) indeholdende ovenstående, husk kildeanvisninger.

1. Vælg i gruppen om i vil arbejde med den fiktive virksomhed Sentinel Surveillance Systems eller den virksomhed/organisation i selv arbejder i.
    - Vi har valgt at gå med Sentinel Surveillance Systems (SSS)

        >Sentinel Surveillance Systems er en mellemstor virksomhed med
        >omkring 85 ansatte. De er specialiseret i udvikling, produktion og
        >installation af avancerede videoovervågningssystemer, og de leverer
        >skræddersyede overvågningsløsninger til både private hjem,
        >virksomheder og kritisk infrastruktur i hele Europa.
        >De har hovedkontor i København, mens deres produktionsfaciliteter
        >er placeret i Tjekkiet, hvilket giver dem adgang til højt kvalificerede
        >ingeniører og teknologer samt omkostningseffektive
        >produktionsmuligheder.
        >Virksomheden er kendt for sin høje grad af digitalisering og
        >avancerede teknologiske løsninger, som gør dem til en af de førende
        >aktører på markedet"

1. Vurder hvilke kategorier af trusselsaktører virksomheden er udsat overfor.
    - SSS er en virksomhed der er specialiseret i udvikling produktion og installation af avancerede IoT-videoovervågningssystemer
    - I følge CFCS's rapport [Cybertruslen mod IoT enheder](https://www.cfcs.dk/globalassets/cfcs/dokumenter/trusselsvurderinger/cybertruslen-mod-iot-enheder.pdf) så er 

        > Truslen fra cyberangreb mod IoT-enheder er **MEGET HØJ**.

        og at

        > Både statslige og ikke-statslige hackere udfører løbende forsøg på cyberangreb mod IoT-enheder i Danmark og i udlandet. Det er meget sandsynligt, at det vil fortsætte på lang sigt.

    Derfor mener vi at cyber kriminalitet og statslig cyber angreb er mest relevante.

1. Identificér, en eller flere trusselsaktører der er mest relevante for virksomheden.
    - Nation state trussel aktører
        - Da SSS blandt andet suplere overvågning til kritisk infrastruktur, og virksomheder.
            [Kinesisk stats opbakket gruppe der går efter kritisk infrastruktur i Indien](https://attack.mitre.org/campaigns/C0043/)
    - Cyberkriminalitet
        - Da der kan være mange penge og goder for hackerer, med kontrol over IoT-enheder.
            [Hackere udnytter IoT-enheder til mange formål](https://www.cfcs.dk/globalassets/cfcs/dokumenter/trusselsvurderinger/cybertruslen-mod-iot-enheder.pdf)

1. Analyser, hvilke Taktikker, teknikker og procedurer aktørerne kunne tænkes at bruge mod virksomheden.
    - bruteforce-angreb
        - [Operation Night Dragon](https://attack.mitre.org/campaigns/C0002/) brugte bruteforce-andgreb til at knække password hashes.
    - T1195 - Supply Chain Compromise
        - [OilRig](https://attack.mitre.org/groups/G0049/) en mistænkt Iransk trusselsgruppe. Har tideligere udnyttet kompromitterede organisationer til at udføre Supply Chain Compromise angreb mod offentlige/stats enheder. Hvilket kunne være SSS der bliver hacket for at få adgang til deres IoT-enheder, som bliver brugt af kritisk infrastruktur. Både software messigt og hardware messigt
    - Development & CI/CD Pipeline Attacks
        - Aktørerne kunne bruge spearphishing angreb mod udviklere, og få adgang til at skrive skadelig kode til produktionen.
    - Collection & Exfiltration
        - Aktørerne kunne samle og eksfilterer overvågnings data til egen server
    - Spionage
        - Aktørerne kan bruge de en, flere eller en kombination af overstående og mange andre angreb til at brgå spionage gennem SSS's IoT-enheder. I følge CFCS, [rapport](https://www.cfcs.dk/globalassets/cfcs/dokumenter/trusselsvurderinger/cybertruslen-mod-iot-enheder.pdf) så er cyberspionage en stor risiko, da IoT-enheder ikke bare er en god ingangs vinkel ind i et netværk, men også et godt mål i sig selv. Aktørerne er særligt ude efter IoT-enheder der lagrer eller behandler data. Dette vil vi mene at SSS's IoT-enheder går ind under. 

1. Vurdér hvilke konsekvenser et cyberangreb kan have for virksomheden.
    - Mistillid til virksomheden.
        - Offenlige og private sektore kan miste tilleden til SSS efter et cyberangreb. Dette skade deres omdømme og dermed også deres indkomst.
    - Tab/kryptering af data.
        - Hvis SSS bliver ramt af et spearphishing angreb kunne de potentiel stå overfor et ransomware angreb, som kunne ramme deres server og data, og dermed afpresset.
    - Det kan have konsekvenser for deres kunder, som inkluderer kritisk infrastruktur.
        - Mange af de angreb der bliver beskrevet kan have store konsekvenser for kunder af SSS. Som kunne midste mange timers overvgåning og vigtig data.
    - deres IoT devices kan blive en del af et botnet.
        - Aktørerne kunne bruge deres IoT-enheder som en del af et botnet, som aktørerne kan begå mere cyberkriminalitet med. Så som DDOS angreb, eller de kan bruge dem som en proxy for at maskere deres spor.