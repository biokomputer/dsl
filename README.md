# biocomp - python based DSL for biocomputing

Propozycja języka domenowo-specyficznego (DSL) do edukacji i wdrażania biocomputingu mogłaby obejmować elementy języka opisu eksperymentów, symulacji, designu i utrzymania systemów biokomputerowych. 
BioDSL posiada jasną i intuicyjną składnię, umożliwiającą tworzenie i uruchamianie eksperymentów oraz analizę wyników.


### Składnia

Główne składniki BioDSL obejmują:
1. **Definicje Molekularne**
2. **Tworzenie Biologicznych Układów Logicznych**
3. **Symulacje Eksperymentów**
4. **Drukowanie i Inżynieria BioSystemów**
5. **Monitorowanie i Utrzymanie Systemów**


Python code with respective classes and logic for creating instances and processing them. Then, we'll create a YAML file containing the parameters for those instances. Finally, we'll write the Python script to parse the YAML file and execute the corresponding functions.


## START

### Zaleznosci

1. **`pyparsing`**: Biblioteka do parsowania, potrzebna do przetwarzania DSL.
2. **`matplotlib`**: Biblioteka do tworzenia wizualizacji, użyta do generowania wykresów wyników symulacji.
3. **`numpy`**: Biblioteka do operacji na tablicach wielowymiarowych, używana do generowania danych do symulacji.

Aby zainstalować te wymagania w swoim środowisku Python, wykonaj następujące kroki:

#### Stwórz i aktywuj wirtualne środowisko:
```bash
python -m venv env
source env/bin/activate  # Na Windows użyj: env\Scripts\activate
```
 
####  Zainstaluj zależności z pliku `requirements.txt`:
```bash
pip install -r requirements.txt
pip install --upgrade pip
```

### Execution Script

To run this setup, follow these steps:

1. Save the Python code in a file named `biocomp.py`.
2. Save the YAML content in a file named `biocomp.yaml`.
3. Execute the Python script from the command line, providing the YAML file as an argument:

```sh
python biocomp.py biocomp.yaml
```

The output should be something like:

```
Running simulation for BioCompSystem1
Conditions: {'time': 100, 'temperature': 37}
Expected Outputs: ['Protein OutputProt']
```

This setup parses the YAML file, creates the necessary objects, and runs the simulation based on the parameters provided in the YAML file.