import random

class LessonEngine:

    def __init__(self, units):
        self.units = units

    def get_lesson_words(self, unit_name, limit=5):
        words = self.units[unit_name]

        # random but stable lesson
        selected = random.sample(words, min(limit, len(words)))
        return selected

    def check_answer(self, correct, user_answer):
        return correct.lower().strip() == user_answer.lower().strip()
