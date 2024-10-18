import yaml
from src.biocomp.biocomp import BiologicalSystem, Simulation, run_simulation
from biograph import visualize_biological_system
from fungi import run_simulation as run_fungi_simulation
from physarum import simulate_reaction_diffusion, generate_plot, generate_graphviz_hierarchy

def main():
    # Load a YAML file and create a BiologicalSystem
    with open("biosystem/1/biocomp.yaml", "r") as file:
        data = yaml.safe_load(file)
    
    bio_system = BiologicalSystem(
        name=data["biological_system"]["name"],
        logic_gates=[],  # Populate with LogicGate objects
        molecules=[]     # Populate with Molecule objects
    )

    # Run a simulation
    simulation = Simulation(
        system=bio_system,
        conditions=data["simulation"]["conditions"],
        outputs=data["simulation"]["outputs"]
    )
    run_simulation(simulation)

    # Generate a graph visualization
    visualize_biological_system(bio_system)

    # Run a fungi simulation
    run_fungi_simulation(simulation)

    # Run a physarum simulation
    physarum_sim = simulate_reaction_diffusion(simulation)
    generate_plot(*physarum_sim, "physarum_plot")
    generate_graphviz_hierarchy(simulation, "physarum_hierarchy")

if __name__ == "__main__":
    main()
