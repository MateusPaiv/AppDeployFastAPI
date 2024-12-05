"""second

Revision ID: 6ed15f76953b
Revises: d38f9668f0af
Create Date: 2024-12-05 13:39:42.507211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from alembic_funcs import ReplaceableObject

# revision identifiers, used by Alembic.
revision: str = '6ed15f76953b'
down_revision: Union[str, None] = 'd38f9668f0af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

customer_view = ReplaceableObject(
    "vendas_view",
    """
        SELECT 
        p.nome AS produto_nome,
        p.valor AS produto_valor,
        p.descricao AS produto_descricao,
        s.total AS venda_total,
        c.name AS cliente_nome,
        c.age AS cliente_idade
    FROM 
        produto p
    JOIN 
        sale s ON p.id = s.produto_id
    JOIN 
        customer c ON s.customer_id = c.id;
    """)

def upgrade() -> None:
    op.drop_table('teste')
    op.create_table(
        'employee',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(50)),
            sa.Column('birthday', sa.String(150)),
            sa.Column('bank', sa.String(150)),
        )
    op.create_view(customer_view)


def downgrade() -> None:
    op.drop_table('employee')
    op.drop_view(customer_view)
    op.create_table(
        'teste',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(50)),
            sa.Column('desccription', sa.String(150)),
        )
    
