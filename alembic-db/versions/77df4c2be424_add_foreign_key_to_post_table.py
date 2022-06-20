"""add foreign key to post_table

Revision ID: 77df4c2be424
Revises: df8b35145b4c
Create Date: 2022-06-18 18:17:08.069342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77df4c2be424'
down_revision = 'df8b35145b4c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post_table', sa.Column('owner_id', sa.Integer(), nullable= False))
    op.create_foreign_key('post_users_fk', source_table='post_table', referent_table="users_table",
                        local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='post_table')
    op.drop_column('post_table', 'owner_id')
    pass
