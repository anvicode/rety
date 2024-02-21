from datetime import timezone

from sqlalchemy import (
    UUID,
    Column,
    DateTime,
    Float,
    ForeignKey,
    String,
    Table,
    Text,
    func,
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.schema import PrimaryKeyConstraint

Base = declarative_base()


association_table = Table(
    "association",
    Base.metadata,
    Column("genre_id", ForeignKey("genre.id")),
    Column("film_work_id", ForeignKey("film_work.id")),
)


class FilmWork(Base):
    __tablename__ = "film_work"

    id = Column(UUID, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    creation_date = Column(DateTime, nullable=True)
    file_path = Column(Text, nullable=True)
    rating = Column(Float)
    type = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(tz=timezone.utc))
    updated_at = Column(DateTime, onupdate=func.now(tz=timezone.utc))

    genrefilmwork = relationship(
        "GenreFilmWork",
        back_populates="FilmWork",
        secondary=association_table,
        cascade="all, delete-orphan",
    )
    personfilmwork = relationship(
        "PersonFilmWork",
        back_populates="FilmWork",
        secondary=association_table,
        cascade="all, delete-orphan",
    )


class Genre(Base):
    __tablename__ = "genre"

    id = Column(UUID, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now(tz=timezone.utc))
    updated_at = Column(DateTime, onupdate=func.now(tz=timezone.utc))

    # genrefilmwork = relationship("GenreFilmWork", back_populates="Genre")


class Person(Base):
    __tablename__ = "person"

    id = Column(UUID, primary_key=True)
    full_name = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(tz=timezone.utc))
    updated_at = Column(DateTime, onupdate=func.now(tz=timezone.utc))

    # personfilmwork = relationship("PersonFilmWork", back_populates="Person")


class GenreFilmWork(Base):
    __tablename__ = "genre_film_work"
    __table_args__ = (PrimaryKeyConstraint("film_work_id", "genre_id"),)

    film_work_id = Column(ForeignKey(FilmWork.id), nullable=False)
    genre_id = Column(ForeignKey(Genre.id), nullable=False)
    created_at = Column(DateTime, server_default=func.now(tz=timezone.utc))

    # filmwork = relationship(
    #     "FilmWork", back_populates="GenreFilmWork", cascade="all, delete-orphan"
    # )
    # genre = relationship(
    #     "Genre", back_populates="GenreFilmWork", cascade="all, delete-orphan"
    # )


class PersonFilmWork(Base):
    __tablename__ = "person_film_work"
    __table_args__ = (PrimaryKeyConstraint("film_work_id", "person_id"),)

    film_work_id = Column(ForeignKey(FilmWork.id), nullable=False)
    person_id = Column(ForeignKey(Person.id), nullable=False)
    role = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(tz=timezone.utc))

    # filmwork = relationship(
    #     "FilmWork", back_populates="PersonFilmWork", cascade="all, delete-orphan"
    # )
    # person = relationship(
    #     "Person", back_populates="PersonFilmWork", cascade="all, delete-orphan"
    # )
