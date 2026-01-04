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
                        ForeignKey, Table, Column, select)
from sqlalchemy.orm import (DeclarativeBase,
                            Mapped,
                            mapped_column, relationship, Session)

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    # id = Column(Integer(), )
    name: Mapped[str] = mapped_column(String(30), nullable=False) # unique=True
    books: Mapped[list['Book']] = relationship(back_populates='author',
                                               cascade='all, delete-orphan') #save-update
    bio: Mapped['AuthorBio'] = relationship(back_populates='author',
                                            cascade='all, delete-orphan',
                                            uselist=False)
    def __repr__(self):
        return f'Author: id={self.id}, name={self.name}'

# МНОГИЕ-КО-МНОГИМ

book_genre_association = Table(
    'book_genre', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id',
                                          ondelete='CASCADE'),
           primary_key=True),
           Column('genre_id', Integer, ForeignKey('genres.id',
                                                  ondelete='CASCADE'),
                  primary_key=True)
)



# ОДИН-КО-МНОГИМ
class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id',
                                                      ondelete='CASCADE')) #SET NULL | RESTRICT
    author: Mapped['Author'] = relationship(back_populates='books',
                                            lazy='joined')
    genres: Mapped[list['Genre']] = relationship(
        'Genre', secondary=book_genre_association,
        back_populates='books', lazy='select'
    )

    # back_populates - название атрибута связи (двусторонняя связь)
    # ForeignKey через таблицы обращаемся к атрибуту (id)
    # в Mapped указываем название модели(класса)

    def __repr__(self):
        return f'Book: id={self.id}, name={self.name}, author_id={self.author_id}'

# ОДИН-К-ОДНОМУ
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
    __tablename__ = 'genres'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    books: Mapped[list['Book']] = relationship(secondary=book_genre_association,
        back_populates='genres',
        lazy='select'
    )

def create_database():
    engine = create_engine('sqlite:///library.db', echo=True)
    Base.metadata.create_all(engine)
    print('База данных и таблицы созданы ')
    return engine

def test(engine):
    with Session(engine) as session:
#         один-ко-многим
        author1 = Author(name='Дж.К.Роулинг')
        book1 = Book(name='Гарри Поттер и филосовский камень', author=author1)
        book2 = Book(name='Фантастические твари и места их обитания', author=author1)
        session.add_all([author1, book1, book2]) # add-для одной записи, add_all-список для добавления
        session.commit()
#         проверка связи от автора к книгам
        print(f'Author: {author1.name}')
        print(f'Books: {[b.name for b in author1.books]}')
        print(f'Book {book1.name} by {book1.author.name}')
#         один-к-одному
        bio = AuthorBio(bio_text='Британская писательница...', author=author1)
        session.add(bio)
        session.commit()
        print(f'Author Bio: {author1.bio.bio_text}')
        print(f'Bio {bio.author.name}')

# Многие-ко-многим
        novel = Genre(name='Роман')
        fiction = Genre(name='Художественная литература')
        book1.genres.extend([novel, fiction])
        session.add_all([novel, fiction])
        session.commit()
        print(f'Genres book {book1.name}: {[g.name for g in book1.genres]}')
        print(f'Books {novel.name}: {[b.name for b in novel.books]}')

#         запросы
# все книги в жанре Роман
        query = select(Book).join(Book.genres).where(Genre.name == 'Роман')
        # '''select * from books as b join book_genre_association as bga
        # on b.id = bga.book_id join genres as g on bga.genre_id = g.id
        #  where g.name = "Роман"; '''
        print(query)
        novel_books = session.scalars(query).all()
        print(novel_books)
        print([b.name for b in novel_books])





if __name__ == '__main__':
    engine = create_database()
    test(engine)
