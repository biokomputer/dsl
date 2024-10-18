

### Funkcje Uaktualnione do Obsługi YAML i Generowania Danych

Wszystkie zaktualizowane funkcje do generowania wykresów, tekstów oraz obrazów zostały zmodyfikowane w powyższym skrypcie.

Powyższa struktura pozwala na bardziej zaawansowane modelowanie reakcji dyfuzji w prostym modelu dla Physarum polycephalum, tworzenie wizualizacji oraz grafów hierarchicznych na podstawie prostego pliku YAML zarządzającego parametrami symulacji.


### Zaktualizowany Skrypt Python

Aby zapewnić, że można pobierać wiele plików YAML oraz opcjonalnie przetwarzać wszystkie pliki YAML w podanym folderze, a także generować wykresy, tekstowe definicje grafów i ich graficzne reprezentacje, skrypt Python został zaktualizowany w poniższy sposób:

#### Instalacja Wymaganych Bibliotek
Najpierw należy zainstalować wymagane biblioteki:
```bash
pip install numpy matplotlib graphviz pyyaml
```

### Główna Część Skryptu

Skrypt Obsługuje hierarchiczną strukturę komórkową Physarum oraz model reakcyjno-dyfuzyjny. Będziemy generować wykresy wzrostu biomasy oraz strukturę hierarchiczną za pomocą Graphviz.


#### Przetwarzanie Pojedynczych Plików

Aby uruchomić skrypt dla pojedynczych plików YAML:
```bash
python physarum.py --files 21/physarum.yaml
```
```bash
python physarum.py --files 21/physarum.yaml 22/physarum.yaml
```

#### Przetwarzanie Folderu

Aby uruchomić skrypt dla wszystkich plików w folderze:
```bash
python physarum.py --folder ./21
```

Dodanie klasy `Simulation` oraz funkcji `generate_graphviz_text` do skryptu Pythona pozwoli na lepszą organizację kodu i łatwiejsze zarządzanie symulacjami. Oto zaktualizowany skrypt, który zawiera te elementy:

### Skrypt `biocomp_sim.py`

#### Instalacja Wymaganych Bibliotek
Najpierw upewnij się, że masz zainstalowane wymagane biblioteki:
```bash
pip install numpy matplotlib graphviz pyyaml
```


### Używanie Skryptu


#### Przetwarzanie Folderu
Aby uruchomić skrypt dla wszystkich plików w folderze:
```bash
python biocomp_sim.py --folder ./your_folder
```




Aby upewnić się, że przy zmianie wartości w sekcji `conditions` w pliku YAML te warunki wpłyną na symulację, trzeba je uwzględnić w modelu symulacji. W skrypcie, parametry takie jak `temperature` i `humidity` powinny wpływać na współczynniki modelu, takie jak wskaźniki reakcji i dyfuzji.

Przykład:
- **Czas symulacji (`time`)** definiuje, jak długo trwać będzie symulacja.
- **Temperatura (`temperature`) i wilgotność (`humidity`) mogą wpływać na wskaźniki reakcji chemicznych i dyfuzji.







### Zaktualizowanie Skryptu Python

#### Dodanie Wpływu Warunków na Model
Skrypty należy zaktualizować, aby zapewnić, że zmienne warunki wpływają na symulację.

```python
```

### Aktualizacje wewnątrz kodu

1. **Wyważenie wartości warunków symulacyjnych**:
    - Wartości `steps` w symulacji są teraz wynikową całością dni przeliczoną na jednostki czasowe symulacji.
    - Współczynnik dyfuzji `D` oraz wskaźnik reakcji `f` są teraz skalowane przez wartości `temperature` i `humidity`.

### Wartości w YAML

Przykład YAML teraz uwzględnia bardziej realistyczne zmiany warunków:

#### Plik 1: `physarum_simulation_1.yaml`
```yaml
type: physarum
name: "PhysarumSimulation1"
grid_size: 101
steps: 10000
diffusion_coefficient: 0.1
reaction_rate: 0.04
k: 0.06
initial_u_value: 0.50
initial_v_value: 0.25
initial_radius: 20
conditions:
  time: 3    # days
  temperature: 1   # Celsius
  humidity: 70     # Percentage
outputs:
  - "u"
  - "v"
```

Teraz, jeśli uruchomisz:

```bash
python physarum.py --files physarum_simulation_1.yaml
```

Zmiany w sekcji `conditions` faktycznie wpływają na symulację. Dostosowanie współczynników dyfuzji i reakcji zwiększa realizm symulacji w zależności od danych warunków środowiskowych.
