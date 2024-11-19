"""add content column to posts table

Revision ID: 34922c8d8995
Revises: aa43080dd2d8
Create Date: 2024-11-10 21:27:08.048919

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34922c8d8995'
down_revision: Union[str, None] = 'aa43080dd2d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
