import argparse
import matplotlib.pyplot as plt
import numpy as np
from pyparsing import Word, alphas, alphanums, Group, Optional, Suppress, Keyword, delimitedList


def load_dsl_from_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        dsl_code = file.read()
    return dsl_code


def run_simulation(simulation):
    time = np.linspace(0, float(simulation.conditions["time"]), 100)  # Generate 100 time points
    output_levels = np.sin(time) / 2 + 0.5  # Example function to simulate protein output level

    plt.figure()
    plt.plot(time, output_levels, label=f"{simulation.outputs[0]}")
    plt.title(f"Simulation: {simulation.system.name}")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Output Level")
    plt.legend()
    plt.show()


def parse_dsl(dsl_code: str):
    identifier = Word(alphas, alphanums + "_")
    value = Word(alphanums + "_.")

    molecule_expr = Group(
        Keyword("molecule") + identifier("type")
        + Suppress("(") + identifier("name")
        + Optional(Suppress(",") + identifier("sequence") + Suppress("=") + value("sequence"))
        + Optional(Suppress(",") + identifier("expression") + Suppress("=") + value("expression"))
        + Optional(Suppress(",") + identifier("structure") + Suppress("=") + value("structure"))
        + Suppress(")")
    )

    logic_gate_expr = Group(
        Keyword("logic_gate") + identifier("gate_type")
        + Suppress("(")
        + identifier("input1") + Suppress("=") + identifier("input1Prot")
        + Suppress(",") + identifier("input2") + Suppress("=") + identifier("input2Prot")
        + Suppress(",") + identifier("output") + Suppress("=") + identifier("outputProt")
        + Suppress(")")
    )

    system_expr = Group(
        Keyword("biological_system") + identifier("name")
        + Suppress("{")
        + Keyword("logic_gates") + Suppress("=") + Group(
            Suppress("[") + delimitedList(logic_gate_expr) + Suppress("]"))("logic_gates")
        + Keyword("molecules") + Suppress("=") + Group(Suppress("[") + delimitedList(molecule_expr) + Suppress("]"))(
            "molecules")
        + Suppress("}")
    )

    simulation_expr = Group(
        Keyword("simulation") + identifier("name")
        + Suppress("{")
        + Keyword("system") + Suppress("=") + identifier("system")
        + Keyword("conditions") + Suppress("{")
        + Group(
            Keyword("time") + Suppress("=") + value("time")
            + Suppress(",") + Keyword("temperature") + Suppress("=") + value("temperature")
        )("conditions")
        + Suppress("}")
        + Keyword("outputs") + Suppress("=") + Group(Suppress("[") + delimitedList(identifier) + Suppress("]"))(
            "outputs")
        + Suppress("}")
    )

    # dsl_expr = molecule_expr | logic_gate_expr
    dsl_expr = molecule_expr | logic_gate_expr | system_expr | simulation_expr
    # print(dsl_expr)
    # print(molecule_expr)
    # print(simulation_expr)
    parsed_result = dsl_expr.searchString(dsl_code)
    # print(parsed_result)

    return parsed_result


class Molecule:
    def __init__(self, type: str, name: str, sequence: str = None, expression: str = None, structure: str = None):
        self.type = type
        self.name = name
        self.sequence = sequence
        self.expression = expression
        self.structure = structure


class LogicGate:
    def __init__(self, gate_type: str, input1: Molecule, input2: Molecule, output: Molecule):
        self.gate_type = gate_type
        self.input1 = input1
        self.input2 = input2
        self.output = output


class BiologicalSystem:
    def __init__(self, name: str, logic_gates, molecules):
        self.name = name
        self.logic_gates = logic_gates
        self.molecules = molecules


class Simulation:
    def __init__(self, system: BiologicalSystem, conditions, outputs):
        self.system = system
        self.conditions = conditions
        self.outputs = outputs


def create_molecule(parsed_molecule):
    return Molecule(
        type=parsed_molecule[0],
        name=parsed_molecule[1],
        sequence=parsed_molecule.get("sequence"),
        expression=parsed_molecule.get("expression"),
        structure=parsed_molecule.get("structure")
    )


def create_logic_gate(parsed_logic_gate, molecules_dict):
    input1 = molecules_dict[parsed_logic_gate["input1Prot"]]
    input2 = molecules_dict[parsed_logic_gate["input2Prot"]]
    output = molecules_dict[parsed_logic_gate["outputProt"]]
    return LogicGate(
        gate_type=parsed_logic_gate["gate_type"],
        input1=input1,
        input2=input2,
        output=output
    )


def parse_dsl_to_objects(parsed_result):
    molecules_dict = {}
    logic_gates = []
    biological_systems = {}
    simulations = {}

    for result in parsed_result:
        if result[0] == "molecule":
            molecule = create_molecule(result)
            molecules_dict[molecule.name] = molecule
        elif result[0] == "logic_gate":
            logic_gate = create_logic_gate(result, molecules_dict)
            logic_gates.append(logic_gate)
        elif result[0] == "biological_system":
            logic_gates_list = [create_logic_gate(gate, molecules_dict) for gate in result["logic_gates"]]
            molecules_list = [create_molecule(mol) for mol in result["molecules"]]
            bio_system = BiologicalSystem(name=result["name"], logic_gates=logic_gates_list, molecules=molecules_list)
            biological_systems[bio_system.name] = bio_system
        elif result[0] == "simulation":
            system = biological_systems[result["system"]]
            conditions = {cond[0]: float(cond[1]) for cond in result["conditions"]}
            outputs = result["outputs"]
            simulation = Simulation(system=system, conditions=conditions, outputs=outputs)
            simulations[result["name"]] = simulation

    return simulations


def main():
    parser = argparse.ArgumentParser(description='Run BioComputing simulation from DSL file.')
    parser.add_argument('file', type=str, nargs='?', default='sym.biocomp',
                        help='The DSL file to process (default: sym.biocomp)')
    parser.add_argument('simulation', type=str, nargs='?', default='BioCompSim1',
                        help='The DSL file to process (default: BioCompSim1)')

    args = parser.parse_args()
    if args.file:
        dsl_code = load_dsl_from_file(args.file)
        if not dsl_code:
            print(f"NOT Parsed FILE")
        print(dsl_code)
        parsed_result = parse_dsl(dsl_code)
        if not parsed_result:
            print(f"NOT Parsed CODE")
        parsed_objects = parse_dsl_to_objects(parsed_result)
        if not parsed_objects:
            print(f"NOT Parsed DSL objects")
            return
        if parsed_objects and args.simulation:
            simulation_name = args.simulation
            simulation = parsed_objects[simulation_name]
            run_simulation(simulation)


if __name__ == "__main__":
    main()
