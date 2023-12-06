"""Renaming students to scholars

Revision ID: 1e556f04bd58
Revises: 791279dd0760
Create Date: 2023-12-06 14:44:55.540662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e556f04bd58'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
