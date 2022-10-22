"""add last few columns to posts table

Revision ID: 177ccfecaf85
Revises: 863b924e66db
Create Date: 2022-10-20 00:27:00.017998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '177ccfecaf85'
down_revision = '863b924e66db'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
