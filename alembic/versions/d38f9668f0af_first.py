"""first

Revision ID: d38f9668f0af
Revises: 
Create Date: 2024-12-05 13:16:40.466748

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd38f9668f0af'
down_revision: Union[str, None] = None
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
