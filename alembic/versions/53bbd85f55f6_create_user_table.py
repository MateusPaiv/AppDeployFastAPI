"""create user table

Revision ID: 53bbd85f55f6
Revises: c0d1f1e13d71
Create Date: 2024-12-06 10:41:26.301197

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid

# revision identifiers, used by Alembic.
revision: str = '53bbd85f55f6'
down_revision: Union[str, None] = 'c0d1f1e13d71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('auth_id', sa.UUID, default=lambda: str(uuid.uuid4()), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('email', sa.String(150), nullable=False, unique=True),
    )
    op.add_column('todo', sa.Column('user_id', sa.Integer(), nullable=True))
                           #nome fk      #tab fk  #tab ref  #col na todo  #col na user
    op.create_foreign_key('fk_todo_user', 'todo', 'user', ['user_id'], ['id'],)

def downgrade() -> None:
    op.drop_table('user')
