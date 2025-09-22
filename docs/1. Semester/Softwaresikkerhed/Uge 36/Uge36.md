# Introduktion til faget og grundlæggende OOP

!!! note "Praktiske mål"

    - At den studerende er bekendt med fagets læringsmål.
    - At den studerende har forståelse for fagets formål.
    - At den studerende har forståelse for grundlæggende OOP.

!!! note "Læringsmål"

    Idag fokuseres der primært på hvad faget handler om, og genopfriskning af grundlæggende programmering.

!!! note "Forberedelse"

    Ingen forberedelse til i dag.

## Opgave - Hvad er software?

!!! note "Opgave beskrivelse"

    Sammen i gruppen skal I diskutere følgende spørgsmål:

    1. Hvad er software?
        - Formulér en definition, som hele gruppen er enige om.
    2. Hvad er forskellen på software og hardware?
        - Nævn fordele og ulemper ved software.
    3. Hvilke egenskaber bør en softwareimplementering have, hvis den F.eks. skal være:
        - Nem at ændre
        - Sikker at ændre
        - Tilgængelig og forståelig for skiftende udviklere

1. Hvad er software?
    - Et værktøj til at styre/ændre hardwarens funktion
    - En eller flere processer der fortæller hardware hvad der skal gøres og i hvilken rækkefølge

2. Nævn fordele og ulemper ved software.
    - Fordele
        - Ændres hurtigt
        - Kan erstattes, indsættes og slettes forholdsvist smertefrit, i forhold til hardware some har fysiske limitationer.
        - Dynamisk 
    - Ulemper
        - Introducerer en større angrebsflade

3. Hvilke egenskaber bør en softwareimplementering have, hvis den F.eks. skal være:
    - Nem at ændre
        - Koden skal være abstrakt/afkoblet nok at man kan tilføje ændringer uden at skulle omskrive eksisterende kode
    - Sikker at ændre
        - Der skal være fejlhåndteringer og testing af kode
        - Input skal “sanitizes” og valideres
        - Data og brugerinformation skal krypteres i bevægelse og gemmes sikkert
        - Brugere skal autoriseres
    - Tilgængelig og forståelig for skiftende udviklere
        - Koden skal have dokumentation
        - Koden skal overholde clean code princippet (selvsigende, ingen magic numbers osv.)


## Opgave - Hvad er sikkerhed?

!!! note "Opgave beskrivelse"

    Sammen i gruppen skal I diskutere følgende spørgsmål:

    1. Hvad er sikkerhed?
        - Formulér en definition, som hele gruppen er enige om.
    2. Hvornår er der behov for sikkerhed?
        - Giv eksempler på situationer, hvor sikkerhed er vigtig.
        - Giv eksempler på situationer, hvor sikkerhed er mindre vigtig
        - Diskutér, hvorfor behovet for sikkerhed er forskelligt i forskellige kontekster.
    3. Hvad sker der, hvis man undervurderer behovet for sikkerhed?
        - Hvilke konsekvenser kan det få? For individ, organisation eller samfund?

1. Definer sikkrhed
    - At være beskyttet mod en trussel
    - En tilstand der forhindre fare eller ubehag
2. Hvornår er er behov for sikkerhed
    - Giv eksempler på situationer, hvor sikkerhed er vigtigt
        - Sikkerhed er vigtigt når der er en risiko
    - Giv eksempler på situationer, hvor sikkerhed er mindre vigtigt
        - Når der ikke er nogen form for fare eller risiko
    - Diskuter, hvorfor behovet for sikkerhed er forskelligt i forskellige kontekster.
        - Det kommer an på hvor stor risici der er
3. Hvad sker der, hvis man undervurderer behovet for sikkerhed?
    - Hvilke konsekvenser kan de få? For individ, organisation eller samfund?
        - Individer kan komme til skade, kan få lækket sensitiv information, misledt og svindlet. 
        - Organisationer kan blive svindlet, gå konkurs, få bøder eller komme i retten. 
        - Samfundets helbred, velvære og udvikling kan påvirkes.


## Opgave - Fagets læringsmål

