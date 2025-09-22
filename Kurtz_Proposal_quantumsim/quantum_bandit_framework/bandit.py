import random
from collections import defaultdict

class ContextualTSBandit:
    def __init__(self, arms):
        self.arms = arms
        self.rewards = defaultdict(lambda: defaultdict(list))

    def choose_arm(self, context):
        means = {}
        for arm in self.arms:
            r = self.rewards[context][arm]
            means[arm] = random.gauss(sum(r)/len(r), 0.1) if r else random.random()
        return max(means, key=means.get)

    def update(self, context, arm, reward):
        self.rewards[context][arm].append(reward)


class NSBandit:
    def __init__(self, arms):
        self.arms = arms
        self.rewards = defaultdict(list)

    def choose_arm(self):
        def score(r): return sum(r[-5:]) / min(5, len(r)) if r else random.random()
        return max(self.arms, key=lambda arm: score(self.rewards[arm]))

    def update(self, arm, reward):
        self.rewards[arm].append(reward)