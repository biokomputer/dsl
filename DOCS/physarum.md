# physarum.py

`physarum.py` is a Python script for simulating the growth of Physarum polycephalum, a slime mold, using a reaction-diffusion model. The script reads simulation parameters from YAML files and generates plots and graph representations of the simulation results.

## Data Structures

### Simulation

Represents a simulation of Physarum polycephalum growth.

#### Attributes
- `name` (str): The name of the simulation.
- `grid_size` (int): The size of the grid used for the simulation.
- `steps` (int): The number of simulation steps.
- `diffusion_coefficient` (float): The diffusion coefficient of the chemicals.
- `reaction_rate` (float): The reaction rate of the chemicals.
- `k` (float): The decay rate of the inhibitor chemical.
- `initial_u_value` (float): The initial value of the activator chemical.
- `initial_v_value` (float): The initial value of the inhibitor chemical.
- `initial_radius` (int): The initial radius of the Physarum colony.
- `conditions` (dict): A dictionary of simulation conditions (e.g., time, temperature, humidity).
- `outputs` (list of str): A list of desired output variables.

## Functions

### simulate_reaction_diffusion(sim: Simulation)

Simulates the reaction-diffusion process of Physarum growth using the Gray-Scott model.

#### Arguments
- `sim` (Simulation): The simulation object containing the necessary parameters.

### generate_plot(u, v, output_file)

Generates a plot of the activator chemical concentration and saves it as a PNG file.

#### Arguments
- `u` (numpy array): The activator chemical concentration matrix.
- `v` (numpy array): The inhibitor chemical concentration matrix.
- `output_file` (str): The base name of the output file (without extension).

### generate_graphviz_hierarchy(sim: Simulation, output_file)

Generates a hierarchical graph representation of the Physarum structure using Graphviz.

#### Arguments
- `sim` (Simulation): The simulation object.
- `output_file` (str): The base name of the output file (without extension).

### generate_graphviz_text(sim: Simulation, output_file)

Generates a Graphviz DOT file representing the simulation as a graph.

#### Arguments
- `sim` (Simulation): The simulation object.
- `output_file` (str): The base name of the output file (without extension).

### generate_graphviz_image(output_file)

Generates a PNG image from a Graphviz DOT file.

#### Arguments
- `output_file` (str): The base name of the output file (without extension).

### parse_yaml_to_simulation(yaml_data: dict) -> Simulation

Creates a Simulation object from a dictionary loaded from a YAML file.

#### Arguments
- `yaml_data` (dict): The dictionary containing the simulation parameters.

### load_yaml_from_file(file_path: str) -> dict

Loads a YAML file and returns its contents as a dictionary.

#### Arguments
- `file_path` (str): The path to the YAML file.

### main()

The main function of the script. It parses command-line arguments, processes YAML files, runs simulations, and generates plots and graph representations.

## Usage

To use the `physarum.py` script, provide one or more YAML files as command-line arguments:

```
python physarum.py --files physarum/21/physarum.yaml physarum/22/physarum.yaml physarum/23/physarum.yaml
```

Alternatively, you can specify a folder containing YAML files:

```
python physarum.py --folder physarum
```

The script will process each YAML file, run the corresponding simulation, and generate plots and graph representations for each simulation.

The YAML files should have the following structure:

```yaml
name: Simulation Name
grid_size: 100
steps: 1000
diffusion_coefficient: 1.0
reaction_rate: 0.055
k: 0.062
initial_u_value: 0.5
initial_v_value: 0.25
initial_radius: 10
conditions:
  time: 30
  temperature: 25
  humidity: 0.8
outputs:
  - activator
  - inhibitor
```

The script will generate PNG files for the activator chemical concentration plot, the simulation graph representation, and the hierarchical structure of the Physarum colony.
