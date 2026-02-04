# Introduktion til faget og grundlæggende netværksviden

## Opgave - Fagets læringsmål

??? note "Opgave beskrivelse"
    
    1. Find læringsmålene i [studieordningen](https://www.ucl.dk/studiedokumenter/it-sikkerhed) og del linket mellem jer
    2. I jeres gruppe debattér hvordan i forestiller jer at læringsmålene er relevante for faget og hvad i kan bruge dem til, begrund jeres valg og noter dem så vi kan diskutere det på klassen.

## Opgave - Grundlæggende netværksviden

!!! note "Opgave beskrivelse"
    
    Besvar følgende spørgsmål.
    
1. Hvad betyder LAN?
    - Local Area Network
2. Hvad betyder WAN?
    - Wide Area Network
3. Hvor mange bits er en ipv4 adresse?
    - 32	
4. Hvor mange forskellige ipv4 adresser findes der?
    - 4,29 milliarder
5. Hvor mange bits er en ipv6 adresse?
    - 128 bits
6. Hvad er en subnet maske?
    - Hosts / netværk
7. Hvor mange hosts kan der være på netværket 10.10.10.0/24
    - 2 ^ 10 - 2 = 254
8. Hvor mange hosts kan der være på netværket 10.10.10.0/22
    - 2 ^ 10 - 2 = 1022 
9. Hvor mange hosts kan der være på netværket 10.10.10.0/30
    - 2 ^2 - 2 = 2
10. Hvad er en MAC adresse?
    - Unikt og inkorporeret i netværkskortet.
    - Bruges til kommunikation på lokale netværk mellem enheder.
11. Hvor mange bits er en MAC adresse?
    - 48 bits
12. Hvilken MAC adresse har din computers NIC?
    - Godt spørgsmål!
13. Hvor mange lag har OSI modellen ?
    - 7 lag
14. Hvilket lag i OSI modellen hører en netværkshub til?
    - Fysisk lag
15. Hvilket lag i OSI modellen hører en switch til?
    - Data link (klassisk switch) / Netværk lag
16. Hvilket lag i OSI modellen hører en router til?
    - Netværk
17. Hvilken addressering anvender en switch?
    - MAC
18. Hvilken addressering anvender en router?
    - IP
19. På hvilket lag i OSI modellen hører protokollerne TCP og UDP til?
    - Transport
20. Hvad udveksles i starten af en TCP forbindelse?
    - Three way handshake
21. Hvilken port er standard for SSH?
    - 22
22. Hvilken port er standard for https?
    - 80 (http) eller 443 (https)
23. Hvilken protokol hører port 53 til?
    - DNS
24. Hvilken port kommunikerer OpenVPN på?
    - 1194
25. Er FTP krypteret?
    - Nej
26. Hvad gør en DHCP server/service?
    - Automatisk tildeling af dynamisk ip-adresser på et netværk
27. Hvad gør DNS?
    - Domain Name Server = Forbinder FQDN til IP-adresser
28. Hvad gør NAT?
    - Network Address Translation
    - Oversætter adresser fra et netværk til et andet
29. Hvad er en VPN?
    - Virtuelt netværk via krypteret tunnel
30. Hvilke frekvenser er standard i WIFI?
    - 2,4 GHz og 5 GHz
31. Hvad gør en netværksfirewall ?
    - Filtrerer netværkstrafik
32. Hvad er OPNsense?
    - Mange ting, blandt andet en router og en firewall


## Opgave - Genopfriskning af grundlæggende netværk

??? note "Opgave beskrivelse"

    Se følgende videoer eller læs det fra bogen, tag notater undervejs og dokumenter dine opdagelser (det du ikke voídste i forvejen, i stikordsform!):

    1. [Introduction (reposted) - What is the Internet](https://youtu.be/74sEFYBBRAY?si=4ueAKQ--N-uJfNmq)
    1. [The network edge](https://youtu.be/k8NmM-hImBU?si=KDe27csJAvhrxKOg)
    1. [The network core](https://youtu.be/f1nUcCdQJ8Y?si=wo3x4KGmDFq3mpF2)
    
    Eller bare læs kapitlerne: 1.1, 1.2, 1.3 i bogen *Computer Networking: A Top-Down Approach*
    
    Svar på følgende reflekterings spørgsmål.

#### SEKTION 1.1

- R1. Hvad er forskellen på en "host" (vært) og et "end system"? Nævn flere forskellige typer af end systems. Er en webserver et end system?
    - Der er ingen forskel, mellem et host og et "end system".
    - Et "end system" er defineret som end systems fordi de sidder ved kanten/enden af af internettet. De er alle forbundet med communication links og packet switches, såsom netværks switches og routere.
    - Smartphones, Workstations, laptop, og servere er alle end systems.
- R2. Ordet "protokol" bruges ofte til at beskrive diplomatiske forbindelser. Hvordan beskriver Wikipedia en diplomatisk protokol?
    - > "A protocol is a rule which describes how an activity should be performed"
- R3. Hvorfor er standarder vigtige for protokoller?
    - Så der ikke er miskommunikation, mellem systemer.
        - Hvis jeg snakker dansk til en tysker, vil tyskeren aldrig forstå mig.
        - Det er en form for universel sprog.

#### SEKTION 1.2

- R6. Lav en liste over de tilgængelige teknologier til internetadgang i din by. 
    - 3G, 4G, 5G, Wifi, Coax kabler, Fibernet.
- R7. Hvad er transmissionshastigheden for Ethernet LAN?
    - > "100 Mbps to tens of Gbps"
- R8. Hvilke fysiske medier kan Ethernet køre over?
    - Coax, og fibernet
- R10. Beskriv de mest populære teknologier til trådløs internetadgang i dag. Sammenlign og opstil forskellene mellem dem.
    - 5G
        - under 100 kilometers dækning
    - Wifi
        - Hastigheder op til og/eller mere end 100 Mbps
        - under 100 meters dækning 
    
        ![Wireless transmission rates](Wireless_transmission.png)

#### SEKTION 1.3

- R12. Hvilken fordel har et kredsløbskoblet netværk (circuit-switched) frem for et pakkekoblet netværk (packet-switched)?
    - Den primære fordel ved et kredsløbskoblet netværk (circuit-switched) er, at de ressourcer, der er nødvendige langs stien (såsom transmissionshastighed og buffere), reserveres eksklusivt i hele kommunikationssessionens varighed
- R15. Nogle indholdsudbydere (content providers) har skabt deres egne netværk. Beskriv Googles netværk. Hvad motiverer indholdsudbydere til at skabe disse netværk?
    - Man reducere prisen man betaler til de højere ISP's og man får bedre kontrol over hvordan ens tjenester bliver send til kunder.

