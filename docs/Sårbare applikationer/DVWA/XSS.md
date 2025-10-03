# XSS

## Vulnerability: Reflected Cross Site Scripting (XSS)

Denne sårbarhed er en cross site scripting (XSS) sårberhed. "reflected" betyder at det man skriver bliver vist på siden på den ene eller den anden måde. 

![alt text](image-2.png)
Den viser hvad end man skriver i feltet.

Jeg prøver at skrive `<script>alert("test")</script>` hvilket virker perfekt.

![alt text](image-3.png)

Grunden til dette virker er at alt der bliver skrevet i fltet bliver reflekteret direkte i HTML.

Når jeg skriver mit navn i feltet så kommer sidens HTML til at se sådan ud. `<pre>Hello Noah</pre>`. Da der ikke er nogen form for validering eller sanitering af det bruger supleret input, så kan man også skrive HTML, og dermed og så Java script.

Jeg prøver som sagt før at bruge `<script>alert("test")</script>`,
Hvilket får sidens HTML til at se sådan ud: `<pre>Hello <script>alert("test")</script></pre>`. Her nester jeg nogle `<script>` tags inde i `<pre>` tags. Script tags gør at man kan køre java script direkte inde i sidens HTML. Jeg køre så `alert("Test")` som får siden til at køre en alert funktion.

Jeg kan ændre mit payload lidt og vise min session cookie.
`<script>alert(document.cookie)</script>`
![alt text](image-4.png)

## Vulnerability: Stored Cross Site Scripting (XSS)

Dett er også Cross Site Scripting, men det er en anden version eller type. Stored XSS betyder at det man skriver, bliver gemt. Det kunne være at men bruger customer supoprt, og sender en ticket, som så bliver gemt på firmaets support side. Den er så gemt indtil en supporter åbner din ticket, hvor hvad end Java script payload venter på at bliver eksikveret i deres browser.

![alt text](image-5.png)

Eksemplet er en guestbook, hvor alt man sender bliver gemt. hvis man reloader siden kan man stadig se mit "init test".

Jeg prøver at give den det samme payload fra sidste opgave: `<script>alert(document.cookie)</script>`

Dette virker som den giver mig min session cookie i en alert.
![alt text](image-4.png)

Efter man trykker på "OK" så kan man se at det payload ikke bliver vist, efter koden blev kørt, ved "Testing"

![alt text](image-6.png)

Nu bliver koden kørt igen og igen, hver gang man åbner den side.

## Vulnerability: DOM Based Cross Site Scripting (XSS)

DOM baseret XSS betyder at der er javascript kode som bruger input som er kontrolleret af brugeren.
Lige som i dette tilfælde hvor det er et URL parameter som er sårbart.

Når man åbner siden `http://IP:1335/vulnerabilities/xss_d/` bliver man mødt af en drop down menu hvor man kan vælge sproget siden bruger.
![alt text](image.png)

Efter at trykke "select" Bliver man redirected til den samme side, men det bliver tilføjet et parameter i enden af URL'en, som får hele URL'en til at se sådan ud `http://IP:1335/vulnerabilities/xss_d/?default=English`. 

En dropdown menu kan gøre applikationen mere sikker ved at give brugeren en rekke valgmuligheder at vælge i mellem, så man er sikker på at få noget data ind som applikationen kan håndtere. Men her bliver det valg faktisk reflekteret i enden af URL'en, hvilket giver brugeren mulighed for at ændre i værdien af `default` parameteret. Ved at indsette det samme payload som tideligere `<script>alert(document.cookie)</script>` får vi en URL der ser sådan ud `http://IP:1335/vulnerabilities/xss_d/?default=<script>alert(document.cookie)</script>`. Efter at requeste siden med dette parameter resultere det i at siden tager inputtet som blev givet og da det var javascript, så bliver det eksikveret i browseren. 

![alt text](image-1.png)