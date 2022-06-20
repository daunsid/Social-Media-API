"""add contents to post_table

Revision ID: c2748aa52810
Revises: bf1b1ea4ee85
Create Date: 2022-06-18 17:52:56.739368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2748aa52810'
down_revision = 'bf1b1ea4ee85'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post_table', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('post_table', 'content')
    pass
