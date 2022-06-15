from pydantic import BaseModel


class BooksBase(BaseModel):
    title: str
    author: str
    pages: int
    section: int = None
