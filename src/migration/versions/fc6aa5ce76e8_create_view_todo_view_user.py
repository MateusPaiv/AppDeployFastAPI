"""create view todo_view_user

Revision ID: fc6aa5ce76e8
Revises: 
Create Date: 2024-12-11 14:57:24.513696

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.core.utils.create_method import ReplaceableObject
# revision identifiers, used by Alembic.
revision: str = 'fc6aa5ce76e8'
down_revision: Union[str, None] = None
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
    op.create_view(customer_view)


def downgrade() -> None:
    op.drop_view(customer_view)