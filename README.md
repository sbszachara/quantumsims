# QuantumSims – Full Project Overview

This repository includes **two quantum simulation frameworks**:
1. 🔹 A simple Qiskit + Bandit integration (minimal prototype)
2. 🔸 A full adaptive simulation based on contextual bandits and machine learning

---

## 📁 Simple Quantum Bandit Framework

This is a very minimal prototype showing how a bandit algorithm can pick between two strategies, one of which runs a small quantum circuit in Qiskit.

### 📄 Files

- `bandit.py` – defines a SimpleBandit class with two strategies (random choice)
- `quantum_sim.py` – runs a one-qubit Hadamard circuit and measures outcomes with Qiskit Aer
- `run_simulation.py` – main driver, uses the bandit to pick a strategy and then runs either the quantum circuit or a dummy alternative

### ⚙️ Install

```bash
pip install qiskit
```

### ▶️ Run

```bash
python run_simulation.py
```

### 🔍 What Happens

- The bandit picks either `strategy_1` or `strategy_2`.
- If it picks `strategy_1`, it runs a Hadamard + measure circuit.
- If it picks `strategy_2`, it just returns dummy results `{"0": 50, "1": 50}`.

This shows a minimal quantum + bandit setup.

---

## 🧠 Advanced Quantum Bandit Framework

This module simulates adaptive quantum error management strategies using contextual bandits and post-processing logic. It is based on the proposal: _Contextual and Uncertainty-Aware Adaptive Quantum Error Management_ by Daniel Krutz (RIT).

### 📁 Files

- `run_simulation.py` – Main orchestrator: handles context, QEC selection, mitigation, and logging
- `quantum_sim.py` – Qiskit circuit + simulated noise modeling
- `bandit.py` – Contextual and non-stationary bandit strategies
- `ml_models.py` – Placeholder for future ML-based prediction (e.g., DRL, PyTorch, SVGP)

### 📥 Clone the Repository

```bash
git clone https://github.com/sbszachara/quantumsims.git
cd quantumsims/quantum_bandit_framework
```

### ⚙️ Setup (Virtual Environment Recommended)

```bash
python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install qiskit numpy
```

### ▶️ Run

```bash
python run_simulation.py
```

You'll see contextual episodes with chosen QEC strategy, simulated fidelity, and post-mitigation steps.

---

## 🧱 Future Work

- Plug in PyTorch models to `ml_models.py`
- Replace Gaussian bandits with learned TS/UCB policies
- Visualize results (e.g. fidelity over time) with Matplotlib

---

## 📜 License

MIT License — Feel free to fork, reuse, and build upon.
