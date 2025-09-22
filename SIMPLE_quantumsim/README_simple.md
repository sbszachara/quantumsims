# Simple Quantum Bandit Framework

This is a very minimal prototype showing how a bandit algorithm can pick between two strategies, one of which runs a small quantum circuit in Qiskit.

## Files

bandit.py – defines a SimpleBandit class with two strategies (random choice)
quantum_sim.py – runs a one-qubit Hadamard circuit and measures outcomes with Qiskit Aer
run_simulation.py – main driver, uses the bandit to pick a strategy and then runs either the quantum circuit or a dummy alternative

## Install

Needs Python 3.8+ and Qiskit. Install with:
pip install qiskit

## Run

From the project folder:
python run_simulation.py

## What happens

- The bandit picks either `strategy_1` or `strategy_2`.
- If it picks `strategy_1`, it runs a simple quantum circuit (Hadamard + measurement) and prints the counts of 0/1 results.
- If it picks `strategy_2`, it just prints a dummy balanced outcome.

This just shows how to wire a bandit decision together with a quantum call in the simplest way.
