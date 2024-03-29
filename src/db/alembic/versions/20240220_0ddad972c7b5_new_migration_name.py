"""new_migration_name

Revision ID: 0ddad972c7b5
Revises: 644d3b4742f1
Create Date: 2024-02-20 13:58:03.078272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ddad972c7b5'
down_revision: Union[str, None] = '644d3b4742f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('film_work', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('film_work', sa.Column('creation_date', sa.DateTime(), nullable=True))
    op.add_column('film_work', sa.Column('file_path', sa.Text(), nullable=True))
    op.alter_column('film_work', 'title',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=False)
    op.alter_column('genre', 'name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=False)
    op.drop_column('genre_film_work', 'id')
    op.alter_column('person', 'full_name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=False)
    op.alter_column('person_film_work', 'role',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=False)
    op.drop_column('person_film_work', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person_film_work', sa.Column('id', sa.UUID(), autoincrement=False, nullable=False))
    op.alter_column('person_film_work', 'role',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
    op.alter_column('person', 'full_name',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
    op.add_column('genre_film_work', sa.Column('id', sa.UUID(), autoincrement=False, nullable=False))
    op.alter_column('genre', 'name',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
    op.alter_column('film_work', 'title',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
    op.drop_column('film_work', 'file_path')
    op.drop_column('film_work', 'creation_date')
    op.drop_column('film_work', 'description')
    # ### end Alembic commands ###
