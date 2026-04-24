from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

# IMPORT YOUR REAL UNITS
from vocab_data.unit1 import unit1
from vocab_data.unit2 import unit2
from vocab_data.unit3 import unit3
from vocab_data.unit4 import unit4
from vocab_data.unit5 import unit5
from vocab_data.unit6 import unit6
from vocab_data.unit7 import unit7
from vocab_data.unit8 import unit8
from vocab_data.unit9 import unit9
from vocab_data.unit10 import unit10

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# convert {"topic": [(word, meaning), ...]} → [(word, meaning), ...]
def normalize(unit_dict):
    return list(unit_dict.values())[0]

DATA = {
    "1": normalize(unit1),
    "2": normalize(unit2),
    "3": normalize(unit3),
    "4": normalize(unit4),
    "5": normalize(unit5),
    "6": normalize(unit6),
    "7": normalize(unit7),
    "8": normalize(unit8),
    "9": normalize(unit9),
    "10": normalize(unit10),
}

@app.get("/question")
def question(unit: str = "1"):
    pool = DATA[unit]
    word = random.choice(pool)

    correct = word[1]

    # build fake options from other meanings
    all_meanings = [w[1] for w in pool]
    options = random.sample(all_meanings, min(3, len(all_meanings)))
    if correct not in options:
        options[0] = correct

    random.shuffle(options)

    return {
        "word": word[0],
        "correct": correct,
        "options": options
    }
