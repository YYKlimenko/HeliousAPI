from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    ...


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(64))
    picture_url: Mapped[str] = mapped_column(String(100))

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f'User(id={self.id}, login={self.username})'


class Comment(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())


class Author(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(1000))
    picture_url: Mapped[str] = mapped_column(String(100))

    albums: Mapped['Album'] = relationship(back_populates='author')


class Album(Base):
    title: Mapped[str] = mapped_column(String(50))
    picture_url: Mapped[str] = mapped_column(String(100))
    date_published: Mapped[datetime] = mapped_column()
    description: Mapped[str] = mapped_column(String(1000))

    authors: Mapped[Author] = relationship(back_populates='albums')


class Text(Base):
    title: Mapped[str] = mapped_column(String(50))
    album: Mapped[Album] = relationship(back_populates='text')
    body: Mapped[str] = mapped_column(String(5000))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())

    authors: Mapped[Author] = relationship(back_populates='texts')


class Quote(Base):
    text: Mapped[Author] = relationship(back_populates='quotes')
    begin: Mapped[int] = mapped_column()
    end: Mapped[int] = mapped_column()
    comment: Mapped[Comment] = relationship(back_populates='quotes')
