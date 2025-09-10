# Grundlæggende netværk

!!! note "Læringsmål"


    **Overordnede læringsmål fra studie ordningen**

    - Den studerende har viden om og forståelse for:
        - Grundlæggende netværksprotokoller
    - Den studerende kan supportere løsning af sikkerhedsarbejde ved at:
        - Mestre forskellige netværksanalyse tools

    **Læringsmål den studerende kan bruge til selvvurdering**
    
    - Den studerende ved hvad OSI modellen og dens lag er
    - Den studerende kender TCP/IP modellen, dens lag og hvordan 3 way handshake fungerer
    - Den studerende kan anvende ping, hvilken protokol ping anvender og relevante ping parametre
    - Den studerende ved hvad traceroute kan anvendes til og hvordan det bruges
    - Den studerende ved hvad whois er og kan anvende det via CLI
    - Den studerende har viden om hvordan DNS systemet er opbygget og hvordan dig kan bruges til at forespørge DNS servere
    - Den studerende ved hvad et netværk er herunder hvad IP adresser og MAC adresser er
    - Den studerende kender til MAC spoofing
    - Den studerende kender de forskellige netværks topologier
    - Den studerende ved hvad hhv. en switch og en router anvendes til
    - Den studerende har viden om ARP protokollen
    - Den studerende kender til DHCP og hvordan protokollen fungerer

!!! note "Forberedelse"


    - Læs undervisningsplanen og øvelser
    - Læs kapitel 2 - Sårbarheder i informationssystemer i "IT-Sikkerhed i praksis", hav fokus på CIA modellen.

    - Gennemfør kurset:
    [Networking Foundations: Networking Basics](https://www.linkedin.com/learning-login/share?account=57075649&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fnetworking-foundations-networking-basics%3Ftrk%3Dshare_ent_url%26shareId%3DsSYuusakR8yljI%252BhoDJAgQ%253D%253D)

## Opgave - CIA modellen

!!! note "Opgave beskrivelse"

    Øvelsen skal laves som gruppe/team

    - Læs om CIA modellen i bogen "IT-Sikkerhed i praksis, en introduktion" kapitel 2.
    - Vælg et af følgende scenarier som i vil vurdere i forhold til CIA:
        - En password manager (software)
        - En lægeklinik (virksomhed)
        - Dine data på computere og cloud (...)
        - Energileverandør (kritisk infrastruktur)
    - Vurder, prioitér scenariet i forhold til CIA modellen. Noter og begrund jeres valg og overvejelser.
    - Hvilke(n) type hacker angreb vil være mest aktuelt at tage forholdsregler imod? (DDos, ransomware, etc.)
    - Hvilke forholdsregler kan i tage for at opretholde CIA i jeres scenarie (kryptering, adgangskontrol, hashing, logging etc.)
    - Hver gruppe fremlægger det de er kommet frem til og alle giver feedback.



- Vælg et af følgende scenarier som i vil vurdere i forhold til CIA:

    - Vi har valgt en lægeklinik (virksomhed)

- Vurder, prioitér scenariet i forhold til CIA modellen. Noter og begrund jeres valg og overvejelser. Hvilken del af CIA mener i er mest vigtig.
    1. Fortrolighed, da persondata er meget følsomt går ind under lovgivninger som GDPR. Hvis en hacker fik adgang til en persons persondata kunne de afpresse, begå identitets tyveri, eller sælge det videre. læækning af patient data kan skade tilliden mellem patien og læge/lægehus.
    2. Integritet er også mgete vigtig da patient jurnaler ikke må ændres af uauthentiseret personale eller andre.
    3. Tilgengelighed da det er vigtigt for læger at have dine data tilgengelig når de skal hjælpe dig.
- Hvilke(n) type hacker angreb vil være mest aktuelt at tage forholdsregler imod? (DDos, ransomware, etc.)
    - Phising
        - Falske mails med farlige links, så man kunne downloade malware/ransomware, eller links til info-stealers til login informationer.
    - Ransomware, dobbelt afpressning
        - Dobbelt afpressning er når en hakcer vil have penge for at give dekrypterings nøglen, hvorefter de afpresser igen for ikke at lække
    - Insider threat
        - Nogen som arbejder for lægeklinikken, og kommer til at lække fortroligt information
- Hvilke forholdsregler kan i tage for at opretholde CIA i jeres scenarie (kryptering, adgangskontrol, hashing, logging etc.)
    - 0 trust
        - Kan mindske inderder threat
    - Multi factor authentication
        - Hvis passwords skulle blive lækket
    - Logging
        - Så man kan se hvad der er sket.
    - Backups
        - Så man kan starte forfra hvis man skulle blive ramt af ransomware
    - Kryptering
        - For at holde fortroligheden
    - Medarbejder security awareness træning
        - For at mindske change for at medarbejdere trykker på farlige link og bliver phishet.