import random

from fastapi import APIRouter
import os
router = APIRouter(prefix="/get_words")

script_dir = os.path.dirname(__file__)
words_path = os.path.join(script_dir, 'words.txt')

words = [
    "apple", "banana", "orange", "grape", "peach", "pear", "plum", "cherry", "melon", "kiwi",
    "table", "chair", "lamp", "sofa", "desk", "shelf", "carpet", "pillow", "curtain", "drawer",
    "dog", "cat", "bird", "fish", "rabbit", "hamster", "turtle", "snake", "horse", "cow",
    "house", "building", "school", "hospital", "church", "store", "park", "stadium", "bridge", "tower",
    "book", "pen", "pencil", "eraser", "notebook", "marker", "ruler", "scissors", "tape", "glue",
    "red", "blue", "green", "yellow", "purple", "pink", "black", "white", "gray", "brown",
    "happy", "sad", "angry", "scared", "excited", "bored", "tired", "hungry", "thirsty", "confused",
    "run", "walk", "jump", "swim", "fly", "read", "write", "listen", "speak", "sing",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "spring", "summer", "winter"
]

@router.get("/words")
async def get_words(words_random: list[str] = words):
    random.shuffle(words_random)
    return {"words": words_random}