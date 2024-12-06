"""teste

Revision ID: 69483e206196
Revises: 738b3f3d51b2
Create Date: 2024-12-06 17:07:06.063527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.utils.create_method import ReplaceableObject

# revision identifiers, used by Alembic.
revision: str = '69483e206196'
down_revision: Union[str, None] = '738b3f3d51b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

customer_view = ReplaceableObject(
    "todo_users_views",
    """
        SELECT
            t.title AS todo_title,
            t.description AS todo_description,
            t.is_completed AS todo_is_completed,
            t.user_id AS user_id,
            u.name AS user_name
        FROM
            todo t
        JOIN
            "user" u ON t.user_id = u.id;
    """)

def upgrade() -> None:
    downgrade()


def downgrade() -> None:
    op.drop_view(customer_view)
