# Python programmering

!!! note "Forberedelse"

    - Læs undervisningsplanen og øvelser
    - Læs kapitel 5 – Udvikling af sikker software, i "IT-Sikkerhed i praksis".
    - Hvis du ikke har brugt Python før, eller har brug for en genopfrisker så brug lidt tid på denne [Python tutorial](https://www.w3schools.com/python/)

!!! note "Læringsmål"

    **Viden**

    Den studerende har viden om og forståelse for:
    - Grundlæggende programmeringsprincipper

    **Færdigheder**

    Den studerende kan supportere løsning af sikkerhedsarbejde ved at:
    - Anvende primitive og abstrakte datatyper

    **Kompetencer**

    Den studerende kan:
    - Læse andres scripts samt gennemskue og ændre i dem

## Opgave - Python recap | Del 1

!!! note "Opgave beskrivelse"
    
    Del 1:

    1. Start med denne lille Python [quiz](https://www.w3schools.com/python/python_quiz.asp)
    1. Læs om hvad [Python](https://www.python.org/doc/essays/blurb/) er og kig på sammenligning med andre [sprog](https://www.python.org/doc/essays/comparisons/).
    1. Lav et fælles gitlab repo til det i laver i denne øvelse, klon det til jeres kali linux vm's.
    1. Analyser sammen simple_calculator.py.
    1. For hver linje i programmet noterer i hvad den enkelte linje gør. I må bruge alle hjælpemidler til at analysere programmet, husk at der er links herunder. Husk også at køre programmet så i dels ved at i kan afvikle python programmer, dels ved hvordan programmets funktionalitet er og at der ikke er fejl i programmet...
    1. Læg mærke til datatyper, kontrol strukturer, variabler, funktioner, indentering osv.
    1. Det er vigtigt at i snakker med hinanden og bruger hinandens erfaring med programmering, i en god dialog vil i også få snakket om forskellene på de forskellige sprog i kender.
    1. På klassen laver vi code review ud fra jeres analayse, formålet er at alle har forstået koden og hvordan Python fungerer.

Python er et scripting language, hvilket vil sige at det ikke er lavet til at man skal kunne håndtere allokering at plads i ram osv. Det er meget frit.
I modsetning til andre sprog som C# er python ikke compiled, og programmet går filen igennem linje for linje. Der er derfor at i kode eksemplet under står funktionerne først så programmet senere kan bruge dem, da de skal læses ind i ram først. Et compiled programmerings sprog bliver lavet til maskin kode, som som resultat køre markant hurtigere end python. Python er heller ikke type stærkt, og har en garbage collector som håntere ram allokering automatisk.

Jeg har ikke lavet en gitlab, men har bare lavet en code-block her som jeg har kommenteret på.

```python
# Funktion til at lægge tal sammen
def add(num1, num2):
    return num1 + num2

# Funktion til at trække fra
def sub(num1, num2):
    return num1 - num2

# Funktion til at dividere
def div(num1, num2):
    return num1 / num2

# Funktion til at gange tal sammen
def mult(num1, num2):
    return num1 * num2

# Simpelt print til terminal
print('\nWelcome to the simple calculator (write q to quit)')

# Definer "result" og "cjosen_operation" 
result = 0.0 # Float
chosen_operation = '' # String

# Start et kontinuerligt while loop.
while True:
    # Få bruger input for det første nummer. "number1" er en string
    print('enter the first number')
    number1 = input('> ')
    if number1 == 'q':
        print('goodbye...')
        break
    # Få bruger input for det andet nummer. "number2" er en string
    print('enter the second number')
    number2 = input('> ')
    if number2 == 'q':
        print('goodbye...')
        break
    # Få bruger input for den operation der skal laves "operation" er en string
    print('would like to: 1. add 2. subtract 3. divide or 4. multiply the numbers?')
    operation = input('> ')
    if operation == 'q':
        print('goodbye...')
        break

    # Hvis "q" bliver brugt lukker programmet igen.

    # Lav try except. Programmet prøver at gøre noget som måske ikke vil virke. Dette er en god måde at fejle hurtigt.
    try:
        # Prøv at lave "number1" og "number2" til floats (komma tal)
        number1 = float(number1)
        number2 = float(number2)

        # Prøv at lave "operation" til en int
        operation = int(operation)

        # Hvis "operation" er 1 så lægger programmet tallende sammen.
        if operation == 1:
            result = add(number1, number2)
            chosen_operation = ' added with '
        
        # Hvis "operation" er 2 så trækker programmet tallende fra hindanden.
        elif operation == 2:
            result = sub(number1, number2)
            chosen_operation = ' subtracted from '
        
        # Hvis "operation" er 3 så dividere programmet tallende med hindanden.
        elif operation == 3:
            result = div(number1, number2)
            chosen_operation = ' divided with '
        
        # Hvis "operation" er 4 så ganger programmet tallende med hindanden.
        elif operation == 4:
            result = mult(number1, number2)
            chosen_operation = ' multiplied with '

        # Print nummer + operation + nummer og resultatet. (2.0 added with 2.0 = 4.0)
        print(str(number1) + chosen_operation + str(number2) + ' = ' + str(result))
        print('restarting....')

    # Denne køre hvis "numer1", "number2" og/eller "operation" er andet end tal.
    except ValueError:
        print('only numbers and "q" is accepted as input, please try again')

    # Denne sørger for at man ikke kan dividere med nul.
    except ZeroDivisionError:
        print('cannot divide by zero, please try again')
```

## Opgave - Python recap | Del 2

!!! note "Opgave beskrivelse"
    
    Nu er det jeres tur til at programmere :-)

    1. Omskriv så meget af programmet som muligt så det har så få gentagelser som muligt, altså abstraher så meget som muligt til funktioner.
    1. Udvid lommeregner programmet så det kan logge input, resultater og fejl til en .log fil.
    1. Brug [logging modulet](https://realpython.com/python-logging/) i Python.
    1. Omskriv programmet så regne funktionerne er i en klasse for sig selv og logging funktionalitet er i en anden klasse. Funktionaliteten skal være den samme som i punkt 5+6.
    1. Lav en python fil der importerer og bruger jeres klasser så programmet afvikles som det oprindelige program.
