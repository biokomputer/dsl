import argparse
import yaml
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict


# Definicje struktur danych
class Simulation:
    def __init__(self, name: str, initial_population: float, growth_rate: float, carrying_capacity: float,
                 conditions: Dict, outputs: List[str]):
        self.name = name
        self.initial_population = initial_population
        self.growth_rate = growth_rate
        self.carrying_capacity = carrying_capacity
        self.conditions = conditions
        self.outputs = outputs


# Funkcja do wczytywania z pliku YAML
def load_yaml_from_file(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


# Funkcja do uruchamiania symulacji wzrostu grzybów
def run_simulation(simulation: Simulation):
    time = np.linspace(0, simulation.conditions['time'], 100)  # Generowanie 100 punktów czasowych
    N = simulation.initial_population
    r = simulation.growth_rate
    K = simulation.carrying_capacity

    # Równanie logistyczne: dN/dt = rN(1 - N/K)
    def logistic_growth(t, N):
        return r * N * (1 - N / K)

    # Symulacja wzrostu populacji
    biomass_levels = [N]
    dt = time[1] - time[0]
    for t in time[1:]:
        N = N + logistic_growth(t, N) * dt
        biomass_levels.append(N)

    # Wizualizacja wyników
    plt.figure()
    plt.plot(time, biomass_levels, label=f"{simulation.outputs[0]}")
    plt.title(f"Simulation: {simulation.name}")
    plt.xlabel("Time (days)")
    plt.ylabel("Biomass")
    plt.legend()
    plt.show()


# Funkcja do tworzenia obiektów symulacji z pliku YAML
def parse_yaml_to_simulation(yaml_data: dict) -> Simulation:
    return Simulation(
        name=yaml_data["name"],
        initial_population=yaml_data["initial_population"],
        growth_rate=yaml_data["growth_rate"],
        carrying_capacity=yaml_data["carrying_capacity"],
        conditions=yaml_data["conditions"],
        outputs=yaml_data["outputs"]
    )


# Główna funkcja
def main():
    parser = argparse.ArgumentParser(description='Run fungal growth simulation from YAML file.')
    parser.add_argument('file', type=str, nargs='?', default='fungi_simulation_1.yaml',
                        help='The YAML file to process (default: fungi_simulation_1.yaml)')

    args = parser.parse_args()
    yaml_data = load_yaml_from_file(args.file)
    simulation = parse_yaml_to_simulation(yaml_data)
    run_simulation(simulation)


if __name__ == "__main__":
    main()