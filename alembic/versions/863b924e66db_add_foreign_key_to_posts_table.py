"""add foreign-key to posts table

Revision ID: 863b924e66db
Revises: a3a37710c505
Create Date: 2022-10-20 00:13:07.868098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '863b924e66db'
down_revision = 'a3a37710c505'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table="posts",referent_table="users",
    local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_user_fk',table_name="posts")
    op.drop_column("posts",'owner_id')
    pass
