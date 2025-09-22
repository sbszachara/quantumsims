# QuantumSims – Weekend Project Overview

This repo has two versions of a simple quantum-bandit simulation:

1. A really basic prototype that just lets a bandit pick a strategy and either runs a quantum circuit or a dummy response.
2. A more built-out version where the bandit decisions depend on the context, and there's support for post-processing and some ML stubs.

---

## Simple Version

This version is a minimal working example. It uses a bandit to randomly choose between:

- `strategy_1`: Runs a simple Qiskit circuit (Hadamard + measurement)
- `strategy_2`: Returns a dummy result (even 50/50 outcome)

### Files

- `bandit.py` – defines `SimpleBandit` with two random strategies
- `quantum_sim.py` – runs the Qiskit circuit
- `run_simulation.py` – uses the bandit to choose and run the circuit

### To Run

```bash
pip install qiskit
python run_simulation.py
```

You'll see the bandit pick a strategy and print out either real or dummy quantum results.

---

## Advanced Version (Contextual Bandits + ML)

This version is inspired by an idea from Daniel Krutz's adaptive quantum error management work. It adds:

- Context-aware strategy selection (using simulated telemetry)
- Post-processing error mitigation (like PEC or ZNE)
- Placeholders for future ML integration (like DRL or SVGP)

### Files

- `run_simulation.py` – main driver for the contextual logic
- `quantum_sim.py` – quantum simulator with fidelity modeling
- `bandit.py` – defines `ContextualTSBandit` and `NSBandit`
- `ml_models.py` – stub file where ML models would go

### To Run

```bash
git clone https://github.com/sbszachara/quantumsims.git
cd quantumsims/quantum_bandit_framework
python3 -m venv venv
source venv/bin/activate        # or venv\Scripts\activate on Windows
pip install qiskit numpy
python run_simulation.py
```

It runs through 10 simulated trials and prints contextual strategy selections and fidelity values.

---

## What's Missing

- No real ML models yet, but stubs are in place (`ml_models.py`)
- Could be extended with PyTorch or scikit-learn
- No visualization/logging yet

---

## License

MIT