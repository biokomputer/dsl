

### Przykłady

+ `fungi_simulation_1.yaml`
+ `fungi_simulation_2.yaml`

### Jak Uruchomić:

1. **Stworzenie Plików YAML**: Utwórz pliki YAML (`fungi_simulation_1.yaml` i `fungi_simulation_2.yaml`) z powyższą zawartością.

2. **Uruchomienie Skryptu**:
   ```bash
   python fungi.py 11/fungi.yaml
   ```
   
   lub
    
   ```bash
   python fungi.py 12/fungi.yaml
   ```


#### Przetwarzanie Pojedynczych Plików

Aby uruchomić skrypt dla pojedynczych plików YAML:
```bash
python fungi.py --files  11/fungi.yaml  12/fungi.yaml
```

#### Przetwarzanie Folderu

Aby uruchomić skrypt dla wszystkich plików w folderze:
```bash
python fungi.py --folder ./11
```

