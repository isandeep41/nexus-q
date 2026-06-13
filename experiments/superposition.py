"""
Quantum Superposition Experiment

This script demonstrates how to place a single qubit into a state of quantum superposition
using a Hadamard gate, and then measure its state.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import Sampler

def run_superposition_experiment():
    # 1. Create a Quantum Circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)

    # 2. Apply a Hadamard gate to put the qubit in superposition
    qc.h(0)

    # 3. Measure the qubit
    qc.measure(0, 0)

    print("Circuit Diagram:")
    print(qc.draw())

    # 4. Execute the circuit using the Sampler primitive
    sampler = Sampler()
    job = sampler.run(qc)
    result = job.result()
    
    # 5. Extract probabilities
    quasi_dists = result.quasi_dists[0]
    
    print("\nResults (Quasi-Probabilities):")
    print(f"State |0>: {quasi_dists.get(0, 0):.4f}")
    print(f"State |1>: {quasi_dists.get(1, 0):.4f}")
    print("Due to superposition, you should see roughly a 50/50 split.")

if __name__ == "__main__":
    run_superposition_experiment()
