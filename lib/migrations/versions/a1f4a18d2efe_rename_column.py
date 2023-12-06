"""rename column

Revision ID: a1f4a18d2efe
Revises: 1e556f04bd58
Create Date: 2023-12-06 17:54:34.253930

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer


# revision identifiers, used by Alembic.
revision = 'a1f4a18d2efe'
down_revision = '1e556f04bd58'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('scholars', 'grade', new_column_name='darasa', existing_type=Integer)


def downgrade():
    op.alter_column('scholars', 'darasa', new_column_name='grade', existing_type=Integer)

