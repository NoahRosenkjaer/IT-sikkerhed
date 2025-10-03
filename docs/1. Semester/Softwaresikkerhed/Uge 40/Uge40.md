# Input validering & Sikker kode konstruktion.

!!! note "Læringsmål"
    
    **Viden**

    - Den studerende har viden om security by design (Input validering og objekt invariance)

    **Færdigheder**

    - Den studerende kan definerer lovlige og ikke lovlig input data
    - Den studerende kan bruge/anvende et standard API og/eller bibliotek.

    **Kompetencer**

    - Den studerende kan Håndterer risikovurdering af programkode for sårbarheder.

!!! note "Praktiske mål"

    - Hver studerende har defineret tilladt input med Regular expression i C#
    - Hver studerende har identificeret et objekt der er mutable og et objekt der ikke er mutable
    - Hver studerende har implementeret håndteringen af invarians i et objekt.

!!! note "Forberedelse"

    - Læs Kapitel 4 i bogen ”Secure by design” (Undtaget 4.1 Immutability)
        Forfatteren nævner “changing state”  et par gange. Her skal det påpeges at det kan betyde (og ofte gør i denne kontekst) ændring af værdien på objekts medlems variabler.

        Failfast betyder essentielt at fejl skal afvikles (F.eks. med en exception) lige så snart de detekteres. I samhæng med kapitel 4, betyder det at der skal smides en exception lige så snart en kontrakt ikke overholdes.
     
    - Du skal Havde de brugs og misbrugstilfælde, risikovuderinger samt trusselsmodelleringen som jeres gruppe lavet i uge 38 klar, da de skal bruges til peer review. 

## Opgave - Introduktion til Regex i C\#

