"""test deploy

Revision ID: b7c69a9150c3
Revises: 6ed15f76953b
Create Date: 2024-12-05 15:45:43.287285

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7c69a9150c3'
down_revision: Union[str, None] = '6ed15f76953b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'teste',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(50)),
            sa.Column('desccription', sa.String(150)),
        )

def downgrade() -> None:
    op.drop_table('teste')

