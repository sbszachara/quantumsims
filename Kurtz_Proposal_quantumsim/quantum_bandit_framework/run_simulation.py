from quantum_sim import run_qec_strategy
from bandit import ContextualTSBandit, NSBandit
from ml_models import predict_noise, predict_mitigation_gain
import random

def get_context():
    return random.choice(["idle", "coherent-noise", "readout-error"])

def safety_check(context, strategy):
    conf = predict_noise(context)["confidence"]
    thresholds = {"full_qec": 0.5, "light_qec": 0.2, "inaction": 0.0}
    return conf >= thresholds[strategy]

def apply_mitigation(strategy, fidelity):
    gains = {"zne": 0.03, "pec": 0.05, "mem": 0.02, "none": 0.0}
    return min(1.0, fidelity + gains.get(strategy, 0.0))

def main():
    qec_bandit = ContextualTSBandit(["full_qec", "light_qec", "inaction"])
    post_bandit = NSBandit(["zne", "pec", "mem", "none"])

    for i in range(10):
        print(f"\n--- Trial {i+1} ---")
        context = get_context()
        print("Context:", context)

        strategy = qec_bandit.choose_arm(context)
        if not safety_check(context, strategy):
            print("Blocked by safety rules. Using 'inaction'.")
            strategy = "inaction"

        result = run_qec_strategy(strategy, context)
        fidelity = result["fidelity"]
        print(f"QEC Strategy: {strategy} | Fidelity: {fidelity:.4f}")
        qec_bandit.update(context, strategy, fidelity)

        mitigation = post_bandit.choose_arm()
        final_fidelity = apply_mitigation(mitigation, fidelity)
        print(f"Mitigation: {mitigation} | Final Fidelity: {final_fidelity:.4f}")
        post_bandit.update(mitigation, final_fidelity)

    print("\nSimulation complete.")

if __name__ == "__main__":
    main()