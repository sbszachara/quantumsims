from quantum_sim import run_quantum_circuit
from bandit import SimpleBandit

def main():
    bandit = SimpleBandit()
    chosen_arm = bandit.choose_arm()
    
    print(f"Bandit chose: {chosen_arm}")
    result = run_quantum_circuit() if chosen_arm == 'strategy_1' else {"0": 50, "1": 50}  # Another dummy strategy
    print("Quantum result:", result)

if __name__ == "__main__":
    main()
