"""add foreign key to post table

Revision ID: 70368e3a3fd7
Revises: 1c37ad81026a
Create Date: 2024-11-11 08:02:55.430627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70368e3a3fd7'
down_revision: Union[str, None] = '1c37ad81026a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("user_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users", local_cols=["user_id"], remote_cols=["id"], ondelete="CASCADE")

def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", column_name="user_id")
