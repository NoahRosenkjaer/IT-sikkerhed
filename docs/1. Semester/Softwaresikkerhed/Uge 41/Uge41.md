# Domæne primitiver, samt 3. parts sårbarheder.

!!! note "Læringsmål"
    
    **Viden**

    - Den studerende har viden og forståelse for security design principper (Domæne primitiver)
    - Den studerende har viden om Kriterier for programkvalitet (Kode kvalitet med domæne primitiver)

    **Færdigheder**

    - Den studerende kan definere lovlige og ikke-lovlige input data. (Invarians i domæne primitiver)
    - Den studerende kan bruge et API og/eller standard bibliotek.
    - Den studerende kan opdage og forhindre sårbarheder i programkoder (Statisk kode analyse)

    **kompetencer**

    - Den studerende kan håndter risikovurdering af programkode (F.eks. mangelende struktur grundet manglende domæne primitiver)

!!! note "Praktiske mål"

    - Den studerende kan implementer en domæne primitive.
    - Den studerende kan udføre en analyse af 3. Parts sårbarheder.

!!! note "Forberedelse"

    - Læs Kapitel 5 i bogen “Secure by design”

## Opgave - Grundlæggende øvelse med domæneprimitiver

!!! note "Opgave beskrivelse"

    - Opret en ny .NET-konsolapplikation.
    - Opret et domæneprimitiv for fornavn. Fornavn må kun indeholde alfabetiske tegn og skal have en længde på mellem 2 og 20 karakterer.
    - Opret et domæneprimitiv for efternavn. Efternavn må kun indeholde alfabetiske tegn og skal have en længde på mellem 2 og 20 karakterer.
    - Opret et domæneprimitiv for alder. Alderen skal være mellem 18 og 99.
    - Opret et domæneprimitiv for CPR-nummer. CPR-nummeret skal overholde syntaksen for et dansk CPR-nummer (kun syntaksen, køn kan du undlade).
    - Opret en GetValue-metode i alle domæneprimitiver, således at værdien kan udlæses (hvis du ikke allerede har gjort det).
    - Opret en Person-klasse, der indeholder et private field for hver af de fire domæneprimitiver.
    - Lad konstruktøren i Person-klassen tage imod et argument for hver af de fire domæneprimitiver og brug argumenterne til at initialisere de private fields.
    - Lav en GetFirstname, GetLastname, GetAge, GetCprNumber-metode, og lad dem returnere værdien af domæneprimitivet (husk at bruge GetValue-metoden).
    - Opret et Person-objekt i konsolapplikationen og udskriv alle fire værdier.
    - (Ekstra) CPR-nummer er følsomme data. Implementer domæneprimitivet til CPR-nummer med Read Once Pattern (se afsnit 5.2 i bogen Secure by Design).
    - (Ekstra) Lav invariansen i domæneprimitivet til CPR-nummer, således at CPR-nummeret passer med personens køn.


Jeg har lavet 2 filer, den ene er til klasserne, og den anden er til selv programmet.
Resultatet bliver at man tilføjer værider, til at person objekt, og de bliver alle retuneret i en tuple.

Classes.cs
```csharp
using System.Text.RegularExpressions;

namespace Classes;
public class FirstName
{
    private string name;

    public FirstName(string name)
    {
        IsNameValid(name);
        this.name = name;
    }

    public string GetValue()
    {
        return name;
    }

    private void IsNameValid(string name)
    {
        if (name.Length < 2)
        {
            throw new ArgumentException("Name must be longer than 2 characters");
        }

        if (name.Length > 20)
        {
            throw new ArgumentException("Name must be less than 20 characters");
        }

        var pattern = new Regex(@"^[a-zA-ZæøåÆØÅ]+");
        if (pattern.IsMatch(name))
        {
            return;
        }
        else
        {
            throw new ArgumentException("Name must be an alphabetic character");
        }
    }
}

public class LastName
{
    private string name;

    public LastName(string name)
    {
        IsNameValid(name);
        this.name = name;
    }

    public string GetValue()
    {
        return name;
    }

    private void IsNameValid(string name)
    {
        if (name.Length < 2)
        {
            throw new ArgumentException("Name must be longer than 2 characters");
        }

        if (name.Length > 20)
        {
            throw new ArgumentException("Name must be less than 20 characters");
        }

        var pattern = new Regex(@"^[a-zA-ZæøåÆØÅ]+");
        if (pattern.IsMatch(name))
        {
            return;
        }
        else
        {
            throw new ArgumentException("Name must be an alphabetic character");
        }
    }
}

public class Age
{
    // Private field that is immutable and an invariant
    private int age;

    // Constructor that accepts an argument and upholds invariance
    public Age(int age)
    {
        IsAgeValid(age);
        this.age = age;
    }

    // Method to get the value of the Age
    public int GetValue()
    {
        return age;
    }

    // Private method to validate age invariant
    private void IsAgeValid(int age)
    {
        if (age < 18)
        {
            throw new ArgumentException("Age cannot be less than 18");
        }

        if (age > 99)
        {
            throw new ArgumentException("Age cannot be more than 99");
        }
    }
}

public class CPR
{
    private string cpr;

    public CPR(string cpr)
    {
        IsCPRValid(cpr);
        this.cpr = cpr;
    }

    public string GetValue()
    {
        return cpr;
    }

    private void IsCPRValid(string cpr)
    {
        var pattern = new Regex(@"^(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])\d{2}-?\d{4}$");
        if (pattern.IsMatch(cpr))
        {
            return;
        }
        else
        {
            throw new ArgumentException("The CPR number does not match the pattern");
        }
    }
}

public class Person
{
    // Private field that holds Age object, immutable and upholds invariance
    private Age age;
    private FirstName firstName;
    private LastName lastName;
    private CPR cpr;

    // Constructor that accepts Age object and checks for null
    public Person(Age age, FirstName firstName, LastName lastName, CPR cpr)
    {
        if (age == null)
        {
            throw new ArgumentNullException("Age cannot be null");
        }
        this.age = age;

        if (firstName == null)
        {
            throw new ArgumentException("Firstname must not be NULL");
        }
        this.firstName = firstName;

        if (lastName == null)
        {
            throw new ArgumentException("Lastname must not be NULL");
        }
        this.lastName = lastName;

        if (cpr == null)
        {
            throw new ArgumentException("CPR number must not be NULL");
        }
        this.cpr = cpr;
    }

    public (string, string, int, string) GetValue()
    {
        return (firstName.GetValue(), lastName.GetValue(), age.GetValue(), cpr.GetValue());
    }
}
```

Program.cs
```csharp
using System;
using Classes;

var age = new Age(22);
var firstName = new FirstName("Noah");
var lastName = new LastName("Rosenkjær");
var cpr = new CPR("200900-1234");


var person = new Person(age, firstName, lastName, cpr);

Console.WriteLine(person.GetValue());
```