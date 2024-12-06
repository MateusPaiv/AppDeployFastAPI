"""create todo table

Revision ID: c0d1f1e13d71
Revises: 
Create Date: 2024-12-06 10:05:59.163553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0d1f1e13d71'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'todo',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        sa.Column('is_completed', sa.Boolean()),
    )


def downgrade() -> None:
    op.drop_table('todo')
