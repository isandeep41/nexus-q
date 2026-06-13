"""
Quantum Entanglement & EPR Paradox Experiment

This script demonstrates how to create an entangled pair of qubits (a Bell state)
and measure them, showing that their outcomes are perfectly correlated.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

def run_entanglement_experiment():
    # 1. Create a Quantum Circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2, 2)

    # 2. Apply a Hadamard gate to the first qubit
    qc.h(0)

    # 3. Apply a CNOT gate with qubit 0 as control and qubit 1 as target
    qc.cx(0, 1)

    # 4. Measure both qubits
    qc.measure([0, 1], [0, 1])

    print("Circuit Diagram:")
    print(qc.draw())

    # 5. Execute the circuit using the StatevectorSampler primitive
    sampler = StatevectorSampler()
    job = sampler.run([qc])
    result = job.result()
    
    # 6. Extract probabilities
    counts = result[0].data.c.get_counts()
    shots = sum(counts.values())
    
    print("\nResults (Quasi-Probabilities):")
    # Qiskit uses little-endian ordering, so bit 0 is the rightmost bit
    print(f"State |00>: {counts.get('00', 0)/shots:.4f}")
    print(f"State |11>: {counts.get('11', 0)/shots:.4f}")
    print("Notice the strong correlation between the two qubits, indicative of entanglement.")

if __name__ == "__main__":
    run_entanglement_experiment()
