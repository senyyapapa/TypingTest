import random
from fastapi import APIRouter
import os

from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

router = APIRouter(prefix="/get_words")

script_dir = os.path.dirname(__file__)
words_path = os.path.join(script_dir, 'words.txt')

def load_words():
    with open(words_path, 'r', encoding='utf-8') as file:
        return [word.strip() for word in file.readlines()]

@router.get("/words")
async def get_words():
    all_words = load_words()
    selected_words = random.sample(all_words, 45)
    random.shuffle(selected_words)
    return {"words": selected_words}
