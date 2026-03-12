"""fix agent_id type

Revision ID: feaf9e42a509
Revises: d1b266318732
Create Date: 2026-03-09 14:55:34.999818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'feaf9e42a509'
down_revision: Union[str, None] = 'd1b266318732'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.execute(
        "ALTER TABLE portfolio_snapshots "
        "ALTER COLUMN agent_id TYPE uuid USING agent_id::uuid"
    )


def downgrade():

    op.execute(
        "ALTER TABLE portfolio_snapshots "
        "ALTER COLUMN agent_id TYPE varchar"
    )
