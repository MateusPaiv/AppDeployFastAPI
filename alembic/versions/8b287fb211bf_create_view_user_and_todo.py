"""create view user and todo

Revision ID: 8b287fb211bf
Revises: 53bbd85f55f6
Create Date: 2024-12-06 12:02:43.674485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.utils.create_method import ReplaceableObject

# revision identifiers, used by Alembic.
revision: str = '8b287fb211bf'
down_revision: Union[str, None] = '53bbd85f55f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


customer_view = ReplaceableObject(
    "todo_views",
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
    op.create_view(customer_view)


def downgrade() -> None:
    op.drop_view(customer_view)
