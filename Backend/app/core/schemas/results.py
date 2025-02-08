from pydantic import BaseModel, ConfigDict


class BestResult(BaseModel):
    wpm: int = 0
    accuracy: int = 0

class ResultBase(BaseModel):
    id: int
    user_id: int
    username: str
    result: int

class CreateResult(ResultBase):
    model_config = ConfigDict(strict=True)

class NewResult(ResultBase):
    model_config = ConfigDict(strict=True)