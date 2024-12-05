"""test delete table teste

Revision ID: 7bda35869c99
Revises: b7c69a9150c3
Create Date: 2024-12-05 15:55:24.806873

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7bda35869c99'
down_revision: Union[str, None] = 'b7c69a9150c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('teste')


def downgrade() -> None:
    op.create_table(
        'teste',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(50)),
            sa.Column('desccription', sa.String(150)),
        )
