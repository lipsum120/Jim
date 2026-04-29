"""drop ExerciseSet table

Revision ID: 83638a0ffd23
Revises: 82bbbb3e33aa
Create Date: 2026-04-29 15:54:35.229261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83638a0ffd23'
down_revision: Union[str, Sequence[str], None] = '82bbbb3e33aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_table("ExerciseSet")


def downgrade() -> None:
    """Downgrade schema."""
    pass
