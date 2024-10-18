# biograph.py

`biograph.py` is a Python script that parses a YAML file containing information about a biological system, runs a simulation, and visualizes the biological system using the Graphviz library.

## Classes

### Molecule

Represents a molecule in the biological system.

#### Attributes
- `type` (str): The type of the molecule.
- `name` (str): The name of the molecule.

#### Methods
- `__init__(self, type, name)`: Initializes a new Molecule object.
- `__repr__(self)`: Returns a string representation of the Molecule object.

### LogicGate

Represents a logic gate in the biological system.

#### Attributes
- `gate_type` (str): The type of the logic gate (e.g., 'NOT', 'AND', 'OR').
- `input1` (Molecule): The first input molecule of the logic gate.
- `input2` (Molecule, optional): The second input molecule of the logic gate.
- `output` (Molecule): The output molecule of the logic gate.

#### Methods
- `__init__(self, gate_type, input1, output, input2=None)`: Initializes a new LogicGate object.
- `__repr__(self)`: Returns a string representation of the LogicGate object.

### BiologicalSystem

Represents a biological system containing molecules and logic gates.

#### Attributes
- `name` (str): The name of the biological system.
- `logic_gates` (list of LogicGate): A list of logic gates in the biological system.
- `molecules` (list of Molecule): A list of molecules in the biological system.

#### Methods
- `__init__(self, name, logic_gates, molecules)`: Initializes a new BiologicalSystem object.
- `__repr__(self)`: Returns a string representation of the BiologicalSystem object.

### Simulation

Represents a simulation of a biological system.

#### Attributes
- `system` (BiologicalSystem): The biological system being simulated.
- `conditions` (dict): A dictionary of simulation conditions.
- `outputs` (dict): A dictionary of expected simulation outputs.

#### Methods
- `__init__(self, system, conditions, outputs)`: Initializes a new Simulation object.
- `run(self)`: Runs the simulation and prints the simulation conditions and expected outputs.

## Functions

### visualize_biological_system(bio_system)

Visualizes the biological system using the Graphviz library.

#### Arguments
- `bio_system` (BiologicalSystem): The biological system to be visualized.

### main(yaml_file)

Parses a YAML file containing information about a biological system, runs a simulation, and visualizes the biological system.

#### Arguments
- `yaml_file` (str): The path to the YAML file containing information about the biological system.

## Usage

To use the `biograph.py` script, provide a YAML file as a command-line argument:

```
python biograph.py biosystem/1/biocomp.yaml
```

The YAML file should contain the following structure:

```yaml
molecules:
  - type: ...
    name: ...
  - ...

logic_gates:
  - gate_type: ...
    input1: ...
    input2: ... (optional)
    output: ...
  - ...

biological_system:
  name: ...

simulation:
  conditions:
    ...
  outputs:
    ...
```

The script will parse the YAML file, create the biological system, run a simulation, and visualize the biological system using Graphviz. The visualization will be saved as a PNG file named `bio_system_graph.png` and automatically opened for viewing.
