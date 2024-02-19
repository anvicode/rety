from datetime import timezone

from sqlalchemy import UUID, Column, DateTime, Float, String, Text, create_engine, func
from sqlalchemy.orm import declarative_base

sqlite_database = "sqlite:///db_films.sqlite"


engine = create_engine(sqlite_database)


Base = declarative_base()


class FilmWork(Base):
    __tablename__ = "film_work"

    id = Column(UUID, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    creation_date = Column(DateTime)
    file_path = Column(Text, nullable=True)
    rating = Column(Float)
    type = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(tz=timezone.utc))
    updated_at = Column(DateTime, onupdate=func.now(tz=timezone.utc))


# class TodoItem(Base):
#     __tablename__ = "todo_item"

#     id = Column(UUID, primary_key=True)
#     title = Column(String(50), nullable=False)
#     list_id = Column(ForeignKey(TodoList.id), nullable=False)
#     completed = Column(Boolean, default=False)
#     created_at = Column(DateTime, server_default=func.now(tz=timezone.utc))

Base.metadata.create_all(engine)

print("Database tables created")
