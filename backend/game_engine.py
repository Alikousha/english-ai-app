import random

class UserState:
    def __init__(self):
        self.xp = 0
        self.level = 1
        self.hearts = 5
        self.correct = 0
        self.wrong = 0
        self.mastery = {}  # word -> score

    def add_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 100:
            self.level += 1
            self.xp = 0

    def lose_heart(self):
        self.hearts -= 1
        if self.hearts < 0:
            self.hearts = 0

    def gain_mastery(self, word):
        self.mastery[word] = self.mastery.get(word, 0) + 1

    def fail_word(self, word):
        self.mastery[word] = self.mastery.get(word, 0) - 1
