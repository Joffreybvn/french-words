"""Initial migration.

Revision ID: 4768fdbe3936
Revises: 
Create Date: 2023-03-08 21:57:42.462313

"""
from datetime import date
from alembic import op
from sqlalchemy import Column, Integer, String, Date, Identity


# revision identifiers, used by Alembic.
revision = '4768fdbe3936'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'word',
        Column("id", Integer, Identity(start=1), primary_key=True),
        Column("slug", String(150), unique=True, nullable=False),
        Column("title", String(150), nullable=False),
        Column("creation_date", Date, default=date.today()),
        Column("phonetic", String(150)),
        Column("translation_en", String(150)),
        Column("translation_es", String(150)),
    )


def downgrade():
    op.drop_table('word')
