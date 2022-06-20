"""add user_table

Revision ID: df8b35145b4c
Revises: c2748aa52810
Create Date: 2022-06-18 17:58:26.447021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df8b35145b4c'
down_revision = 'c2748aa52810'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users_table',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                            server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:

    op.drop_table('users_table')
    pass
