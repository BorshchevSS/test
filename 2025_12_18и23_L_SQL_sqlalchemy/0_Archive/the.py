# pip install sqlalchemy

# import sqlalchemy
#
# int  - Integer
# str  -  String(length)
# str  - Text
# bool - Boolean (true/false)
# float - Float() Numeric()
# datetime.datetime  - DateTime()
# datetime.date - Date()
# Enum()
# Mapped[int] Integer

from sqlalchemy import (create_engine,
                        String, Integer,
                        ForeignKey, Table, Column)
from sqlalchemy.orm import (DeclarativeBase,
                            Mapped,
                            mapped_column, relationship, Session)

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    # id = Column(Integer(), )
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    books: Mapped[list['Book']] = relationship(back_populates='author', cascade="all, delete-orphan") #cascade="delete-orphan" каскадное удаление
    bio: Mapped['AuthorBio'] = relationship(back_populates='bio',
                                            cascade='all, delete-orphan',
                                            uselist=False)

    def __repr__(self):
        return f"Author: id={self.id}, name={self.name}"

# МНОГИЕ-КО-МНОГИМ

book_genre_association = Table(
    "book_genre", Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE"), primary_key=True),
    Column('genre_id', Integer,ForeignKey('genres.id', ondelete='CASCADE'), primary_key=True)
)

class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    author: Mapped['Author'] = relationship(back_populates='books')
    genres: Mapped[list["Genre"]] = relationship(
        "Genre", secondary=book_genre_association, back_populates="books", lazy="select"
    )

class AuthorBio(Base):
    __tablename__ = 'author_bios'
    id: Mapped[int] = mapped_column(primary_key=True)
    bio_text: Mapped[str] = mapped_column(String(200))
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'),
                                           unique=True, nullable=False)
    author: Mapped['Author'] = relationship(
        back_populates='bio', lazy='joined'
    )
    def __repr__(self):
        return f'AuthorBio: id={self.id}, author_id={self.author_id}'

class Genre(Base):
    __tablename__ = "genres"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    books: Mapped[list["Book"]] = relationship(
        secondary=book_genre_association,
        back_populates="genres",
        lazy="select"
    )

def create_database():
    engine = create_engine("sqlite:///library.db", echo=True)
    Base.metadata.create_all(engine)
    print("Базы данных и таблицы созданы")
    return engine

if __name__=="__main__":
    engie = create_database()