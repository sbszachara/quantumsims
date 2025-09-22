# ===============================================
# File: quantum_sim.py
# Description: Simulates a quantum circuit and models fidelity as affected by noise and QEC
# Mapping to Framework:
# - Runtime QEC logic that affects effective noise model
# ===============================================

from qiskit import QuantumCircuit
from qiskit_aer import Aer

def run_qec_strategy(strategy, context="default"):
    """
    Simulates a toy circuit under a given QEC strategy and environmental context.
    This abstracts the 'dynamic instruction compiler' layer referenced in the proposal.
    """

    # Build a single-qubit quantum circuit
    qc = QuantumCircuit(1, 1)
    qc.h(0)         # Apply Hadamard (to create superposition)
    qc.measure(0, 0)  # Measure in Z-basis

    # Base noise per context (environmental source)
    base_noise = {
        "idle": 0.05,
        "coherent-noise": 0.15,
        "readout-error": 0.25
    }.get(context, 0.10)  # default fallback

    # QEC strategy modifies how much of that noise gets suppressed
    noise_factor = {
        "full_qec": 0.3,    # Strong suppression
        "light_qec": 0.6,   # Partial suppression
        "inaction": 1.0     # No suppression
    }.get(strategy, 1.0)

    effective_noise = base_noise * noise_factor
    fidelity = 1.0 - effective_noise  # Toy fidelity model: 1 - noise

    # Execute on Qiskit Aer simulator backend
    simulator = Aer.get_backend('aer_simulator')
    job = simulator.run(qc, shots=100)
    result = job.result()
    counts = result.get_counts(qc)

    return {"counts": counts, "fidelity": fidelity}
