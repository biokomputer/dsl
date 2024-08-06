
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



#### Uruchomienie kodu Python

Po zainstalowaniu wszystkich potrzebnych bibliotek, możesz uruchomić swój kod Python zawierający parser DSL oraz symulację i wizualizację.
v1
```bash
python biodsl.py sym1.biocomp
```
v2
```bash
python biocomp.py sym1.biocomp
```
v3
```bash
python b2.py sym2.biocomp
```
```sql
molecule DNA(name="Plasmid123", sequence="ATGCGTACG...")
molecule Protein(name="GFP", expression="Plasmid123", structure="AlphaHelix")

logic_gate AND(
    input1=Protein(name="Input1Prot"),
    input2=Protein(name="Input2Prot"),
    output=Protein(name="OutputProt")
)

biological_system BioCompSystem1 {
    logic_gates = [AND]
    molecules = [Protein(name="Input1Prot"), Protein(name="Input2Prot"), Protein(name="OutputProt")]
}

simulation BioCompSim1 {
    system = BioCompSystem1
    conditions {
        time = 100  # in minutes
        temperature = 37  # in Celsius
    }
    outputs = ["Protein OutputProt"]
}
```


## FAQ

How to deactivate a Virtual Environment?

```bash
deactivate
``` 






### Plik DSL [sym1.biocomp](sym1.biocomp)

Język DSL opisany w twoim pytaniu najbardziej przypomina **JSON** oraz elementy języków takich jak **YAML** czy **TOML**, jednak zawiera specjalne konstrukcje strukturalne, które upodabniają go także do opisu konfiguracji lub nawet do niektórych specyficznych formatu w języku **Python**.

Dla podkreślenia składni w Markdown, można skorzystać z fragmentów typu JSON lub Python, aby uzyskać odpowiednie podświetlenie składni.

Używając składni SQL jako najbardziej zbliżonej, aby w pewnym stopniu oddać strukturę twojego DSL:


```sql
molecule DNA(name="Plasmid123", sequence="ATGCGTACG...")
molecule Protein(name="GFP", expression="Plasmid123", structure="AlphaHelix")

logic_gate AND(
    input1=Protein(name="Input1Prot"),
    input2=Protein(name="Input2Prot"),
    output=Protein(name="OutputProt")
)

biological_system BioCompSystem1 {
    logic_gates = [AND]
    molecules = [Protein(name="Input1Prot"), Protein(name="Input2Prot"), Protein(name="OutputProt")]
}

simulation BioCompSim1 {
    system = BioCompSystem1
    conditions {
        time = 100  # in minutes
        temperature = 37  # in Celsius
    }
    outputs = ["Protein OutputProt"]
}
```

### format JSON

```json
{
  "molecule": {
    "DNA": {
      "name": "Plasmid123",
      "sequence": "ATGCGTACG..."
    },
    "Protein": {
      "name": "GFP",
      "expression": "Plasmid123",
      "structure": "AlphaHelix"
    }
  },
  "logic_gate": {
    "AND": {
      "input1": "Protein(name=\"Input1Prot\")",
      "input2": "Protein(name=\"Input2Prot\")",
      "output": "Protein(name=\"OutputProt\")"
    }
  },
  "biological_system": {
    "BioCompSystem1": {
      "logic_gates": ["AND"],
      "molecules": ["Protein(name=\"Input1Prot\")", "Protein(name=\"Input2Prot\")", "Protein(name=\"OutputProt\")"]
    }
  },
  "simulation": {
    "BioCompSim1": {
      "system": "BioCompSystem1",
      "conditions": {
        "time": 100,
        "temperature": 37
      },
      "outputs": ["Protein OutputProt"]
    }
  }
}
```

### Edytory i Typy Plików

Visual Studio Code jest wyjątkowo elastycznym edytorem, który obsługuje wiele języków i typów plików. Można użyć wtyczki do podświetlania składni specyficznych dla JSON, YAML lub nawet własnych DSL.

Zaproponowany typ pliku dla DSL to `.biocomp`.

### Konfiguracja podświetlania składni w VSCode

Aby skonfigurować podświetlanie składni dla niestandardowych plików w VSCode, można użyć wtyczki takie jak "Language Support for JSON" lub "YAML". Możliwe jest także tworzenie własnych rozszerzeń, które definiują skrypt podświetlania składni.

#### Przykład konfiguracji w VSCode

1. **Rozszerzenie json**:
   Zainstaluj rozszerzenie `vscode-json` lub `vscode-yaml`.
   
2. **Plik ustawień**:
    Przejdź do ustawień użytkownika (klawisz skrótu `Ctrl+,`) i dodaj:

    ```json
    "files.associations": {
        "*.biocomp": "json"  // lub "yaml"
    }
    ```

3. **Dostosowanie**:
   Możesz również dostosować podświetlanie składni używając bardziej zaawansowanych wtyczek, takich jak TextMate, które pozwalają na definiowanie wzorców regularnych dla podświetlania specyficznej składni.

### Podsumowanie

Twój custom DSL przypomina JSON, YAML, a także pewne specyficzne formy zapisu struktur w Pythonie. Aby korzystać z podświetlania składni w edytorze, takim jak Visual Studio Code, można skonfigurować pliki `.biocomp` do używania reguł podświetlania składni JSON lub YAML. Poniższy kod jest przykładem konfiguracji do osiągnięcia takiego rezultatu.




Aby pobrać zawartość DSL z pliku, skorzystamy z funkcji Python do obsługi plików. Poniżej znajdziesz kompletny kod, który zawiera kroki: wczytania DSL z pliku, parsowania tego DSL, przetworzenia wyników parsowania na odpowiednie struktury danych oraz uruchomienia symulacji i wyświetlenia wyników.

### Krok 1: Definiowanie Struktur DSL w Pythonie

Skorzystamy z wcześniej zdefiniowanych struktur danych:

```


----