# int - Integer
# str - String(length)
# str - Text
# bool - Boolean (true\false)
# float - Float() Numeric()
# datetime.datetime - DateTime()
# datetime.date - Date()
# Enum() Перечисление определённых значений
# Mappped[int] Integer

from sqlalchemy import (create_engine,
                        String, Integer,
                        ForeignKey)
from sqlalchemy.orm import (DeclarativeBase,
                            Mapped,
                            mapped_column, relationship)

class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False) # nullable=False не может быть пустым; String(30) строка максимальной длины 30
    books: Mapped[list['Book']] = relationship(back_populates="author", cascade="all, delete-orphan")
    bio: Mapped["AuthorBio"] = relationship(back_populates="bio", cascade="all, delete-orphan")

# Один-ко-многим
class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id", ondelete="CASCADE")) #set null restrict-запрет удаления
    author: Mapped["Author"] = relationship(back_populates="books", lazy="dynamic") #lazy=Принцип загрузки

    def __repr__(self):
        return  f"Book: id={self.id}, name={self.name}, author_id={self.author_id}"

# Один-к-одному
class AuthorBio(Base):
    __tablename__ = "author_bios"
    id: Mapped[int] = mapped_column(primary_key=True)
    bio_text: Mapped[str] = mapped_column(String(200))
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), unique=True, nullable=False)
    author: Mapped["Author"] = relationship(
        back_populates="bio", lazy="joined"
    )
    def __repr__(self):
        return f"AuthorBio: id={self.id}, author_id={self.author_id}"