# Eksamen

## Prøveform
Prøven er en individuel, mundtlig prøve med udgangspunkt i et spørgsmål, som den stude-
rende trækker til eksamen. Alle spørgsmål, der kan trækkes til eksamen, er udleveret til de studerende senest 14
dage før eksamen, så de studerende har mulighed for at forberede sig. Hvad angår
spørgsmålene, vil der blive lagt vægt på, at den studerende kan inddrage `eksempler` fra
projektarbejdet og `praktiske øvelser` fra det forgangne semester. Der er ingen forberedelse
på selve dagen. Den individuelle, mundtlige eksamen varer 25 minutter inkl. votering.

Opdelingen vil blive således:

- 10 minutters præsentation
- 10 minutters samtale/diskussion
- 5 minutters votering

## Eksamen spørgsmål/emner

Jeg brainstormer med hvad jeg kunne snakke om, i forhold til hvert spørgsmål.

- [ ] **Netværk med fokus på OSI, TCP/IP modeller og netværksprotokoller samt (u)sikkerhed i disse.**
    - Forklare om OSI og TCP/IP modellerne.
    - Forklare om HTTP vs. HTTPS.
        - Måske forklare TLS
        - Vis et eksempel med wireshark, før og efter kryptering

- [ ] **Netværk med fokus på trafikmonitorering og skanning samt hvordan dette kan anvendes i arbejdet med sikkerhed.**
    - Forklar trafikmonitorering og skanning.
        - Wireshark
        - Nmap
    - Lav et lille netværk med diagram til.
        - 1x attack machine
        - 1x router opnsense
        - 1x victim machine
    - Demonstrær nmap scanning, og så wireshark samme scanning.

- [ ] **Programmering med database og fokus på database (u)sikkerhed.**
    - Forklar om databaser og database typer, SQL og noSQL
        - Hvad databaserne er gode til. (Fordele og ulemper) 
    - Vis hvordan en database kan bruges med programering.
    - Keylogger programmet kan måske kobles på her.

- [ ] **Programmering med netværk og fokus på sikkerhed i protokoller.**
    - Demonstrær keylogger programet, som bruger socket biblioteket.

- [ ] **Scripting i bash og powershell med fokus på hvordan det kan anvendes i arbejdet med sikkerhed.**
    - Forklar vad bash og powershell bruges til (Automation)
        - Man kan bruge det til både red og blue team.
    - Måske forklar syntax
    - Lav et script i både bash og powershell, som gør det samme, skal være noget med sikkerhed. 
        - password checker.