# ===============================================
# File: bandit.py
# Description: Implements two types of multi-armed bandits used to select runtime QEC and post-processing strategies.
# Mapping to Framework:
# - The ContextualTSBandit reflects the Thompson Sampling with Contextual Linear Models (TS-CL)
# - The NSBandit serves as a lightweight non-contextual bandit used for post-processing strategy selection
# ===============================================

import random
from collections import defaultdict

class ContextualTSBandit:
    def __init__(self, arms):
        # Each 'arm' corresponds to a QEC strategy (e.g., full_qec, light_qec, inaction)
        self.arms = arms
        # Rewards are stored by context → arm → list of fidelities observed
        self.rewards = defaultdict(lambda: defaultdict(list))

    def choose_arm(self, context):
        # This function models Thompson Sampling with Gaussian priors per context-arm
        means = {}
        for arm in self.arms:
            r = self.rewards[context][arm]
            # If reward history exists, sample from normal(mean, 0.1) else use uniform random
            means[arm] = random.gauss(sum(r)/len(r), 0.1) if r else random.random()
        # Select the arm with the highest sampled reward
        return max(means, key=means.get)

    def update(self, context, arm, reward):
        # Update the rewards with observed fidelity for (context, strategy)
        self.rewards[context][arm].append(reward)


class NSBandit:
    def __init__(self, arms):
        # Post-processing strategies (PEC, ZNE, MEM, none)
        self.arms = arms
        self.rewards = defaultdict(list)

    def choose_arm(self):
        # Uses average reward over recent 5 runs to select best strategy
        def score(r): return sum(r[-5:]) / min(5, len(r)) if r else random.random()
        return max(self.arms, key=lambda arm: score(self.rewards[arm]))

    def update(self, arm, reward):
        # Update observed reward (fidelity) for the mitigation strategy
        self.rewards[arm].append(reward)
