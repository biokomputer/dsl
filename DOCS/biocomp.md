# biocomp.py

`biocomp.py` is a Python script that simulates a biological system based on a YAML configuration file. It defines classes for molecules, logic gates, and the biological system itself, and provides functionality to run simulations and visualize the results.

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
- `conditions` (dict): A dictionary containing the simulation conditions.
- `outputs` (list of str): A list of expected output names.

#### Methods
- `__init__(self, system, conditions, outputs)`: Initializes a new Simulation object.
- `run(self)`: Runs the simulation and prints the simulation details.

## Functions

### run_simulation(simulation: Simulation)

Runs a simulation and plots the output levels.

#### Arguments
- `simulation` (Simulation): The simulation to be run.

### main(yaml_file)

Parses a YAML file, creates a biological system, and runs a simulation.

#### Arguments
- `yaml_file` (str): The path to the YAML file containing the biological system data.

## Usage

To use the `biocomp.py` script, provide a YAML file as a command-line argument:

```
python biocomp.py biosystem/1/biocomp.yaml
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
    time: ...
  outputs:
    - ...
```

The script will parse the YAML file, create the biological system, and run a simulation based on the provided configuration. The simulation results will be visualized using a plot of the output levels over time.
