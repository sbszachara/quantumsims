from qiskit import QuantumCircuit, Aer, execute

def run_quantum_circuit():
    # Create a simple quantum circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Apply Hadamard gate to put qubit in superposition
    qc.measure(0, 0)
    
    # Use the Aer simulator
    simulator = Aer.get_backend('aer_simulator')
    job = execute(qc, simulator, shots=100)
    result = job.result()
    
    # Return counts of outcomes
    counts = result.get_counts(qc)
    return counts

if __name__ == "__main__":
    print(run_quantum_circuit())
