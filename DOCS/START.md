Aby stworzyć skrypt, który będzie wczytywał plik DSL z linii poleceń, zaczniemy od prostego skryptu Python, który przetworzy dane z pliku i uruchomi symulację. Następnie dodamy `setup.py`, aby umożliwić łatwą instalację, i `Makefile`, aby uprościć proces uruchamiania i instalacji.

### Skrypt Python - `biocomp.py`

Najpierw stwórz skrypt Python, który będzie przetwarzał plik DSL podany jako argument:

```python
```

### Plik `setup.py`

Plik `setup.py` umożliwi instalację skryptu jako pakietu Python:


### Plik `Makefile`

proces budowania, instalacji i uruchamiania skryptu:


### Instrukcje Użytkowania

1. **Instalacja środowiska wirtualnego (opcjonalnie)**:
   ```bash
   python -m venv env
   source env/bin/activate  # Na Windows: .\env\Scripts\activate
   ```

2. **Stworzenie pliku DSL**:
   Upewnij się, że masz plik DSL o nazwie `bio_comp.dsl` z odpowiednią zawartością.

3. **Instalacja pakietu**:
   ```bash
   make install
   ```

4. **Uruchomienie symulacji**:
   ```bash
   make run file=bio_comp.dsl
   ```

5. **Czyszczenie środowiska** (opcjonalne):
   ```bash
   make clean
   ```

### Podsumowanie

Powyższe kroki pomogą w utworzeniu skryptu, który wczytuje plik DSL, parsuje jego zawartość, przetwarza dane, przeprowadza symulację i wyświetla wyniki graficzne. Pliki `setup.py` i `Makefile` ułatwią instalację i zarządzanie projektem.