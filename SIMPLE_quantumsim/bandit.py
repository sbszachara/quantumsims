import random

class SimpleBandit:
    def __init__(self):
        self.arms = ['strategy_1', 'strategy_2']
    
    def choose_arm(self):
        # For now, just randomly choose an arm
        return random.choice(self.arms)

if __name__ == "__main__":
    bandit = SimpleBandit()
    print(bandit.choose_arm())
