from pyparsing import Word, alphas, alphanums, Group, Optional, Suppress, Keyword, delimitedList, quotedString, removeQuotes, Forward
import argparse
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict

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
    dsl_expr = Forward()
    dsl_expr <<= (molecule_expr | logic_gate_expr | biological_system_expr | simulation_expr)
    parsed_result = dsl_expr.searchString(dsl_code)
    return parsed_result


# Pobieranie DSL z pliku (przykładowo)

dsl_code = """
molecule DNA(name="Plasmid123", sequence="ATGCGTACG...")
molecule Protein(name="GFP", expression="Plasmid123", structure="AlphaHelix")

logic_gate AND(
    input1=Protein(name="Input1Prot"),
    input2=Protein(name="Input2Prot"),
    output=Protein(name="OutputProt")
)

biological_system BioCompSystem1 {
    logic_gates = [AND]
    molecules = [Protein(name="Input1Prot"), Protein(name="Input2Prot"), Protein(name="OutputProt")]
}

simulation BioCompSim1 {
    system = BioCompSystem1
    conditions {
        time = 100  # in minutes
        temperature = 37  # in Celsius
    }
    outputs = ["Protein OutputProt"]
}
"""
parsed_result = parse_dsl(dsl_code)
print(parsed_result)


#  przetwarzania wyniku parsera w obiektywne struktury danych:

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
    logic_gates = []
    biological_systems = {}
    simulations = {}

    for result in parsed_result:
        if result[0] == "molecule":
            molecule = create_molecule(result)
            molecules[molecule.name] = molecule
        elif result[0] == "logic_gate":
            logic_gate = create_logic_gate(result)
            logic_gates.append(logic_gate)
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
            simulations[simulation.system] = simulation

    return simulations

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


parsed_objects = parse_dsl_to_objects(parsed_result)
print(parsed_objects)
simulation = parsed_objects["BioCompSystem1"]
run_simulation(simulation)
