# Angreb på autentificering

!!! note "Læringsmål"

    **Viden**

    - metoder til vurdering og efterprøvning af sikkerhedsmæssige foranstaltninger.

    **Færdighed**

    - anvende metoder til at identificere og analysere sikkerhedsmæssige svagheder i webapplikationer.
    - tolke og vurdere testresultater i forhold til kendte sikkerhedsprincipper.

    **Kompetencer**

    - gennemføre vurdering af sikkerheden i webapplikationer på baggrund af systematiske test.


!!! note "Praktiske mål"

    - Den studerende har udført et dictionary password angreb
    - Den studerende har udført et brute force password angreb (Kombinatorisk)
    - Den studerende har udført et Token manipulations angreb.


!!! note "Forberedelse"

    - Læs kapitel 8 i bogen "Hacking APIs"

## Opgave - Angreb på Autentificering & Password

!!! note "Opgave beskrivelse"

    1. Udfør øvelsen: [Dictionary attack med Burp Suite](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/5_basic_Authentication_Attacks.md#-dictionary-attack-with-burp-suite)
    1. Udfør øvelsen: [Dictionary attack med WFuzz](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/5_basic_Authentication_Attacks.md#-dictionary-attack-with-wfuzz)
    1. Udfør øvelsen: [Exhaustive brute force attack med Burp Suite](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/5_basic_Authentication_Attacks.md#-exhaustive-brute-force-attack-with-burp-suite)
    1. Udfør øvelsen: [Password spraying](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/5_basic_Authentication_Attacks.md#-password-spraying)
    1. Udfør øvelsen: [Brute forcing OTP](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/5_basic_Authentication_Attacks.md#-attacking-password-recovery--otp)
    1. Udfør øvelsen: [Brute forcing i Juice Shop](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/JuiceShop/5_basic_Authentication_Attacks.md#basic-authentication-attacks-against-juice-shop)

### Del opgave - Dictionary attack med Burp Suite

??? note "Opgave beskrivelse"

    1. Create a wordlist with 20 passwords of your own choosing that comply with the crAPI password policy.
    1. Create a user whose password is included in your wordlist.
    1. Capture a crAPI login request using Burp Suite.
    1. Send the request to Intruder (like sending it to Repeater).
    1. Go to the Intruder tab.
    1. Set Attack Type to Sniper.
    1. In the request body, set the email to match the user from step 2.
    1. Highlight the value of the password field and click Add.
    1. Switch to the Payloads tab.
    1. Set Payload Type to Simple list.
    1. Load your wordlist from step 1.
    1. ⚠️ Uncheck the "URL-encode these characters" box at the bottom. This prevents Burp from altering the password format.
    1. Click Start attack.
    1. Observe which request(s) return HTTP status 200 OK and confirm successful login.

Jeg startede med at starte crAPI containerne op, imens de startede lavede jeg en wordlist af passwords, hvor et af dem var det rigtige.

```txt
Usert1234!
Users1234!
Userr1234!
Userq1234!
Userp1234!
Usero1234!
Usern1234!
Userm1234!
Userl1234!
Userk1234!
Userj1234!
Useri1234!
Userh1234!
Userg1234!
Userf1234!
Usere1234!
Userd1234!
Userc1234!
Userb1234!
Usera1234!
```

Her er password nr. 20 det rigtige.
Jeg vælger at bruge Caido da burp kan være langsomt med community edition.

![alt text](image.png)

Her har jeg opfanget en fejlet login request, hvor `pass` er blevet markeret da jeg har lavet den til en placeholder for caidos automate. Jeg uploader derefter min wordlist af passwords til Caido, og vælger den som payload.

![alt text](image-1.png)

Den vil nu lave en login request med hvert password i listen.
Efter at starte brute force angrebet finder den det rigtige password efter 20 forsøg.

![alt text](image-2.png)

Det kan ses da forsøg nummer 20 har en `200 OK` i stedet for `401` som de andre hvor de fejler. Resultatet bliver at jeg bliver givet en Bearer token i en responce til den sidste request.

```json linenums="0"
{
    "token": "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ1c2VyQGEuY29tIiwiaWF0IjoxNzU5NzM1MDUzLCJleHAiOjE3NjAzMzk4NTMsInJvbGUiOiJ1c2VyIn0.goQKZS8JSNC760eod0DzpI86Ofcos7rBhRjiSU6EFhlkaLvp1T-WN8uZNYACc2GaQHPuKCzlF23S3Jig0T-zukxo9ETRdnclh5OSsZ0M1zDY8QaB_MzUrG3TD_QwpcYVBQo6bqvBJwDsfWAsmQtvnJ_qjZqHEtMPg92uB6mQCtssv7amXrGpZXnynpzdha9U67som-yfzMz9FnwcESv0PK2d0dEwevt7A-zD95lQnfsd33de8aLuStK5z-BRcbxjuvrM_hoCz3fZbS4r6VaP6n21DEaHs9zt8tRzjXvWLOIAaHFUSIZ0kVFj8fDcJ4wWTHr18tj8SHC-loYYAKDxnA",
    "type": "Bearer",
    "message": "Login successful",
    "mfaRequired": false
}
```

### Del opgave - Dictionary attack med WFuzz

??? note "Opgave beskrivelse"

    1. Create a crAPI user with a password found in rockyou.txt.
    2. Execute the dictionary attack using the following parameters:
        - Request body format: {"email": "<email>", "password": "<password>"}
        - Hide HTTP 401 responses.
        - Set Content-Type: application/json header.
        - Use rockyou.txt as the wordlist.


Jeg bruger kali linux via Windows WSL, og downloader rockyou.txt med denne kommando: `wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt`.

Laver en bruger "bob" med et password der er i `rockyou.txt`

prøver at bruge wfuzz men den får en fejl. Dette fixede det: `sudo apt install -y python3-setuptools python3-pip`

Efter at kigge i [dokumentationen](https://wfuzz.readthedocs.io/en/latest/user/basicusage.html) og lidt hjælp fra chatGPT så nåede jeg frem til en kommando der ser sådan ud: 

`wfuzz -z file,rockyou.txt -H "Content-Type: application/json" -d '{"email":"bob@bob.com","password":"FUZZ"}' http://127.0.0.1:8888/identity/ap
i/auth/login`

- -z er det payload men vil bruge. Her bruger jeg en fil.
- -H bruger jeg til at specificere en http header jeg vil bruge. Jeg bruger `Content-Type: application/json` da jeg gerne vil sende email og password som `JSON` i body message.
- -d bruger jeg til at definere POST data, som i dette tilfælde jo er `JSON`
- Så skriver jeg den URL som skal angribes

Her er resultatet:

```terminal linenums="0"
Target: http://127.0.0.1:8888/identity/api/auth/login
Total requests: 14344391

=====================================================================
ID           Response   Lines    Word       Chars       Payload
=====================================================================

000000007:   401        0 L      2 W        76 Ch       "1234567"
000000015:   401        0 L      2 W        76 Ch       "lovely"
000000031:   401        0 L      2 W        76 Ch       "friends"
000000034:   401        0 L      2 W        76 Ch       "angel"
000000001:   401        0 L      2 W        76 Ch       "123456"
000000030:   401        0 L      2 W        76 Ch       "anthony"
000000033:   401        0 L      2 W        76 Ch       "purple"
000000032:   401        0 L      2 W        76 Ch       "butterfly"
000000029:   401        0 L      2 W        76 Ch       "soccer"
000000003:   200        0 L      2 W        533 Ch      "Bob123456789!"
000000023:   401        0 L      2 W        76 Ch       "000000"
000000026:   401        0 L      2 W        76 Ch       "sunshine"
000000027:   401        0 L      2 W        76 Ch       "chocolate"
000000025:   401        0 L      2 W        76 Ch       "tigger"
000000021:   401        0 L      2 W        76 Ch       "111111"
000000028:   401        0 L      2 W        76 Ch       "password1"
```

Her kan man ses outputtet, hvor jeg får en `200 OK` da den forsøger at burge passworded `Bob123456789!`

### Del opgave - Exhaustive brute force attack med Burp Suite

??? note "Opgave beskrivelse"

    1. Use Postman to create a user with the password passwd (bypassing frontend validation, as shown in Exercise 4 - Endpoint Analysis).
    1. Capture the login request in Burp Suite.
    1. Send it to Intruder.
    1. Set the email to match the user created.
    1. Highlight the value of the password field and click Add.
    1. In Payload Type, select Brute forcer.
    1. Set character set to passwd.
    1. Set min and max length to 6.
    1. Observe the payload count and request count — this is the total number of combinations Intruder will try.
    1. Click Start attack and let it run.

Jeg bruger postman til at lave en bruger, da ved at ungå websidens UI kan man også ungå de password regler den har. hvilket gør at jeg kan lave en bruger med `passwd`, som ikke har store bogstaver, tal eller tegn.

![alt text](image-3.png)

Dernest fangede jeg en login request, som jeg så har sendt til intruder i burp suite, Da caido ikke har en ligende værktøj.

![alt text](image-4.png)

Jeg setter Charavter set til `passwd` og setter det til min og max 6 length. Efter at trykke start prøver den alle kombinationer af bogstaverne "passwd" ind til den bruger den rigtige kombination.

![alt text](image-5.png)

Viser ikke det sidste resultat, da brup comunity edition er meget langsomt, og ville tager alt for langt tid.

### Del opgave - Password spraying

??? note "Opgave beskrivelse"

    1. Create or reuse a crAPI user.
    1. Create a short wordlist of 5 likely passwords (include the one for the user created in step 1).
    1. Get user data from the EDE vulnerability found in [Exercise 2 in Exploting BOLA and Excessive data exposure](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/2_Exploiting_BOLA_And_Excessive_Data_Exposure.md) to gather 4 users email adresses.
    1. Add the email adress you created in step 1 along with the email adresses found in step 3 to a wordlist.
    1. Capture a login request and send to Intruder.
    1. Set Attack type to Cluster bomb
    1. Highlight the value of the `email` field and click Add. (This will be set 1 when you set the payload)
    1. Highlight the the value of the `password` field and click Add. (This will be set 2 when you set the payload)
    1. Set Payload Set 1 to the email wordlist. (There is a dropdown menu to select this in the payload tab)
    1. Set Payload Set 2 to the password list.
    1. Uncheck "URL-encode these characters" in both payloads.
    1. Click Start attack.
    1. Look for requests returning HTTP 200 OK.

Jeg går igennem alle steps og samler emails og passwords.

Jeg får lavet denne email liste:

```txt
user@c.com
user@f.com
robot001@example.com
user1@test.com
pogba006@example.com
adam007@example.com
bob@bob.com
```

Og denne password list.

```txt
Usert1234!
Users1234!
Userr1234!
Userq1234!
Bob123456789!
```

Jeg laver et cluster bomb angreb med brup. Først laver den fejl kun at disable "URL-encode these characters" for det ene payload. hvilket resultere i fejlet login ved alle muligheder. Ved at tjekke det af ved begge payloads fikser det problemet.

Når den starter prøver den at matche alle emails med alle passwords for at finde en eller flere der virker sammen. Som man kan se på bileldet her under så er det bobs account vi finder igen, da den retunere en `200 OK`.

![alt text](image-6.png)

### Del opgave - Brute forcing OTP

??? note "Opgave beskrivelse"

    - Step 1: Understand crAPI's OTP Password Recovery

        1. Create a user.
        1. Use the Forgot Password? feature.
        1. Input email and leave OTP page open.
        1. Open Mailhoq, get the OTP.
        1. Enter OTP and new password.
        1. Log in to confirm password reset.

            Expected Result: You’ve changed the user’s password using OTP.

    - Step 2: Test OTP Strength

        1. Request 3 new OTPs.
        1. Check if all are 4-digit numeric codes.

            Expected Outcome: All OTPs are weak, 4-digit numbers.

    - Step 3: Test OTP Brute Force Attempt

        1. In the browser, Request An OTP again.
        1. Enter wrong OTP in the browser, and capture request to /identity/api/auth/v3/check-otp.
        1. Resend 10x using Burp suite Repeater, and observe status change to 503.
        1. Check the error message.

            Note: While a 503 error is suppose to indicate a server issue, here it signals that the API has enforced a max-try lockout mechanism.

    - Step 4: Bypass with Legacy API Version

        1. Modify path from /v3/check-otp to /v2/check-otp.
        1. Send 10+ bad requests.
        1. Confirm no 503 response, meaning that v2 does not enforce limits.

            When no limits are enforced, we can try to brute for the OTP. OTP's are just passwords, and we know that 4 digit make for a weak password.

    - Step 5: Create OTP Wordlist

        We will create a wordlist with all posible OTP combination, from 0000 to 9999. This can be done with BASH with:

        ```shell
        for i in $(seq -f "%04g" 0 9999); do echo $i; done | iconv -f UTF-8 -t UTF-8 > wordlist.txt
        ```

        Or powershell with:

        ```powershell
        0..9999 | ForEach-Object { $_.ToString('D4') } | Out-File -FilePath wordlist.txt -Encoding utf8
        ```

    - Step 6: Brute Force OTP

        Burp suite community is "throttled", meaning it is slow. Alternative free tools like ZAP can be used. Before starting the brute force attemp, ensure a new otp flow is stared

        1. Start a new password recovery flow.
        1. Send the OTP check request with legacy path to /v2/check-otp, to Burp suite intruder.
        1. Use OTP wordlist to bruteforce the OTP.
        1. Look for a 200 OK response.

            Expected Outcome: OTP is brute-forced successfully and password is changed.

Jeg kunne godt ændre bobs password, og alle de OTP'er jeg efterspurgte have kun 4 cifre.

### Del opgave - Brute forcing i Juice Shop

??? note "Opgave beskrivelse"

    1. Intercept a login request in Juice Shop for the administrator.
    1. Use a brute-force tool such as Burp Suite Intruder.
    1. Set the email to `admin@juice-sh.op`.
    1. Use the `best1050.txt` wordlist as the payload for the password field.
    1. Launch the attack and observe which password returns a successful authentication (HTTP 200 OK).


## Opgave - Angreb på Autentificering & Tokens

!!! note "Opgave beskrivelse"

    1. Udfør øvelsen: [Introduction to JWT Tokens](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/6_Basic_Token_Attacks.md#-introduction-to-jwt-tokens)
    1. Udfør øvelsen: [Manipulating the JWT payload](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/crAPI/6_Basic_Token_Attacks.md#-manipulating-the-jwt-payload)
    1. Udfør øvelsen: [Basic Attack Against Authentication Tokens in Juice Shop](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/JuiceShop/6_Basic_Token_Attacks.md#-basic-attacks-against-authentication-tokens-in-juice-shop)

### Del opgave - Introduction to JWT Tokens

!!! note "Opgave beskrivelse"

    Go to [https://jwt.io/](https://jwt.io/) and perform the following using JWT Encoder:

    1. Change the value of `sub`. How drastically does the signature change?
    1. Change the value of `iat`. What happens to the signature?
    1. Copy and decode the JWT header in a base64 decoder. What metadata do you see?

1. Change the `sub`
    - The sub by default is set to `1234567890` which converts to `eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0`
    - Changing the value by removing `5` from it changes everything after `eyJzdWIiOiIxMjM0N` in the output.
2. Change the `iat`
    - The last part of the payload changes, and the entier signature is compleatly replaced.
3. Base64 decode the JWT header.
    - It gives me this decoded header. `{"alg":"HS256","typ":"JWT"}`

### Del opgave - Manipulating the JWT payload

!!! note "Opgave beskrivelse"

    As User A, log in and capture a GET request to the dashboard using Burp Suite.

    Notice with JWT editor installed, all request that contains a JWT token, is highligthed in green

    1. Send the request to Repeater.
    1. Switch to the JSON Web token tab.
    1. In the payload section, modify the email claim to use User B’s email.
    1. Click Send.
    1. Observe: the response now contains User B’s information.

    This indicates improper or missing validation of the JWT signature on the server side.

    Does This Work Everywhere?

    1. Capture a password update request and send it to Repeater.
    1. Replace the token with your modified one from earlier.
    1. Send the request.

    You should receive a 401 Unauthorized, indicating the backend correctly validates tokens in this case.

Jeg prøver at bruge Caido med et community plugin "JWT Analyzer".

Jeg fanger en `GET` request til Dashboard. `GET /identity/api/v2/user/dashboard`. Når man sender denne request får den et responce man forventer til bruger A's information.

```json linenums="0"
{
    "id": 11,
    "name": "User A",
    "email": "user@a.com",
    "number": "1234",
    "picture_url": null,
    "video_url": null,
    "video_name": null,
    "available_credit": 100090.0,
    "video_id": 0,
    "role": "ROLE_USER"
}
```

Jeg sender denne request til JWT Analyzer, som identifisere min JWT token med det samme.

![alt text](image-7.png)

Jeg sender så min token til editoren, hvor jeg ændre emailen til bruger B's email.

![alt text](image-8.png)

Der efter kopier jeg den nye JWT Token til min dashboard request og erstatter den originale Token. 

```json linenums="0"
{
    "id": 12,
    "name": "User B",
    "email": "user@b.com",
    "number": "12345",
    "picture_url": null,
    "video_url": null,
    "video_name": null,
    "available_credit": 100.0,
    "video_id": 0,
    "role": "ROLE_USER"
}
```

Efter at opfange en password reset request, og tilføje den modifiseret JWT Token, får jeg en `401` responce.
`CRAPIResponse(message = Invalid Token, status = 401)` Dette sker nu da dette API endpoint faktisk tjekker om den JWT Token den modtager faktisk er en gyldig Token.

### Del opgave - Basic Attack Against Authentication Tokens in Juice Shop

!!! note "Opgave beskrivelse"

    Token Validation

    1. Create or reuse a Juice Shop user account.
    1. Authenticate with that user and capture a GET request to /rest/user/whoami (with a 200 OK response, and at JWT token).
    1. Send the request to Burp Repeater.
    1. Inspect the request: note the Authorization token present in both the Header and Cookie.

    We notice that the token are included in both a header, and a cookie, so lets investigate which of the token are actaul used for validation in this path

    1. Modify the token in the Header by appending a character; resend and observe the response.
    1. Modify the token in the Cookie similarly; resend and observe the response.
    1. Try to Remove the Authorization header completely and resend; note if the response is still 200 OK, and what is the response?
    1. which token the does server use for validation on this request path?, and which does it use for autentication?
    1. Change the request back to its original state before moving on.

    JWT Payload Manipulation

    1. Using the JWT Editor tab in Burp Repeater, change the payload:
        - Set email to admin@juice-sh.op
        - Set id to 1 (We know from earlier, that user id's are given sequencelly)
    1. Resend the request with the modified token and observe the status code (likely 304).

    Using Unsigned Tokens

    1. In Burp Repeater’s JWT Editor, click Attack → none signing Algorithm to:
        - Set alg to none in the JWT header
        - Removes the signature entirely, and sets header alg to None (token format: <header>.<payload>.)
    1. Send the unsigned token request and confirm you receive a 200 OK response.
    1. Save this unsigned token admin for subsequent steps.

    Privilege Escalation: Changing Admin Password

    1. Capture a password change request and send it to Repeater.
    1. Replace the token in the Authorization header and Cookie with the unsigned admin token.
    1. Send the request and confirm a 200 OK response.
    1. Extract the MD5 hashed password from the response, crack it (e.g., crackstation.net), and verify it matches your chosen password.
    1. Log in as the Juice Shop administrator using the new password.
