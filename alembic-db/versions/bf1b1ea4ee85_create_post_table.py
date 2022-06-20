"""create post_table

Revision ID: bf1b1ea4ee85
Revises: 
Create Date: 2022-06-18 17:34:41.693289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf1b1ea4ee85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('post_table', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_table("post_table")
    pass