!!! note "Opgave beskrivelse"

    Noter alle besvarelser!

    1. For hvert læringsmål:
        - Diskutér i gruppen hvad det betyder
        - Notér en kort fortolkning eller oversættelse til jeres egne ord
    2. Sammenlign læringsmålene fra Software sikkerhed med dem fra It-sikkerhed i webapplikationer.
        - Notér eventuelle overlap eller fælles fokusområder
    3. Find og notér:
        - Afleveringsdato for eksamensrapporten i Software sikkerhed
        - Datoen for den mundtlige eksamination (Tjek [semesterbeskrivelsen for 1. og 2. semester](https://esdhweb.ucl.dk/D25-2977210.pdf) – Efterår 2025)

**Viden**

Den studerende har viden om: 

- Hvilken betydning programkvalitet har for it-sikkerhed ift.: 
    - Stor betydning: Dårlig kode kvalitet skaber fejl og uforudsigelige huller som kan udnyttes
- Trusler mod software 
    - At man har viden om forskellige angreb vektorer og hvordan software kan udnyttes
- Kriterier for programkvalitet 
    - At man har viden kode principper der understøtter programkvalitet
- Fejlhåndtering i programmer 
    - At man har viden om fejlhåndtering af bugs og fejl i koden
- Forståelse for security design principles, herunder: 
    - Viden om security design principper såsom security by design og privacy by design

**Færdigheder** 
Den studerende kan tage højde for sikkerhedsaspekter ved at:

- Programmere håndtering af forventede og uventede fejl 
    - At kunne programmere exception-handling
- Definere lovlige og ikke-lovlige input data, bl.a. til test 
    - At kunne sanitære og input validere
- Bruge et API og/eller standard biblioteker
    - At kunne brug en API og code libraries
- Opdage og forhindre sårbarheder i programkoder 
    - At kunne se sårbarheder i kode
- Sikkerhedsvurdere et givet software arkitektur 
    - At kunne vurdere software arkitekturen ud fra kvalitet og struktur såsom abstraktion og principper

**Kompetencer** 

Den studerende kan:

- Håndtering risikovurdering af programkode for sårbarheder. 
    - Både kunne finde sårbarheder, udarbejde risikovurdering for programkode


## Opgave - Regular expression

!!! note "Opgave beskrivelse"

    1. Lav en regular expression, som kan detektere mønsteret for et dansk CPR-nummer.
        - Overvej: Hvad kendetegner et CPR-nummer? Hvilket format skal din regex finde?
    2. Skriv et eksempel i C#, hvor du bruger din regex til at validere et CPR-nummer.
        - Du skal blot skrive selve koden – det behøver ikke kunne eksekveres.
    3. Test dit mønster med Regex101
        - Brug testdata og justér, hvis det ikke virker som forventet.

1. regular expression
    - Jeg startede med at lave et mønster (med [Regex101](https://regex101.com/)) som godtog tal mellem 0 pg 9, 6 gange så en bindestreg og så 4 tal mellem 0 og 9. Den endte med at se sådan ud: `\d{6}-\d{4}`
    - Også selv om den virkede fint, så kom jeg i tanke om at der ikke må være mere end 12 for måneder, og max 31 dage på en måned. derfor endte jeg med denne: 
    
        `(0[0-9]|[12][0-9]|3[01])[01][0-2]\d{2}-\d{4}`

2. eksempel i C#
    - Efter jeg fik mit regex mønster på plads, skrev jeg lidt C# kode til at teste det med C# og forstå C# lidt mere. Koden kan ses her under:

```csharp
using System.Text.RegularExpressions;

// Definer regex pattern, som bare tager alle tal
//string pattern = @"\d{6}-\d{4}";

// Denne tager højde for at der er 12 måneder, og max 31 dage på en måned.
string pattern = @"(0[0-9]|[12][0-9]|3[01])[01][0-2]\d{2}-\d{4}";

// Start en regex instans?
Regex regex = new Regex(pattern);

// Sprøg brugeren om deres CPR nummer
Console.WriteLine("Indtast dit CPR nummer for a validere: ");
string? user_input = Console.ReadLine();

// Tjek om inputtet er null
if (user_input != null)
{
    // Match
    if (regex.IsMatch(user_input))
    {
        Console.WriteLine("Det er et CPR nummer!");
    }
    else
    {
        Console.WriteLine("Det matcher ikke CPR nummer formatet");
    }
}
```
## Opgave - Grundlæggende OOP med C\#

!!! note "Opgave beskrivelse"

    Denne opgave tager udgangspunkt i [Tutorial: Introduktion til klasser i C# (Microsoft)](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/tutorials/classes) 

    1. Gennemfør tutorialen ved at implementere en konsolapplikation
    2. Brug læseguiden nedenfor til at reflektere over nøglebegreber i hvert afsnit

??? note "Fuld kode"

    BankAccount

    ```csharp
    namespace Classes;

    public class BankAccount
    {
        private static int s_accountNumberSeed = 1234567890;
        public string Number { get; }
        public string Owner { get; set; }
        public decimal Balance
        {
            get
            {
                decimal balance = 0;
                foreach (var item in _allTransactions)
                {
                    balance += item.Amount;
                }

                return balance;
            }
        }

        public BankAccount(string name, decimal initialBalance)
        {
            Number = s_accountNumberSeed.ToString();
            s_accountNumberSeed++;

            Owner = name;
            MakeDeposit(initialBalance, DateTime.Now, "Initial balance");
        }

        private List<Transaction> _allTransactions = new List<Transaction>();

        public void MakeDeposit(decimal amount, DateTime date, string note)
        {
            if (amount <= 0)
            {
                throw new ArgumentOutOfRangeException(nameof(amount), "Amount of deposit must be positive");
            }
            var deposit = new Transaction(amount, date, note);
            _allTransactions.Add(deposit);
        }

        public void MakeWithdrawal(decimal amount, DateTime date, string note)
        {
            if (amount <= 0)
            {
                throw new ArgumentOutOfRangeException(nameof(amount), "Amount of withdrawal must be positive");
            }
            if (Balance - amount < 0)
            {
                throw new InvalidOperationException("Not sufficient funds for this withdrawal");
            }
            var withdrawal = new Transaction(-amount, date, note);
            _allTransactions.Add(withdrawal);
        }

        public string GetAccountHistory()
        {
            var report = new System.Text.StringBuilder();

            decimal balance = 0;
            report.AppendLine("Date\t\tAmount\tBalance\tNote");
            foreach (var item in _allTransactions)
            {
                balance += item.Amount;
                report.AppendLine($"{item.Date.ToShortDateString()}\t{item.Amount}\t{balance}\t{item.Notes}");
            }

            return report.ToString();
        }
    }
    ```

    Transaction

    ```csharp
    namespace Classes;

    public class Transaction
    {
        public decimal Amount { get; }
        public DateTime Date { get; }
        public string Notes { get; }

        public Transaction(decimal amount, DateTime date, string note)
        {
            Amount = amount;
            Date = date;
            Notes = note;
        }
    }
    ```

    Program

    ```csharp
    using Classes;

    var account = new BankAccount("Noah", 1000);
    Console.WriteLine($"Account {account.Number} was created for {account.Owner} with {account.Balance} initial balance.");

    account.MakeDeposit(751, DateTime.Now, "Løn");
    account.MakeWithdrawal(500, DateTime.Now, "Rent");
    Console.WriteLine($"{account.GetAccountHistory()}");
    ```

    Program output

    ```Terminal
    Account 1234567890 was created for Noah with 1000 initial balance.
    Date            Amount  Balance Note
    05/09/2025      1000    1000    Initial balance
    05/09/2025      751     1751    Løn
    05/09/2025      -500    1251    Rent
    ```

- Hvad er `Number`, `Owner` og `Balance`?
    - De er alle properties eller egenskaber. De er lidt lige som normale variable, men man kan definere validation eller regler til dem, sådan så `Owner` ikke kan settes til null eller en tom string. 
- Hvad gør metoderne `MakeDeposit` og `MakeWithdrawal`?
    - `MakeDeposit`: Denne metode gør at man kan indsette penge på kontoen.
    - `MakeWithdrawal`: Denne metode gør at man kan trække penge fra kontoen.
- Hvorfor omtales klasser også som typer?
    - Fordi de er typer, i C\# er classer en måde at opfinde nye typer. I dette tilfælde definere jeg et nyt variabel med typen BankAccount på lije 3 i Program. Den BankAccount type er lige som alle de andre basale typer: (int, string, bool, osv.). Så klasser udvider C\#'s funktionalitet, ved at lade dig opfinde dine egne typer. 

- Hvorfor bruge en konstruktør med parametre?
    - Så man kan definere `Number`, `Owner` og `Balance` når man starter den. Ellers ville den ikke vide Hvem er ejer kontoen, eller hvor maget der skal insettes på den til at starte med.
- Kan objektet oprettes uden parametre?
    - Nej, da konstruktøren er lavet med parametre, skal de gives.
- Hvad betyder det, at s_accountNumberSeed er privat?
    - Det betyder at den kun kan blive tilgået af koden inde i BankAccount klassen. Så man kan ikke bruge `account.s_accountNumberSeed`.

- Hvad er fordelen ved at transaktioner har deres egen klasse?
    - Det kunne gøre det lettere at ændre/udvide i senere, da det er seperart fra BankAccount.
    - Det er nemt at have alle informationerne et sted.
- Hvorfor er listen allTransactions privat?
    - Så kun BankAccount kan se og ændre listen.
    - Det er mere sikkert, så nye logs bliver lavet på den måde det er beregnet til.
- Hvad sker der, hvis der kastes en ArgumentOutOfRangeException?
    - Programmet stopper med at eksikvere den kode blok, og contol går tilbage til det sidste catch block. Det bruges til at teste, lige som i guiden hvor man tester for om man kan lave en negativ deposit. Hvor man bruger try-catch. 
- Hvorfor kaldes MakeDeposit fra konstruktøren?
    - Så når en account bliver lavet, setter den de 1000 ind på kontoen med det samme.

- Hvordan anvendes allTransactions?
    - `_allTransactions` er en liste over allTransactions, og den anvendes i `Balance`, hvor den bliver loopet over for at hente alle `Amount` i listen, for at legge dem sammen til at få den nuværende balance.
- Hvorfor er det en god idé at holde transaktionerne private?
    - Det er mere sikkert, så nye logs bliver lavet på den måde det er beregnet til. Hvis man kunne tilgå den fra Program kunne man helt undgå at, det tjek for om noget er lig med eller under 0. hvilket kunne ødelægge programmet.