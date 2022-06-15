from fastapi import FastAPI, Depends, HTTPException
from starlette import status
import schemas
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


app = FastAPI()


# покажи все книги
@app.get("/",
         summary="List of all books.")
def getBook(session: Session = Depends(get_session)):
    """
    List of all books.
    """
    books = session.query(models.Book).all()
    return books


# найди книгу по id
@app.get("/{id}",
         summary="Search for a book by ID.")
def getBook(id: int,
            session: Session = Depends(get_session)):
    """
    Search for a book by **ID**.
    """
    book = session.query(models.Book).get(id)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Student not found.")


# добавить книгу
@app.post("/",
          status_code=status.HTTP_201_CREATED,
          summary="Add a new book.")
def addBook(book: schemas.BooksBase, session: Session = Depends(get_session)):
    """
    Add a new book.
    **Title** title of the book,
    **Author** author of the book,
    **Pages** number of pages,
    **Section** number of chapters.
    """
    book = models.Book(title=book.title,
                       author=book.author,
                       pages=book.pages,
                       section=book.section)
    session.add(book)
    session.commit()
    session.refresh(book)

    return book


# изменить
@app.put("/{id}",
         summary="Сhange book parameters.")
def updateBook(id: int, book: schemas.BooksBase, session: Session = Depends(get_session)):
    """
    Сhange book parameters.
    """
    bookObject = session.query(models.Book).get(id)
    bookObject.title = book.title
    bookObject.author = book.author
    bookObject.pages = book.pages
    bookObject.section = book.section
    session.commit()
    return bookObject


# удалить
@app.delete("/{id}",
            status_code=status.HTTP_204_NO_CONTENT,
            summary="Delete a book.")
def deleteBook(id: int, session: Session = Depends(get_session)):
    """
    Delete a book.
    """
    bookObject = session.query(models.Book).get(id)
    session.delete(bookObject)
    session.commit()
    session.close()
    return 'deleted...'
