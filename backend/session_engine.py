import random

class SessionEngine:
    def __init__(self):
        self.sessions = {}

    def start_session(self, user_id, unit_words):
        words = unit_words.copy()

        random.shuffle(words)

        self.sessions[user_id] = {
            "words": words,
            "index": 0,
            "score": 0,
            "wrong_queue": [],
            "finished": False
        }

        return self.sessions[user_id]

    def get_current_word(self, user_id):
        session = self.sessions[user_id]

        if session["index"] >= len(session["words"]):
            if session["wrong_queue"]:
                session["words"] = session["wrong_queue"]
                session["wrong_queue"] = []
                session["index"] = 0
            else:
                session["finished"] = True
                return None

        return session["words"][session["index"]]

    def submit_answer(self, user_id, correct_word, user_answer):
        session = self.sessions[user_id]

        is_correct = user_answer.lower().strip() == correct_word.lower().strip()

        if is_correct:
            session["score"] += 1
            session["index"] += 1
        else:
            session["wrong_queue"].append((correct_word))
            session["index"] += 1

        return {
            "correct": is_correct,
            "score": session["score"],
            "finished": session["finished"]
        }

    def progress(self, user_id):
        session = self.sessions[user_id]
        total = len(session["words"])
        done = session["index"]
        return int((done / total) * 100) if total > 0 else 0
