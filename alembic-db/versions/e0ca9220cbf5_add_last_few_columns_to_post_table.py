"""add last few columns to post_table

Revision ID: e0ca9220cbf5
Revises: 77df4c2be424
Create Date: 2022-06-18 18:28:25.427548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0ca9220cbf5'
down_revision = '77df4c2be424'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.add_column('post_table', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('post_table', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:

    op.drop_column('post_table', 'published')
    op.drop_column('post_table', 'created_at')
    pass
