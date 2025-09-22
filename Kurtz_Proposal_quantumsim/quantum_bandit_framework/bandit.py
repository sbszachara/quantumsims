# bandit.py
# -------------------------------------------------------------
# This file defines both contextual and non-contextual multi-armed bandits.
# These are used for selecting optimal strategies for:
# 1. Real-time error correction (ContextualTSBandit)
# 2. Post-processing mitigation (NSBandit)
# The Thompson Sampling logic models the adaptive behavior described in the
# Krutz QEC framework for resource-aware decision-making.
# -------------------------------------------------------------

import numpy as np
import random

class ContextualTSBandit:
    """
    Contextual Thompson Sampling Bandit (TS-CL)
    --------------------------------------------------
    - Used for runtime error correction (QEC) strategy selection.
    - Takes in contextual telemetry (e.g., noise class: idle, coherent-noise).
    - Applies Thompson Sampling to select optimal QEC strategy
      (e.g., full_qec, light_qec, inaction) based on historical fidelity rewards.
    """
    def __init__(self, strategies, context_classes):
        self.strategies = strategies
        self.contexts = context_classes

        # Alpha and Beta parameters for Beta distributions, per context and strategy
        self.alpha = {
            context: {strategy: 1 for strategy in strategies}
            for context in context_classes
        }
        self.beta = {
            context: {strategy: 1 for strategy in strategies}
            for context in context_classes
        }

    def select(self, context):
        # Sample from Beta distribution for each strategy in current context
        samples = {
            strategy: np.random.beta(self.alpha[context][strategy],
                                     self.beta[context][strategy])
            for strategy in self.strategies
        }
        # Return the strategy with the highest sampled reward
        return max(samples, key=samples.get)

    def update(self, context, strategy, reward):
        # Reward = normalized fidelity or success metric
        self.alpha[context][strategy] += reward
        self.beta[context][strategy] += 1 - reward


class NSBandit:
    """
    Non-Contextual Bandit (Naive Strategy Selector)
    --------------------------------------------------
    - Used for post-processing strategy selection (e.g., PEC, ZNE, MEM, none).
    - Ignores contextual telemetry; uses average observed fidelity to select strategy.
    - Can be extended with metadata for contextual logic.
    """
    def __init__(self, strategies):
        self.strategies = strategies
        self.alpha = {strategy: 1 for strategy in strategies}
        self.beta = {strategy: 1 for strategy in strategies}

    def select(self):
        # Sample from Beta distributions and pick the best
        samples = {
            strategy: np.random.beta(self.alpha[strategy], self.beta[strategy])
            for strategy in self.strategies
        }
        return max(samples, key=samples.get)

    def update(self, strategy, reward):
        # Update belief about strategy effectiveness
        self.alpha[strategy] += reward
        self.beta[strategy] += 1 - reward
