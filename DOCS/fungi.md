# fungi.py

`fungi.py` is a Python script for running fungal growth simulations based on YAML configuration files. It uses the logistic growth equation to model the growth of fungal biomass over time.

## Data Structures

### Simulation

Represents a simulation of fungal growth.

#### Attributes
- `name` (str): The name of the simulation.
- `initial_population` (float): The initial population size of the fungus.
- `growth_rate` (float): The growth rate of the fungus.
- `carrying_capacity` (float): The carrying capacity of the environment.
- `conditions` (dict): A dictionary of simulation conditions (e.g., time, temperature, humidity).
- `outputs` (list of str): A list of desired output variables.

## Functions

### load_yaml_from_file(file_path: str) -> dict

Loads a YAML file and returns its contents as a dictionary.

#### Arguments
- `file_path` (str): The path to the YAML file.

### run_simulation(simulation: Simulation)

Runs a simulation of fungal growth using the logistic growth equation.

#### Arguments
- `simulation` (Simulation): The simulation object containing the necessary parameters.

### generate_plot(time, biomass_levels, output_file)

Generates a plot of the biomass growth over time and saves it as a PNG file.

#### Arguments
- `time` (array-like): The time points of the simulation.
- `biomass_levels` (array-like): The biomass levels at each time point.
- `output_file` (str): The base name of the output file (without extension).

### generate_graphviz_text(simulation: Simulation, output_file)

Generates a Graphviz DOT file representing the simulation as a graph.

#### Arguments
- `simulation` (Simulation): The simulation object.
- `output_file` (str): The base name of the output file (without extension).

### generate_graphviz_image(output_file)

Generates a PNG image from a Graphviz DOT file.

#### Arguments
- `output_file` (str): The base name of the output file (without extension).

### parse_yaml_to_simulation(yaml_data: dict) -> Simulation

Creates a Simulation object from a dictionary loaded from a YAML file.

#### Arguments
- `yaml_data` (dict): The dictionary containing the simulation parameters.

### main()

The main function of the script. It parses command-line arguments, processes YAML files, runs simulations, and generates plots and graph representations.

## Usage

To use the `fungi.py` script, provide one or more YAML files as command-line arguments:

```
python fungi.py --files fungi/11/fungi.yaml fungi/12/fungi.yaml
```

Alternatively, you can specify a folder containing YAML files:

```
python fungi.py --folder fungi
```

The script will process each YAML file, run the corresponding simulation, and generate plots and graph representations for each simulation.

The YAML files should have the following structure:

```yaml
name: Simulation Name
initial_population: 10.0
growth_rate: 0.5
carrying_capacity: 1000.0
conditions:
  time: 30
  temperature: 25
  humidity: 0.8
outputs:
  - biomass
```

The script will generate PNG files for the biomass growth plot and the graph representation, as well as a Graphviz DOT file for each simulation.
