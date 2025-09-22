from qiskit import QuantumCircuit
from qiskit_aer import Aer

def run_qec_strategy(strategy, context="default"):
    """ Simulates runtime QEC strategy. Adjusts circuit fidelity based on 'strategy' and 'context' """
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    
    base_noise = {
        "idle": 0.05,
        "coherent-noise": 0.15,
        "readout-error": 0.25
    }.get(context, 0.10)

    noise_factor = {
        "full_qec": 0.3,
        "light_qec": 0.6,
        "inaction": 1.0
    }.get(strategy, 1.0)

    effective_noise = base_noise * noise_factor
    fidelity = 1.0 - effective_noise

    simulator = Aer.get_backend('aer_simulator')
    job = simulator.run(qc, shots=100)
    result = job.result()
    counts = result.get_counts(qc)
    return {"counts": counts, "fidelity": fidelity}