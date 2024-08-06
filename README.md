# BioDSL
python based DSL for biocomputing

Propozycja języka domenowo-specyficznego (DSL) do edukacji i wdrażania biocomputingu mogłaby obejmować elementy języka opisu eksperymentów, symulacji, designu i utrzymania systemów biokomputerowych. 
BioDSL posiada jasną i intuicyjną składnię, umożliwiającą tworzenie i uruchamianie eksperymentów oraz analizę wyników.


### Składnia BioDSL

Główne składniki BioDSL obejmują:
1. **Definicje Molekularne**
2. **Tworzenie Biologicznych Układów Logicznych**
3. **Symulacje Eksperymentów**
4. **Drukowanie i Inżynieria BioSystemów**
5. **Monitorowanie i Utrzymanie Systemów**

### Przykładowe Definicje i Kody BioDSL

#### 1. Definicje Molekularne

```plaintext
molecule DNA(name="Plasmid123", sequence="ATGCGTACG...")
molecule Protein(name="GFP", expression="Plasmid123", structure="AlphaHelix")
```

#### 2. Tworzenie Biologicznych Układów Logicznych

```plaintext
logic_gate AND(
    input1=Protein(name="Input1Prot"),
    input2=Protein(name="Input2Prot"),
    output=Protein(name="OutputProt")
)

biological_system BioCompSystem1 {
    logic_gates = [AND]
    molecules = [Protein(name="Input1Prot"), Protein(name="Input2Prot"), Protein(name="OutputProt")]
}
```

#### 3. Symulacje Eksperymentów

```plaintext
simulation BioCompSim1 {
    system = BioCompSystem1
    conditions {
        time = 100  # in minutes
        temperature = 37  # in Celsius
    }
    outputs = ["Protein OutputProt"]
}
```

#### 4. Drukowanie i Inżynieria BioSystemów

```plaintext
printable BioSystemPrintDesign1 {
    system = BioCompSystem1
    fabrication_methods = ["CRISPR", "PCR"]
}

print BioSystemPrintDesign1 {
    device = "BioPrinter3000"
    material = "Plasmid"
}
```

#### 5. Monitorowanie i Utrzymanie Systemów

```plaintext
monitor BioCompSystem1 {
    parameters = ["Protein OutputProt"]
    interval = 10  # in minutes
}

maintenance_plan BioCompMaintenance1 {
    system = BioCompSystem1
    tasks = [
        {description="Check protein levels", frequency="daily"},
        {description="Clean bioreactor", frequency="weekly"}
    ]
}
```

### Przykładowy Workflow z BioDSL

#### Kod definicji i symulacji

```plaintext
# Definiowanie molekuł
molecule DNA(name="Plasmid123", sequence="ATGCGTACG...")
molecule Protein(name="GFP", expression="Plasmid123", structure="AlphaHelix")

# Tworzenie układu logicznego
logic_gate AND(
    input1=Protein(name="Input1Prot"),
    input2=Protein(name="Input2Prot"),
    output=Protein(name="OutputProt")
)

# Definiowanie systemu biologicznego
biological_system BioCompSystem1 {
    logic_gates = [AND]
    molecules = [Protein(name="Input1Prot"), Protein(name="Input2Prot"), Protein(name="OutputProt")]
}

# Symulacja eksperymentu
simulation BioCompSim1 {
    system = BioCompSystem1
    conditions {
        time = 100  # in minutes
        temperature = 37  # in Celsius
    }
    outputs = ["Protein OutputProt"]
}
```

#### Kod drukowania i inżynierii

```plaintext
# Design do druku bioinżynieryjnego
printable BioSystemPrintDesign1 {
    system = BioCompSystem1
    fabrication_methods = ["CRISPR", "PCR"]
}

# Drukowanie systemu
print BioSystemPrintDesign1 {
    device = "BioPrinter3000"
    material = "Plasmid"
}
```

#### Kod monitoringu i utrzymania

```plaintext
# Monitorowanie systemu
monitor BioCompSystem1 {
    parameters = ["Protein OutputProt"]
    interval = 10  # in minutes
}

# Plan utrzymania systemu
maintenance_plan BioCompMaintenance1 {
    system = BioCompSystem1
    tasks = [
        {description="Check protein levels", frequency="daily"},
        {description="Clean bioreactor", frequency="weekly"}
    ]
}
```

### Podsumowanie

BioDSL jest zaprojektowany, aby uprościć edukację i wdrażanie biocomputingu, poprzez intuicyjną składnię i jasne reprezentacje kroków od definicji molekularnych, przez symulacje i drukowanie, aż po monitorowanie i utrzymanie systemów.

Umożliwia łatwiejsze zrozumienie i wdrożenie zarówno dla początkujących, jak i dla bardziej zaawansowanych uczniów oraz badaczy.

