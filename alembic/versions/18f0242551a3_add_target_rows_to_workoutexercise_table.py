"""add target rows to WorkoutExercise table

Revision ID: 18f0242551a3
Revises: be97a10e0128
Create Date: 2026-04-29 16:00:28.391394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18f0242551a3'
down_revision: Union[str, Sequence[str], None] = 'be97a10e0128'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
