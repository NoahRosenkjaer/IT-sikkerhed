# Rekognoscering

!!! note "Læringsmål"

    **Viden**

    - anvende metoder til at identificere og analysere sikkerhedsmæssige svagheder i webapplikationer
    - metoder til vurdering og efterprøvning af sikkerhedsmæssige foranstaltninger
    
    **Færdigheder**
    
    - metoder til vurdering og efterprøvning af sikkerhedsmæssige foranstaltninger
    - tolke og vurdere testresultater i forhold til kendte sikkerhedsprincipper.
    
    **Kompetencer**
    
    - gennemføre vurdering af sikkerheden i webapplikationer på baggrund af systematiske test.
    - udlede og formidle relevante identificerede sikkerhedsproblematikker til fagfæller.

!!! note "Praktiske mål"

    - Hver studerende har anvendt Gobuster til enumerering af crAPI.
    - Hver studerende har anvendt flere af wordlisterne fra seclist.
    - Hver studerende er begyndt at udarbejde en wordlist til crAPI.

!!! note "Forberedelse"

    - Læs kapitel 6 i bogen "Hacking APIs"
    - Se tutorialen [NMAP basics tutorial](https://www.youtube.com/watch?v=W7076RPIgfQ)
    - Se tutorialen [Gobuster basics tutorial](https://www.youtube.com/watch?v=HjXNK-mYwDQ)

??? note "Reflektions punkter efter forberedelsen"

    1. Hvad er passiv rekognoscering?
        - Det er at man bruger offentlige resourcer til at få information om målet. og man får sin information fra andenhånds kilder.
    2. Hvad er OSINT?
        - Det er en form for passiv rekognoscering. Og man interagere ikke med målet.
    3. Hvad er de 3 faser i den passive rekognoscering proces?
        - Phase One: Cast a Wide Net
        - Phase Two: Adapt and Focus
        - Phase Three: Document the Attack Surface
    4. Hvad er aktiv rekognoscering?
        - Det er aktivt at scanne målet med tools som n-map, eller Gobuster.
    5. Hvad er de 4 faser i den aktive rekognoscreings proces?
        - Phase Zero: Opportunistic Exploitation
        - Phase One: Detection Scanning
        - Phase Two: Hands-on Analysis
        - Phase Three: Targeted Scanning

## Opgave - OSINT med GitHub

!!! note "Opgave beskrivelse"

    Kildekoden til en applikation i en offentlig repository på GitHub udstiller uhensigtsmæssigt et stykke information for meget.

    Link til repo:
    [https://github.com/mesn1985/DotNetApplicationWithToMuchInformation](https://github.com/mesn1985/DotNetApplicationWithToMuchInformation)

    1. Find og forklar hvilken information, der udstilles uhensigtsmæssigt. 
    2. Hvorfor er det et problem? 
    3. Hvordan burde informationen være håndteret i stedet?

1. Find og forklar hvilken information, der udstilles uhensigtsmæssigt. 
    - appsettings.json
        - **"ApiToken": "abc123def456ghi789"**
        - I denne konfigurations fil finder man en API key.
    - AWSSecretsManager.cshtml.cs
        - **string secretName = "AspNetCoreSecurityAWS";**
        - **string region = "us-east-2";**
        - Dette ligner et ID til at få adgang til noget Amazon cloud.
2. Hvorfor er det et problem? 
    - API key
        - Med den kan alle bruge deres API, som om de var dem.
    - secretName
        - Med dette kan man bruge secretName til at generere en API key på vegne af den applikation.
3. Hvordan burde informationen være håndteret i stedet?
    - Man burde bruge environment variabler.

## Opgave - Aktiv Rekognoscering

??? note "Opgave beskrivelse"

    1. Brug [Nmap](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/3_Active_reconnaissance.md#1--nmap-full-port-scan) til at scanne alle porte

        - Udfør en fuld portscanning
        - Dokumentér hvilke porte der er åbne

    2. Lav en [Nmap](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/3_Active_reconnaissance.md#2--nmap-service-version-detection) service scanning

        - Udfør en service detection (-sV) for at identificere hvilke services der kører
        - Sammenlign resultaterne med din portscan

    3. Brug [Gobuster](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/3_Active_reconnaissance.md#3--enumerating-crapi-with-gobuster-and-the-wordlist-commontxt)  med `common.txt`

        - Brug gobuster til at brute-force paths på crAPI
        - Gem resultaterne og notér relevante endpoints

    4. Brug [Gobuster](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/3_Active_reconnaissance.md#5--enumerating-crapi-with-zap) med `quickhits.txt`

        - Brug din anden wordlist og sammenlign output
        - Tilføj evt. nye paths til din samlede wordlist

    5. Test dine egne wordlister

        - Du har undervejs bygget dine egne wordlists (crAPI)
        - Brug gobuster eller ZAP til at teste dem
        - Sammenlign med common.txt og quickhits.txt

Jeg starter med at downloade [seclists](https://www.kali.org/tools/seclists/)

1. Brug [Nmap](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/3_Active_reconnaissance.md#1--nmap-full-port-scan) til at scanne alle porte

    - Udfør en fuld portscanning
        - Jeg brugte denne kommando `nmap 127.0.0.1 -p1-65535` til at scanne alle porte.
    - Dokumentér hvilke porte der er åbne
        
        |PORT|STAE|SERVICE|
        |---|---|---|
        |3000/tcp|open|ppp|
        |4280/tcp|open|vrml-multi-use|
        |8025/tcp|open|ca-audit-da|
        |8443/tcp|open|https-alt|
        |8888/tcp|open|sun-answerbook|

2. Lav en [Nmap](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/3_Active_reconnaissance.md#2--nmap-service-version-detection) service scanning

    - Udfør en service detection (-sV) for at identificere hvilke services der kører
        - Jeg brugte denne kommando `nmap 127.0.0.1 -p1-65535 -sV` til at scanne alle porte.
    - Sammenlign resultaterne med din portscan

        |PORT|STATE|SERVICE|VERSION|
        |---|---|---|---|
        |3000/tcp| open|  ppp?|NONE|
        |4280/tcp| open|  http|     Apache httpd 2.4.62 ((Debian))|
        |8025/tcp| open|  http|     Golang net/http server (Go-IPFS json-rpc or InfluxDB API)|
        |8443/tcp| open|  ssl/http| OpenResty web app server 1.25.3.1|
        |8888/tcp| open|  http|     OpenResty web app server 1.25.3.1|

3. Brug [Gobuster](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/3_Active_reconnaissance.md#3--enumerating-crapi-with-gobuster-and-the-wordlist-commontxt)  med `common.txt`

    - Brug gobuster til at brute-force paths på crAPI
        1. Først testede jeg hvor langt crAPI's `Content-Length` er. med denne kommando `curl -k -i https://127.0.0.1:8443/thispathshouldnotexist | grep Content-Length` hvilket giver: `Content-Length: 2837`. Dette gør jeg da den responder med 200 ok, selv om siden ikke findes.
        2. Nu da man kender den `Content-Length: 2837`, kan man køre denne kommando `gobuster dir -u https://127.0.0.1:8443 -w /usr/share/seclists/Discovery/Web-Content/common.txt --no-tls-validation --exclude-length 2837`
    - Gem resultaterne og notér relevante endpoints

Resultaterne er gemt her:
```shell linenums="0"
/.env                 (Status: 200) [Size: 201]
/.well-known/jwks.json (Status: 200) [Size: 528]
/community            (Status: 301) [Size: 175
/favicon.ico          (Status: 200) [Size: 3150]
/identity             (Status: 301) [Size: 175
/images               (Status: 301) [Size: 175
/robots.txt           (Status: 200) [Size: 67]
/workshop             (Status: 301) [Size: 175
```

4. Brug [Gobuster](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/3_Active_reconnaissance.md#5--enumerating-crapi-with-zap) med `quickhits.txt`

    - Brug din anden wordlist og sammenlign output
        - Her bruger jeg denne kommando `gobuster dir -u https://127.0.0.1:8443 -w /usr/share/seclists/Discovery/Web-Content/quickhits.txt --no-tls-validation --exclude-length 2837`. Her har jeg erstattet selv word listen.
    - Tilføj evt. nye paths til din samlede wordlist
        -  Her fandt den kun et path `/.env                 (Status: 200) [Size: 201]`

5. Test dine egne wordlister

    - Du har undervejs bygget dine egne wordlists (crAPI)
        - Ja
    - Brug gobuster eller ZAP til at teste dem
        - Kommando: `gobuster dir -u https://127.0.0.1:8443 -w ownWordList.txt --no-tls-validation --exclude-length 2837`
        - Resultat: 
    ```shell linenums="0"
    Starting gobuster in directory enumeration mode
    ===============================================================
    /.env                 (Status: 200) [Size: 201]
    /favicon.ico          (Status: 200) [Size: 3150]
    /identity             (Status: 301) [Size: 175] [--> https://127.0.0.1/identity/]
    /community            (Status: 301) [Size: 175] [--> https://127.0.0.1/community/]
    /images               (Status: 301) [Size: 175] [--> https://127.0.0.1/images/]
    /workshop             (Status: 301) [Size: 175] [--> https://127.0.0.1/workshop/]
    /robots.txt           (Status: 200) [Size: 67]
    /.well-known/jwks.json (Status: 200) [Size: 528]
    Progress: 8 / 8 (100.00%)
    ```

    - Sammenlign med common.txt og quickhits.txt

    Min list kommer til at være ens med common. da det vra common der fandt alt i min liste.

    ```txt
    .env
    .well-known/jwks.json
    community
    favicon.ico          
    identity
    images
    robots.txt           
    workshop   
    ```