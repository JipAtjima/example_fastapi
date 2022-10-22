"""add content column to posts table

Revision ID: a322000b9314
Revises: f218892e36c3
Create Date: 2022-10-19 22:30:25.111022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a322000b9314'
down_revision = 'f218892e36c3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
