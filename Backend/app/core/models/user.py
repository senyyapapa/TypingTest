from pydantic import BaseModel
from sqlalchemy import ForeignKey

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = 'users'
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[bytes]
    results: Mapped[list["Result"]] = relationship(back_populates="user")

class Result(Base):
    __tablename__ = 'results'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    result: Mapped[int] = mapped_column()

    user: Mapped["User"] = relationship(back_populates="results")
