# Definiowanie Struktur DSL w Pythonie
from typing import List, Dict

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
    def __init__(self, name: str, logic_gates: List[LogicGate], molecules: List[Molecule]):
        self.name = name
        self.logic_gates = logic_gates
        self.molecules = molecules

class Simulation:
    def __init__(self, system: BiologicalSystem, conditions: Dict[str, float], outputs: List[str]):
        self.system = system
        self.conditions = conditions
        self.outputs = outputs
      
from pyparsing import Word, alphas, alphanums, Group, Optional, Suppress, Keyword, delimitedList

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
        + Keyword("logic_gates") + Suppress("=") + Group(Suppress("[") + delimitedList(logic_gate_expr) + Suppress("]"))("logic_gates")
        + Keyword("molecules") + Suppress("=") + Group(Suppress("[") + delimitedList(molecule_expr) + Suppress("]"))("molecules")
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
        + Keyword("outputs") + Suppress("=") + Group(Suppress("[") + delimitedList(identifier) + Suppress("]"))("outputs")
        + Suppress("}")
    )

    dsl_expr = molecule_expr | logic_gate_expr | system_expr | simulation_expr
    parsed_result = dsl_expr.searchString(dsl_code)
    return parsed_result


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


# Load dsl_code from file
def load_dsl_from_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        dsl_code = file.read()
    return dsl_code

filename="sym1.biocomp"
dsl_code = load_dsl_from_file(filename)


parsed_result = parse_dsl(dsl_code)
print(parsed_result)


# Przetwarzanie wyników parsowania i symulacja
import matplotlib.pyplot as plt
import numpy as np

def run_simulation(simulation: Simulation):
    time = np.linspace(0, simulation.conditions["time"], 100)  # Generate 100 time points
    output_levels = np.random.rand(100)  # Random values to simulate protein output level

    plt.figure()
    plt.plot(time, output_levels, label=f"{simulation.outputs[0]}")
    plt.title(f"Simulation: {simulation.system.name}")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Output Level")
    plt.legend()
    plt.show()

# Przyklad zdefiniowanych danych
input1_prot = Molecule(type="Protein", name="Input1Prot")
input2_prot = Molecule(type="Protein", name="Input2Prot")
output_prot = Molecule(type="Protein", name="OutputProt")

and_gate = LogicGate(gate_type="AND", input1=input1_prot, input2=input2_prot, output=output_prot)
bio_system = BiologicalSystem(name="BioCompSystem1", logic_gates=[and_gate], molecules=[input1_prot, input2_prot, output_prot])

simulation_conditions = {"time": 100, "temperature": 37}
simulation = Simulation(system=bio_system, conditions=simulation_conditions, outputs=["Protein OutputProt"])

run_simulation(simulation)
