![obraz](https://github.com/user-attachments/assets/4f3edf66-756a-4844-a3fe-99c39f4d43dd)

[BioComp](https://dsl.biokomputery.pl/) to propozycja języka domenowo-specyficznego (DSL) do edukacji i wdrażania biocomputingu obejmuje elementy języka opisu eksperymentów, symulacji, designu i utrzymania systemów biokomputerowych. 


### Składnia

Główne składniki BioDSL obejmują:

1. **Definicje Molekularne**
2. **Tworzenie Biologicznych Układów Logicznych**
3. **Symulacje Eksperymentów**
4. **Drukowanie i Inżynieria BioSystemów**
5. **Monitorowanie i Utrzymanie Systemów**


### Zaleznosci

BioComp zostal zaimplementowany jako Kod Pythona z klasami i logiką do tworzenia instancji i ich przetwarzania.
Pliki YAML zawieraja parametry dla tych instancji.
Skrypt `biocomp.py` analizuje plik YAML, tworzy niezbędne obiekty i uruchamia symulację w oparciu o parametry zawarte w pliku YAML.


1. **`pyparsing`**: Biblioteka do parsowania, potrzebna do przetwarzania DSL.
2. **`matplotlib`**: Biblioteka do tworzenia wizualizacji, użyta do generowania wykresów wyników symulacji.
3. **`numpy`**: Biblioteka do operacji na tablicach wielowymiarowych, używana do generowania danych do symulacji.
4. **`graphviz`**: The addition of the `graphviz` module is necessary for graph visualization.


### Instalacja

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


This setup parses the YAML file, creates the necessary objects, and runs the simulation based on the parameters provided in the YAML file.


## Samples

These examples include various configurations of molecules, logic gates, and simulation conditions.
Assuming you have implemented `AND`, `OR`, and `NOT` gate logic in your actual `LogicGate` class, these should yield appropriate outputs based on the conditions set in each YAML file.
Examples can handle various gate types (`AND`, `OR`, `NOT`). 
If not, you'll need to add the logic for these gate types in your `LogicGate` class implementation.

To test your script with these examples, save each YAML configuration as separate files 


### BioCompSystem1

![bio_system_graph.png](1%2Fbio_system_graph.png)

```css
digraph {
	Input1Prot [label="Input1Prot (Protein)"]
	Input2Prot [label="Input2Prot (Protein)"]
	OutputProt [label="OutputProt (Protein)"]
	"AND Gate"
	Input1Prot -> "AND Gate"
	Input2Prot -> "AND Gate"
	"AND Gate" -> OutputProt
}
```

```bash
python biocomp.py 1/biocomp.yaml
```

![1](1/sim.png)

```
Running simulation for BioCompSystem1
Conditions: {'time': 100, 'temperature': 37}
Expected Outputs: ['Protein OutputProt']
```


### BioCompSystem2
![bio_system_graph.png](2/bio_system_graph.png)

```css
digraph {
	Input1Prot [label="Input1Prot (Protein)"]
	Input2Prot [label="Input2Prot (Protein)"]
	OutputProt [label="OutputProt (Protein)"]
	"OR Gate"
	Input1Prot -> "OR Gate"
	Input2Prot -> "OR Gate"
	"OR Gate" -> OutputProt
}
```

```bash
python biocomp.py 2/biocomp.yaml
```

```yaml
Running simulation for BioCompSystem2
Conditions: {'time': 150, 'temperature': 25}
Expected Outputs: ['Protein OutputProt']
```
![sym](2/sim.png)


### BioCompSystem3
![bio_system_graph.png](3/bio_system_graph.png)


```css
digraph {
	Input1Prot [label="Input1Prot (Protein)"]
	Input2Prot [label="Input2Prot (Protein)"]
	Input3Prot [label="Input3Prot (Protein)"]
	OutputProt1 [label="OutputProt1 (Protein)"]
	OutputProt2 [label="OutputProt2 (Protein)"]
	"AND Gate"
	Input1Prot -> "AND Gate"
	Input2Prot -> "AND Gate"
	"AND Gate" -> OutputProt1
	"OR Gate"
	OutputProt1 -> "OR Gate"
	Input3Prot -> "OR Gate"
	"OR Gate" -> OutputProt2
}
```

```sh
python biocomp.py 3/biocomp.yaml
```

```yaml
Running simulation for BioCompSystem3
Conditions: {'time': 200, 'temperature': 30}
Expected Outputs: ['Protein OutputProt1', 'Protein OutputProt2']
```
![3](3/sim.png)


### BioCompSystem4
![bio_system_graph.png](4/bio_system_graph.png)

```css
digraph {
	Input1Prot [label="Input1Prot (Protein)"]
	OutputProt [label="OutputProt (Protein)"]
	"NOT Gate"
	Input1Prot -> "NOT Gate"
	"NOT Gate" -> OutputProt
}
```

```sh
python biocomp.py 4/biocomp.yaml
```

```yaml
Running simulation for BioCompSystem4
Conditions: {'time': 120, 'temperature': 37}
Expected Outputs: ['Protein OutputProt']
```
![4](4/sim.png)




## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=biokomputer/dsl&type=Date)](https://star-history.com/#biokomputer/dsl&Date)


## [Contributions](http://contribution.softreck.dev)

[CONTRIBUTION](CONTRIBUTION.md) are always welcome:
+ did you found an [Issue or Mistake](https://github.com/biokomputer/dsl/issues/new)?
+ do you want to [improve](https://github.com/biokomputer/dsl/edit/main/README.md) the article?
+ are you interested do join another [git projects](https://github.com/biokomputer/)?
+ have something to contribute or discuss? [Open a pull request](https://github.com/biokomputer/dsl/pulls) or [create an issue](https://github.com/biokomputer/dsl/issues).



## Autor

![obraz](https://github.com/tom-sapletta-com/rynek-pracy-2030-eu/assets/5669657/24abdad9-5aff-4834-95a0-d7215cc6e0bc)

## Tom Sapletta

Na co dzień DevOps, ewangelista hipermodularyzacji, ostatnio entuzjasta biocomputing.
Łączy doświadczenie w programowaniu i research-u poprzez wdrażanie nowatorskich rozwiązań. 
Szerokie spektrum zainteresowań, umiejętności analityczne i doświadczenie w branży owocują eksperymentalnymi projektami opensource.

+ [Tom Sapletta, Linkedin](https://www.linkedin.com/in/tom-sapletta-com)
+ [Tom Sapletta, Github](https://github.com/tom-sapletta-com)


---



<script type="module">    
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  //import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.8.0/dist/mermaid.min.js';
  mermaid.initialize({
    startOnReady:true,
    theme: 'forest',
    flowchart:{
            useMaxWidth:false,
            htmlLabels:true
        }
  });
  mermaid.init(undefined, '.language-mermaid');
</script>