!!! note "Opgave beskrivelse"

    1. Opret en ny .NET konsolapplikation kaldet `BasicRegexUsage`.
    1. Følg og implementer eksemplerne i [tutorialen](https://www.csharptutorial.net/csharp-regular-expression/csharp-regex/).
    1. Eksperimentér med koden ved at ændre Regex-udtryk og test resultatet — prøv fx at ændre mønstre og inputstrenge for at se, hvordan det påvirker valideringen.

Jeg ændrede lidt i koden, men vi har allerede gennemgået en mere komplekst eksempel med regex, hvor vi skulle validere CPR-nummer strukture, [her](../Uge%2036/Uge36.md#opgave-regular-expression). Men her er koden til denne opgave som jeg har ændret lidt.

```csharp
using System.Text.RegularExpressions;
using static System.Console;


var message = "I have 2 apples, 7 dogs, and 100 USD";
var pattern = @"\d";

var matches = Regex.Matches(message, pattern);

foreach (var match in matches)
{
    Console.WriteLine(match);
}
```

## Opgave - Inputvalidering til konsolapplikation

!!! note "Opgave beskrivelse"

    Denne opgave er baseret på dette [repo](https://github.com/mesn1985/InputValidationsBasicExercises)

    1. Valider, at navnet (nameInput) ikke er længere end 20 tegn.
    1. Valider, at navnet ikke er kortere end 3 tegn.
    1. Valider, at navnet kun indeholder alfabetiske karakterer ved hjælp af Regex (brug ikke andre metoder til dette).
    1. Test valideringen ved at køre applikationen og prøve forskellige inputs.
    Tip: Sørg for at validere længden, inden du bruger Regex på inputtet.

Først brugte jeg regex til både at sørge for at der kun er bogstaver, og sørge for at navnet er over 3 og under 20 tegn.

```csharp
//-- snippet --

static bool nameInputIsvalid(string? nameInput)
{
    //insert validation code here.
    if (string.IsNullOrWhiteSpace(nameInput))
    {
        return false;
    }
    
    if (nameInput.Length < 3)
    {
        return false;
    }
    
    if (nameInput.Length > 20)
    {
        return false;
    }

    var pattern = new Regex(@"^[a-zA-Z]+$");
    var result = pattern.IsMatch(nameInput);
    return result;
}
//-- snippet --
```

Kode beskrivelse:

- Tjek om input er `NULL` eller whitespace
- Tjek om input er mindre end 3
- Tjek om input er større end 20
- Brug regex til at tjekke om der er andet end bogstaver.

## Opgave - Inputvalidering i en webapplikation

!!! note "Opgave beskrivelse"

    1. Valider, at navnet i argumentet nameInput ikke er længere end 20 tegn.
    1. Valider, at navnet i argumentet ikke er kortere end 3 tegn.
    1. Valider, at navnet kun indeholder alfabetiske karakterer ved hjælp af Regex (brug ikke andre metoder til dette).
    1. Test valideringen ved at køre applikationen og prøve forskellige inputs.
    Tip: Sørg for at validere længden, inden du bruger Regex på inputtet.

Jeg bruger det samme kode som sidste opgave.

```csharp
//-- snippet --

private Boolean NameIsValid(string name)
{
    //Insert logic for name validation here, and return the correct boolean value true/false
    if (string.IsNullOrWhiteSpace(name))
    {
        return false;
    }

    if (name.Length < 3)
    {
        return false;
    }
    
    if (name.Length > 20)
    {
        return false;
    }
    
    var pattern = new Regex(@"^[a-zA-Z]+$");
    var result = pattern.IsMatch(name);
    return result;
}
//-- snippet --
```

## Opgave - Exceptions i C\#

!!! note "Opgave beskrivelse"

    1. Opret en ny .NET konsolapplikation.
    1. Følg og implementer [tutorialen](https://www.csharptutorial.net/csharp-tutorial/csharp-throw-exception/).
    1. Prøv at oprette et Circle-objekt med negativ radius, samt fjerne try & catch fra koden. (Dette vil lave det, som hedder en uncaught exception.)


Hvis jeg udkommentere dette stykke koder under, er koden lige glad om den input radius er positiv eller negativ.

```csharp
//-- snippet --
if (radius <= 0)
{
    throw new ArgumentOutOfRangeException(nameof(radius),
    "The radius should be positive"
    );
}
//-- snippet --
```

I dette lille eksempel gør det ingen forskel da minus gange minus giver plus.

Jeg prøvede også at fjerne det `try catch` der ligger længere nede i koden så får jeg en uncaught exception

```Terminal
Unhandled exception. System.ArgumentOutOfRangeException: The radius should be positive (Parameter 'radius')
```

## Opgave - Opretholdelse af invarians med konstruktøren

!!! note "Opgave beskrivelse"

    1. Opret en ny konsolapplikation i C#.
    1. Opret en ny klasse ved navn Person.
    1. Opret to private fields i klassen: firstname og lastname, begge af typen string.
    1. Implementer klassens konstruktør, som tager imod to string-argumenter og initialiserer de private fields.
    1. Håndhæv invariansen i konstruktøren ved at validere, at firstname og lastname ikke er null og opfylder de samme regler som i Opgave 18 – Inputvalidering i konsolapplikation. Hvis reglerne ikke er overholdt, skal der kastes en exception.
    1. Lav en metode GetFirstName, som returnerer værdien af firstname.
    1. Lav en metode GetLastName, som returnerer værdien af lastname.
    1. Opret en instans af Person med gyldige værdier for for- og efternavn.
    1. Udskriv navnene i konsollen.

Efter at gå igennem alle opgavens trin, er jeg nået frem til dette:

```csharp
public class Person
{
    private readonly string firstname;
    private readonly string lastname;

    public Person(string firstname, string lastname)
    {
        // Invariance
        if (string.IsNullOrEmpty(firstname))
            throw new ArgumentException("firstname cannot be null or empty");
        // Invariance
        if (string.IsNullOrEmpty(lastname))
            throw new ArgumentException("lastname cannot be null or empty");

        this.firstname = firstname;
        this.lastname = lastname;
    }

    public string GetFistName()
    {
        return firstname;
    }
    public string GetLastName()
    {
        return lastname;
    }
}

class Program
{
    public static void Main(string[] args)
    {
        var person = new Person("Noah", "Rosenkjær");
        Console.WriteLine($"Hello {person.GetFistName()} {person.GetLastName()}");
    }
}
```

Output:
`Hello Noah Rosenkjær`



## Opgave - Opretholdelse af objekters integritet med invarians i webapplikationer

!!! note "Opgave beskrivelse"


    1. Inspicer metoden `ValidateName` i filen `NameController.cs`. Hvorfor oprettes der et nyt objekt med værdierne fra det modtagne DTO-objekt `person`?
    1. Åbn filen `Person.cs`, som kan findes i mappen Models.
    1. Implementer håndhævelsen af invarians for de to argumenter i `Person`-konstruktøren. (Reglerne er de samme som fra tidligere øvelser.)
    1. Afprøv applikationen, og valider med forskellige inputs.
    1. Bemærk, at den eneste regel, inputvalideringen håndhæver, er, at data skal være sat [Notnull].
    1. Hvad sker der, når du forsøger med f.eks. et navn på 21 karakterer?

- Hvorfor oprettes der et nyt objekt med værdierne fra det modtagne DTO-objekt person?
    - Ikke sikker
- Implementer håndhævelsen af invarians for de to argumenter i Person-konstruktøren. (Reglerne er de samme som fra tidligere øvelser.)

    ```csharp
    private void isFirstNameValid(string name)
    {
        if (string.IsNullOrEmpty(firstname))
            throw new ArgumentException("firstname cannot be null or empty");
        ///Add Invariance validation Here
        /// Throw an Exception if the name is invalid
    }
    private void isLastNameValid(string name)
    {
        if (string.IsNullOrEmpty(lastname))
            throw new ArgumentException("lastname cannot be null or empty");
        ///Add Invariance validation Here
        /// Throw an Exception if the name is invalid
    }
    ```