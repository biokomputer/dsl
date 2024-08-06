import argparse
import os
import yaml
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict
import graphviz


# Definicje struktur danych
class Simulation:
    def __init__(self, name: str, growth_rate: float,
                 conditions: Dict, outputs: List[str]):
        self.name = name
        self.growth_rate = growth_rate
        self.conditions = conditions
        self.outputs = outputs

# Stałe modelu
D = 0.1  # Współczynnik dyfuzji
f = 0.04  # Tempo reakcji
k = 0.06  # Krystalizacja

def simulate_reaction_diffusion(n, steps, D, f, k, initial_u_value, initial_v_value, initial_radius):
    u = np.ones((n, n))
    v = np.zeros((n, n))

    # Inicjalizacja w centrum reaktora
    r = initial_radius
    u[n//2-r:n//2+r, n//2-r:n//2+r] = initial_u_value
    v[n//2-r:n//2+r, n//2-r:n//2+r] = initial_v_value

    def laplacian(Z):
        return (
            -4*Z +
            np.roll(Z, (0, 1), (0, 1)) +
            np.roll(Z, (0, -1), (0, 1)) +
            np.roll(Z, (1, 0), (0, 1)) +
            np.roll(Z, (-1, 0), (0, 1))
        )

    for _ in range(steps):
        uvv = u * v * v
        du = (D * laplacian(u) - uvv + f * (1 - u))
        dv = (D * laplacian(v) + uvv - (f + k) * v)
        u += du
        v += dv

    return u, v



# Generowanie grafu hierarchicznego
def generate_graphviz_hierarchy(output_file):
    dot = graphviz.Digraph(comment='Physarum Hierarchical Structure')
    dot.node('A', 'Physarum polycephalum')
    for i in range(1, 5):
        dot.node(f'B{i}', f'Nucleus {i}')
        dot.edge('A', f'B{i}')
        for j in range(1, 5):
            dot.node(f'C{i}{j}', f'Sub Nucleus {i}{j}')
            dot.edge(f'B{i}', f'C{i}{j}')
    dot.render(output_file, format='png', cleanup=True)


generate_graphviz_hierarchy('physarum_hierarchy')

# Funkcja generująca wykres wzrostu biomasy
def generate_plot(u, v, output_file):
    plt.figure()
    plt.imshow(u, cmap='hot')
    plt.colorbar()
    plt.title("Physarum polycephalum Growth")
    plt.savefig(f"{output_file}.png")
    plt.close()


# Funkcja generująca definicję grafu
def generate_graphviz_text(simulation_params, output_file):
    content = f"""
    digraph G {{
        node [shape=record];
        "Simulation" [label="{{Name: {simulation_params['name']}|Initial Population: {simulation_params['initial_u_value']}|Growth Rate: {simulation_params['reaction_rate']}|Conditions: time={simulation_params['conditions']['time']}, temperature={simulation_params['conditions']['temperature']}, humidity={simulation_params['conditions']['humidity']}}}" ];
    }}
    """
    with open(f"{output_file}.dot", 'w') as file:
        file.write(content)


# Funkcja generująca graficzną reprezentację grafu
def generate_graphviz_image(output_file):
    dot_file = f"{output_file}.dot"
    graphviz.render('dot', 'png', dot_file)

# Funkcja do tworzenia obiektów symulacji Physarum z pliku YAML
def parse_yaml_to_simulation(yaml_data: dict):
    return yaml_data

# Funkcja do wczytywania plików YAML
def load_yaml_from_file(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Główna funkcja obsługująca folder i pliki YAML
def main():
    parser = argparse.ArgumentParser(description='Run Physarum growth simulations from YAML files.')
    parser.add_argument('--files', type=str, nargs='*', help='The YAML files to process')
    parser.add_argument('--folder', type=str, help='Folder containing YAML files')

    args = parser.parse_args()

    files = args.files if args.files else []
    if args.folder:
        for file_name in os.listdir(args.folder):
            if file_name.endswith('.yaml'):
                files.append(os.path.join(args.folder, file_name))

    if not files:
        print("No YAML files specified.")
        return

    for file in files:
        yaml_data = load_yaml_from_file(file)
        simulation_params = parse_yaml_to_simulation(yaml_data)

        n = simulation_params['grid_size']
        steps = simulation_params['steps']
        D = simulation_params['diffusion_coefficient']
        f = simulation_params['reaction_rate']
        k = simulation_params['k']
        initial_u_value = simulation_params['initial_u_value']
        initial_v_value = simulation_params['initial_v_value']
        initial_radius = simulation_params['initial_radius']

        u, v = simulate_reaction_diffusion(n, steps, D, f, k, initial_u_value, initial_v_value, initial_radius)

        base_name = os.path.splitext(file)[0]
        generate_plot(u, v, base_name)
        generate_graphviz_text(simulation_params, base_name)
        generate_graphviz_image(base_name)


if __name__ == "__main__":
    main()