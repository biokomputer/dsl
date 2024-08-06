import argparse
import matplotlib.pyplot as plt
import numpy as np
from pyparsing import Word, alphas, alphanums, Group, Optional, Suppress, Keyword, delimitedList, quotedString, \
    removeQuotes, Forward
from typing import List, Dict


# Definicje struktur danych
class Molecule:
    def __init__(self, type: str, name: str, sequence: str = None, expression: str = None, structure: str = None):
        self.type = type
        self.name = name
        self.sequence = sequence
        self.expression = expression
        self.structure = structure


class LogicGate:
    def __init__(self, gate_type: str, input1: str, input2: str, output: str):
        self.gate_type = gate_type
        self.input1 = input1
        self.input2 = input2
        self.output = output


class BiologicalSystem:
    def __init__(self, name: str, logic_gates: List[str], molecules: List[str]):
        self.name = name
        self.logic_gates = logic_gates
        self.molecules = molecules


class Simulation:
    def __init__(self, system: str, conditions: Dict[str, float], outputs: List[str]):
        self.system = system
        self.conditions = conditions
        self.outputs = outputs


# Funkcja do wczytywania z pliku
def load_dsl_from_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        dsl_code = file.read()
    return dsl_code


# Funkcja do uruchamiania symulacji
def run_simulation(simulation):
    time = np.linspace(0, float(simulation.conditions["time"]), 100)  # Generate 100 time points
    output_levels = np.sin(time) / 2 + 0.5  # Example function to simulate protein output level

    plt.figure()
    plt.plot(time, output_levels, label=f"{simulation.outputs[0]}")
    plt.title(f"Simulation: {simulation.system}")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Output Level")
    plt.legend()
    plt.show()


# Funkcja do parsowania DSL
def parse_dsl(dsl_code: str):
    identifier = Word(alphas, alphanums + "_")
    value = Word(alphanums + "_.")
    string_value = quotedString.setParseAction(removeQuotes)

    # Molecule expression
    molecule_expr = Group(
        Keyword("molecule") + identifier("type")
        + Suppress("(")
        + "name" + Suppress("=") + string_value("name")
        + Optional(Suppress(",") + "sequence" + Suppress("=") + string_value("sequence"))
        + Optional(Suppress(",") + "expression" + Suppress("=") + string_value("expression"))
        + Optional(Suppress(",") + "structure" + Suppress("=") + string_value("structure"))
        + Suppress(")")
    )

    # Logic gate expression
    logic_gate_expr = Group(
        Keyword("logic_gate") + identifier("gate_type")
        + Suppress("(")
        + "input1" + Suppress("=") + identifier("input1Prot")
        + Suppress(",") + "input2" + Suppress("=") + identifier("input2Prot")
        + Suppress(",") + "output" + Suppress("=") + identifier("outputProt")
        + Suppress(")")
    )

    # Biological system expression
    biological_system_expr = Group(
        Keyword("biological_system") + identifier("name")
        + Suppress("{")
        + "logic_gates" + Suppress("=") + Group(Suppress("[") + delimitedList(identifier) + Suppress("]"))(
            "logic_gates")
        + "molecules" + Suppress("=") + Group(Suppress("[") + delimitedList(identifier) + Suppress("]"))("molecules")
        + Suppress("}")
    )

    # Condition clause in simulations
    condition_expr = Group(
        "conditions" + Suppress("{")
        + "time" + Suppress("=") + value("time")
        + Suppress("# in minutes")
        + "temperature" + Suppress("=") + value("temperature")
        + Suppress("# in Celsius")
        + Suppress("}")
    )

    # Simulation expression
    simulation_expr = Group(
        Keyword("simulation") + identifier("name")
        + Suppress("{")
        + "system" + Suppress("=") + identifier("system")
        + condition_expr("conditions")
        + "outputs" + Suppress("=") + Group(Suppress("[") + delimitedList(string_value) + Suppress("]"))("outputs")
        + Suppress("}")
    )

    # Complete DSL expression
    dsl_expr = molecule_expr | logic_gate_expr | biological_system_expr | simulation_expr
    parsed_result = dsl_expr.searchString(dsl_code)
    return parsed_result


# Funkcja do tworzenia obiektów z parsowanych wyników
def create_molecule(parsed_molecule):
    return Molecule(
        type=parsed_molecule[0],
        name=parsed_molecule[1],
        sequence=parsed_molecule.get("sequence"),
        expression=parsed_molecule.get("expression"),
        structure=parsed_molecule.get("structure")
    )


def create_logic_gate(parsed_logic_gate):
    return LogicGate(
        gate_type=parsed_logic_gate["gate_type"],
        input1=parsed_logic_gate["input1Prot"],
        input2=parsed_logic_gate["input2Prot"],
        output=parsed_logic_gate["outputProt"]
    )


def parse_dsl_to_objects(parsed_result):
    molecules = {}
    logic_gates = {}
    biological_systems = {}
    simulations = {}

    for result in parsed_result:
        if result[0] == "molecule":
            molecule = create_molecule(result)
            molecules[molecule.name] = molecule
        elif result[0] == "logic_gate":
            logic_gate = create_logic_gate(result)
            logic_gates[logic_gate.gate_type] = logic_gate
        elif result[0] == "biological_system":
            bio_system = BiologicalSystem(
                name=result["name"],
                logic_gates=result["logic_gates"],
                molecules=result["molecules"]
            )
            biological_systems[bio_system.name] = bio_system
        elif result[0] == "simulation":
            simulation = Simulation(
                system=result["system"],
                conditions={
                    "time": float(result["conditions"]["time"]),
                    "temperature": float(result["conditions"]["temperature"])
                },
                outputs=result["outputs"]
            )
            simulations[result["name"]] = simulation

    return molecules, logic_gates, biological_systems, simulations


# Główna funkcja
def main():
    parser = argparse.ArgumentParser(description='Run BioComputing simulation from DSL file.')
    parser.add_argument('file', type=str, nargs='?', default='bio_comp.dsl',
                        help='The DSL file to process (default: bio_comp.dsl)')

    args = parser.parse_args()
    dsl_code = load_dsl_from_file(args.file)
    parsed_result = parse_dsl(dsl_code)
    molecules, logic_gates, biological_systems, simulations = parse_dsl_to_objects(parsed_result)

    print("Molecules:", molecules)
    print("Logic Gates:", logic_gates)
    print("Biological Systems:", biological_systems)
    print("Simulations:", simulations)

    # Assuming the BioCompSim1 simulation is to be found
    if "BioCompSim1" not in simulations:
        print("Simulation 'BioCompSim1' not found in parsed result.")
        return

    simulation = simulations["BioCompSim1"]
    run_simulation(simulation)


if __name__ == "__main__":
    main()